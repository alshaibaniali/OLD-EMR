from django.contrib import admin
from .models import DoctorRegistration
from .models import  Doctors
from .models import  Patients
# Register your models here.


admin.site.register(DoctorRegistration)
admin.site.register(Doctors)
admin.site.register(Patients)