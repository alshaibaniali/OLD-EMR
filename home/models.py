from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name =     models.CharField(max_length=30)
    last_name  =     models.CharField(max_length=30)
    username =       models.CharField(max_length=30, unique=True)
    email =          models.EmailField(verbose_name="email", max_length=60, unique=True)
    password1 =      models.CharField(max_length=30)
    password2 =      models.CharField(max_length=30)
    #date_joined =    models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    #last_login =     models.DateTimeField(verbose_name='last login', auto_now=True)
    #is_admin =       models.BooleanField(default=False)
    #is_staff =       models.BooleanField(default=False)
    #is_superuser =   models.BooleanField(default=False)
    #is_active =      models.BooleanField(default=True)

#-----------------changes from here --------------------------------------------------------
    gender =         models.CharField(max_length=50,default="None")
    doc_id =         models.CharField(primary_key=True,max_length=50)
    dept =           models.CharField(max_length=50)
    hospital =       models.CharField(max_length=20)
    phone =          models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+";"+self.last_name+";"+self.username+";"+self.gender+";"+self.doc_id+";"+self.dept+";"+self.hospital+";"+self.email+";"+self.phone+";"+self.password1+";"+self.password2

#---------------------------till here----------------------------------------------


class Login(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    # class DoctorRegistration(models.Model):
    #     first_name =     models.CharField(max_length=30)
    #     last_name  =     models.CharField(max_length=30)
    #     username =       models.CharField(max_length=30, unique=True)
    #     email =          models.EmailField(verbose_name="email", max_length=60, unique=True)
    #     phone =          models.CharField(max_length=20)
    #     password1 =      models.CharField(max_length=30)
    #     password2 =      models.CharField(max_length=30)

