from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import Registration
from .models import Login
# from .models import DoctorRegistration

# Register your models here.

#class AccountAdmin(UserAdmin):
 #   list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
  # readonly_fields = ('date_joined', 'last_login')

   # filter_horizontal = ()
    #list_filter = ()
    #fieldsests =  ()


admin.site.register(Registration) #,AccountAdmin
admin.site.register(Login)
# admin.site.register(DoctorRegistration)

