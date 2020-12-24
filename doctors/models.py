from django.db import models

# Create your models here.

class DoctorRegistration(models.Model):
    first_name =     models.CharField(max_length=30)
    last_name  =     models.CharField(max_length=30)
    username =       models.CharField(max_length=30, unique=True)
    gender =         models.CharField(max_length=50,default="None")
    doc_id =         models.CharField(primary_key=True,max_length=50)
    dept =           models.CharField(max_length=50)
    hospital =       models.CharField(max_length=20)
    email =          models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone =          models.CharField(max_length=20)
    password1 =      models.CharField(max_length=30)
    password2 =      models.CharField(max_length=30)

    def __str__(self):
        return self.first_name+";"+self.last_name+";"+self.username+";"+self.gender+";"+self.doc_id+";"+self.dept+";"+self.hospital+";"+self.email+";"+self.phone+";"+self.password1+";"+self.password2



class Doctors(models.Model):
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



class Patients(models.Model):
    name = models.CharField(max_length=50)
    AID= models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, default="None")

    type = models.CharField(max_length=50)
    stage = models.CharField(max_length=20)
    treatement=models.CharField(max_length=300)



    @staticmethod
    def validteuser(AID,email):
        print(AID,email)
        print(AID,email)
        try:
         contents=Patients.objects.get(AID=AID,email=email)
         print(contents.email)
         return 'yes'
        except Patients.DoesNotExist:
          return 0















