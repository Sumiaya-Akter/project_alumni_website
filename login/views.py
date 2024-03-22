from asyncio.windows_events import NULL
from multiprocessing import context
from login.forms import FilterForm, UserForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from login.models import UserModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout


def home(request):
    context = {'login': False, 'membership': False}
    user = request.user
    if user.is_authenticated:
        context = {'login': True, 'membership': len(
            UserModel.objects.filter(username=user.username)) == 0}
    return render(request, 'home.html', context)


def LOGIN(request):
    if 'signup' in request.POST:
        username = request.POST.get('username')
        series = request.POST.get('series')
        userid = request.POST.get('userid')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(userid, email, pass1)

        myuser.save()

        messages.success(request, 'Your account successfully created!')

        return render(request, 'LOGIN.html')

    if 'signin' in request.POST:
        userid = request.POST.get('userid')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=userid, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid')
            return render(request, 'LOGIN.html')

    else:
        return render(request, 'LOGIN.html')


def Donor_Sponsor(request):
    print('called')
    res = UserModel.objects.raw(
        'select * from login_usermodel order by student_id asc')
    options={""}
    temp=[]
    for x in res:
        temp.append(str(x.student_id)[0:2])
    options.update(temp)
    options.pop()
    
    form=FilterForm()
    if request.method == 'POST':
            form = FilterForm(request.POST)
            if form.is_valid():
                series=form.cleaned_data['text']
                if series!='all':
                    series+='%'
                else:
                    series='%'
                print(series)
                res = UserModel.objects.raw(
        f"select * from login_usermodel where student_id like '{series}' order by student_id asc")
                
    context = {'login': False, 'membership': False,
               'members': res,
               'options':options,
               'form':form}

    user = request.user
    if user.is_authenticated:
        context = {'login': True,
                   'membership': len(
                       UserModel.objects.filter(username=user.username)) == 0,
                   'members': res,'options':options ,'form':form}
    return render(request, 'Donor_Sponsor.html', context)


def contact_us(request):
    context = {'login': False, 'membership': False}
    user = request.user
    if user.is_authenticated:
        context = {'login': True, 'membership': len(
            UserModel.objects.filter(username=user.username)) == 0}
    return render(request, 'contact_us.html', context)


def membership(request):
    context = {'login': False}
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/membership')
        if len(UserModel.objects.filter(username=user.username)) != 0:
            return redirect('/')
        form = UserForm()
        context = {'login': True, 'form': form, 'membership': True}
    else:
        return redirect('/')
    return render(request, 'membership.html', context)


def Events(request):
    context = {'login': False, 'membership': False}
    user = request.user
    if user.is_authenticated:
        context = {'login': True, 'membership': len(
            UserModel.objects.filter(username=user.username)) == 0}
    return render(request, 'Events.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('/')
