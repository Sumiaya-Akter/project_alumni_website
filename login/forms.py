

from login.models import Filter, UserModel
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username', 'image', 'full_name', 'student_id', 'job_title', 'job_location',
                  'linked_in', 'email']
        widgets = {
            'image': forms.FileInput(attrs={
                'onchange': "readURL(this);"
            })
        }
        



class FilterForm(forms.ModelForm):

    class Meta:
        model = Filter
        fields = ['text']


