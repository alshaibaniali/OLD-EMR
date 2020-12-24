from django.db import models

# Create your models here.


class PatientsReg(models.Model):
    first_name =     models.CharField(max_length=30)
    last_name  =     models.CharField(max_length=30)
    username =       models.CharField(max_length=30, unique=True)
    gender =         models.CharField(max_length=50,default="None")
    doc_id =         models.CharField(primary_key=True,max_length=50)
    dept =           models.CharField(max_length=50)
    hospital =       models.CharField(max_length=20)
    email =          models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone =          models.CharField(max_length=20)
    password1 =      models.CharField(max_length=30,help_text="Minimum of 8 Characters")
    password2 =      models.CharField(max_length=30,help_text="Minimum of 8 Characters")

    def __str__(self):
        return self.first_name+";"+self.last_name+";"+self.username+";"+self.gender+";"+self.doc_id+";"+self.dept+";"+self.hospital+";"+self.email+";"+self.phone+";"+self.password1+";"+self.password2