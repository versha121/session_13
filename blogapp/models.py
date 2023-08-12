from django.db import models

# Create your models here.

# class UserRegister(models.Model):
#     email=models.CharField('email',max_length=10,null=True,default="")
#     fname=models.CharField('fname',max_length=10,null=True,default="")
#     name=models.CharField('name',max_length=10,null=True,default="")
#     Class=models.IntegerField('Class',max_length=10,null=True,default="")
#     age=models.IntegerField('age',max_length=10,null=True,default="")
#     gender=models.CharField('gender',max_length=10,null=True,default="")
class Home(models.Model):
    title=models.CharField('title',max_length=20,null=True,default="")
    content=models.CharField('content',max_length=20,null=True,default="")


def __str__(self):
    return str(self.name)