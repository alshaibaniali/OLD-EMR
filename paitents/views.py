from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from doctors.models import Patients
from paitents.models import PatientsReg
from doctors.models import DoctorRegistration
from django.http import HttpResponseRedirect
#from django.http import HttpResponse
#from django.http import Registration
#from django.http import Login
#from .models import Destination

# Create your views here.
loginUser = ""
loginFlag = False

def index(request):

    return render(request, 'paitents/index.html')


def register(request):

    if request.method == 'POST':
       print()
       print(type(request.POST))
       print()

       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
      # gender = request.POST['gender']
       #doc_id = request.POST['doc_id']
      # dept = request.POST['dept']
       #hospital = request.POST['hospital']
       email = request.POST['email']
      # phone = request.POST['phone']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       print(username, password1, password2, email, first_name, last_name,)
         #doc_id, dept, hospital, phone, gender
       #--------------------------------------------
    #    count = 0
    #    message = ""
    #    searchObject = Doctors.objects.all()
    #    flag = 1
    #    for i in range(len(searchObject)):
    #         lst = str(searchObject[i]).split(";")
    #         print(lst[0], doc_id)
    #         if lst[0] == doc_id:
    #             message = message + "Doctor already exists.\n"
    #             flag = 0
    #             break
    #    if flag == 1:
    #         count = count + 1
      #---------------------------------------

       if password1==password2:
           if User.objects.filter(username=username).exists():
               #print('Username Taken')
               messages.info(request,'Username Taken')
               return redirect('/paitents/register')
             #  return redirect('register')

           elif User.objects.filter(email=email).exists():
                 #print('Email Already Exists')
                 messages.info(request,'Email Already Exists')
                 return redirect('/paitents/register')
           else:
                                                        #encrypt_text
            user = PatientsReg(username=username, password1=password1,password2=password2, email=email, first_name=first_name, last_name=last_name,)
           # doc_id=doc_id, dept=dept, hospital=hospital, phone=phone, gender=gender
            user.save();
            print(' User Created')
            messages.info(request,'User Created')
            return redirect('/paitents/login')

       else:
          #print('Passwords Not Matching')
          messages.info(request,'Passwords Not Matching')
          return redirect('/paitents/register')
       return redirect('/paitents/login')


    else:
          return render(request,'paitents/reg.html')





def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user=auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           return redirect('/paitents/home')
       else:
           messages.info(request,'invalid credentials')
           return redirect('/paitents/login')

    else:
       return render(request,'paitents/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/paitents/home')



#---------------------------------------------------------------------

def patientlogin(request):
    global loginFlag, loginUser
    if request.method == 'POST':
        AID = request.POST['AID']
        email = request.POST['email']

        print(AID, email)
        message = ""

        if len(Patients.objects.filter(AID=AID)) == 0:
            messages.info(request,'No Matching Accounts Found')
            #message = message + "No Matching Accounts Found"
            return redirect('/paitents/patientlogin')
        else:
            patientdetails = Patients.objects.get(AID=AID)
            print(patientdetails.email)
            print(message)
            context = {"patientdetails": patientdetails}
            return render(request, 'paitents/Phome.html', context)

    else:
        return render(request, 'paitents/index1.html')




def patienthome(request):

    return render(request, 'paitents/Phome.html')



def viewrecords(request):

    return render(request, 'paitents/Patientrecords.html')











