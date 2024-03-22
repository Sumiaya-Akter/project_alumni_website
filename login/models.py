from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    full_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=9)
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    linked_in = models.CharField(max_length=255, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60)


class Filter(models.Model):
    text = models.CharField(max_length=255)
