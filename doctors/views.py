from pydoc import Doc
from sklearn.ensemble import RandomForestClassifier
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import DoctorRegistration
from .models import Doctors
from .models import Patients
#from .models import Paitens
from doctors.models import Doctors
from django.urls import reverse
from django.http import HttpResponseRedirect
#the folllowing code is used to retuen the users to login page whenever they wanna access anyother pages without first loginin in
from django.contrib.auth.decorators import login_required

from itertools import count


loginUser = ""
loginFlag = False
forgotEmpID = ""
loginName = ""
#from django.http import HttpResponse
#from django.http import Registration
#from django.http import Login
#from .models import Destination

# Create your views here.

#-------------------------------------------index/homePage---------------------------------------
def index(request):
    return render(request,'doctors/index.html')

#-------------------------------------------doc_register---------------------------------------

def doc_register(request):

    if request.method == 'POST':
       print()
       print(type(request.POST))
       print()

       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       gender = request.POST['gender']
       doc_id = request.POST['doc_id']
       dept = request.POST['dept']
       hospital = request.POST['hospital']
       email = request.POST['email']
       phone = request.POST['phone']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       print(username, password1, password2, email, first_name, last_name, doc_id, dept, hospital, phone, gender)

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
               return redirect('/doctors/doc_register')
             #  return redirect('register')

           elif User.objects.filter(email=email).exists():
                 #print('Email Already Exists')
                 messages.info(request,'Email Already Exists')
                 return redirect('/doctors/doc_register')
           else:
            print(count)
            if count == 2:
              raw_text = password1
              encrypt_text = raw_text                                             #encrypt_text
            user = Doctors(username=username, password1=password1,password2=password2, email=email, first_name=first_name, last_name=last_name,
            doc_id=doc_id, dept=dept, hospital=hospital, phone=phone, gender=gender)
            user.save();
            print(' User Created')
            messages.info(request,'User Created')
            return redirect('/doctors/login')

       else:
          #print('Passwords Not Matching')
          messages.info(request,'Passwords Not Matching')
          return redirect('/doctors/doc_register')
       return redirect('/doctors/login')


    else:
          return render(request,'doctors/reg.html')


#-------------------------------------------doctors/login---------------------------------------

def login(request):
     from .models import Doctors
     from .models import Patients
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/doctors/moduleContains')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/doctors/login')

     else:
        return render(request,'doctors/login.html')






# def login(request):
#     global loginFlag, loginUser
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         print(username, password)
#         message = ""

#         if len(Doctors.objects.filter(username=username, assword=password)) == 0:
#             message = message + "No Matching Accounts Found"
#         else:
#             pass_hash = str(Doctors.objects.filter(username=username, password=password)[0]).split(";")[4]
#             decrypt_text = pass_hash
#             if password == decrypt_text:
#                 message = message + "Welcome to the Home Page"
#                 loginFlag = True
#                 loginUser = username
#                 print(loginUser)
#                 return redirect('/doctors/moduleContains')
#             else:
#                 message = message + "Wrong Password Entered"

#         print(message)
#         context = {"message": message}
#         return render(request, 'doctors/login.html', context)

#     else:
#         return render(request, 'doctors/login.html')



#-------------------------------------------doctors/logout---------------------------------------

def logout(request):
    auth.logout(request)
    return redirect('/doctors/home')

#-------------------------------------------doctors/ModuleContains--------------------------------------
@login_required(login_url='/doctors/login/')
def moduleContains(request):
    # auth.moduleContains(request)
    return render(request,'doctors/moduleContains.html')

#-----------------------------------------------COPD---------------------------------------
@login_required(login_url='/doctors/login')
def copd(request):
    # auth.copd(request)
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()
        name = request.POST['name']
        AID = request.POST['AID']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        Weight = request.POST['Weight']
        lip = request.POST['lip']
        FEV = request.POST['FEV']
        si = request.POST['si']
        temp = request.POST['temp']
        message=''

        print( name, AID, email, age, gender, Weight, lip, FEV,si,temp)

        FEV=float(FEV)
        si=float(si)
        import pandas as pd
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split

        str = 'doctors/copd_2.xlsx'

        read = pd.read_excel(str)

        X = read.loc[0:, ['age', 'gender', 'weight', 'lipcolor', 'FEV1', 'smoking intensity', 'temperature']]
        print(X)

        Y = read.loc[0:, ['label']]

        # print(Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state = 1)

        # print(len(X_train))

        # print(len(Y_train))

        # print(len(X_test))

        # print(len(Y_test))
        name, AID, email, age, gender, Weight, lip, FEV, si, temp


        Descisiontree = DecisionTreeClassifier()
        Descisiontree.fit(X_train, Y_train.values.ravel())
        prediction2 = Descisiontree.predict(X_test)
        print('TREE algorithm ranges', accuracy_score(Y_test, prediction2) * 100)
        print('Tree Prediction', Descisiontree.predict([[age, gender, Weight, lip, FEV, si,temp]]))
        copdpred=Descisiontree.predict([[age, gender, Weight, lip, FEV, si,temp]])
        if copdpred=='severe':
            treat='1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators,bullectomy,3.lung  transplant'
        elif  copdpred=='mild':
            treat='1.quit smcoking,pulmonary rehab,2.short-acting bronchodilators '
        else:
             treat='1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators'

        descision_tree_predicted=Descisiontree.predict(X_test)
        print("Descion tree accuracy",accuracy_score(descision_tree_predicted,Y_test)*100)


        Randomforest=RandomForestClassifier(n_estimators=5)
        Randomforest.fit(X_train,Y_train)
        random_forest_predicted = Randomforest.predict(X_test)
        print("Randomforest  accuracy", accuracy_score(random_forest_predicted, Y_test) * 100)


        from sklearn.neighbors import KNeighborsClassifier

        KNN=KNeighborsClassifier()
        KNN.fit(X_train,Y_train)
        KNN_predicted=KNN.predict(X_test)
        print("KNN  accuracy", accuracy_score(KNN_predicted, Y_test) * 100)

        new_data = Patients(name=name,AID=AID,email=email,
                             age=age,
                             gender=gender, type='COPD',
                             stage=copdpred, treatement=treat
                             )
        new_data.save()

        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "mgadam2020@gmail.com"
        receiver_email = email
        password = 'ali927580000000000'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Patient Medical Report"
        message["From"] = sender_email
        message["To"] = receiver_email
        data = 'data'
        # Create the plain-text and HTML version of your message
        text = """\
        """
        html = """\
        <html>
          <body>
            <p>Hi,<br>
             <p ><span style="width" class="">Patient Name :{0}   </span></p>
        <p ><span style="width" class="">Patient AID : {1}  </span></p>
        <p ><span style="width" class="">Patient Email : {2}  </span></p>
        <p ><span style="width" class="">Patient Gender :{3}   </span></p>

        <p ><span style="width" class="">Patient Type : {4}  </span></p>
        <p ><span style="width" class="">Disease Stage :  {5} </span></p>
        <p ><span style="width" class="">Patient Treatment :{6}   </span></p>

            </p>
            <p>
          </body>
        </html>
        """.format(name,AID,email,gender,"COPD",copdpred,treat)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )


            from sklearn.metrics import confusion_matrix
            cm1 = confusion_matrix(descision_tree_predicted, Y_test)
            print(cm1)
            import seaborn as sns
            import matplotlib.pyplot as plt
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm1, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Tree_Predicted')
            plt.show()

            cm2 = confusion_matrix(random_forest_predicted, Y_test)
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm2, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Forest_Predicted')
            plt.show()



        return render(request, 'doctors/copdresults.html', {'name':name,'AID':AID
                      ,'email':email,'gender':gender,'type':'COPD',
                      'stage':copdpred,'treatement':treat})

        message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}

        return render(request, 'doctors/copd.html', context)

    return render(request, 'doctors/copd.html')

#----------------------------------------------COPD_Result---------------------------------------
@login_required(login_url='/doctors/login')
def copdresults(request):

    return render(request, 'doctors/copdresults.html')



#-------------------------------------------------------Diabetes---------------------------------------
@login_required(login_url='/doctors/login')
def diabetes(request):
    # auth.diabetes(request)
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()


        name = request.POST['name']
        AID = request.POST['AID']
        email = request.POST['email']
        gender = request.POST['gender']
        Pregnancies = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        BMI=float(BMI)
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        DiabetesPedigreeFunction=float(DiabetesPedigreeFunction)
        Age = request.POST['Age']
        message=''
        Insulin=float(Insulin)
        DiabetesPedigreeFunction=float(DiabetesPedigreeFunction)
        print( name, AID, email, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction
                 ,Age)

        import pandas as pd
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split
        message=''
        str = 'doctors/diabetes.csv'

        read = pd.read_csv(str)

        X = read.loc[0:,
            ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction',
             'Age']]
        print(X)

        Y = read.loc[0:, ['Outcome']]

        # print(Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

        # print(len(X_train))

        # print(len(Y_train))

        # print(len(X_test))

        # print(len(Y_test))

        model2 = DecisionTreeClassifier()
        model2.fit(X_train, Y_train.values.ravel())
        prediction2 = model2.predict(X_test)
        print('TREE algorithm Accuracy', accuracy_score(Y_test, prediction2) * 100)
        print('Tree Prediction', model2.predict([[  Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction
                 ,Age]]))
        prediction = model2.predict([[  Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction
                 ,Age]])
        print(prediction)


        if prediction == [0]:
            print('Moderate sugar , no need any treatement')
            treat='Moderate sugar , no need any treatement'
        elif prediction == [1]:
            print('Either oral medication or insulin should be taken accordingly')
            treat = 'Either oral medication or insulin should be taken accordingly'
        else:
            print(" couldn't able to find the stage ")

        Randomforest = RandomForestClassifier(n_estimators=5)
        Randomforest.fit(X_train, Y_train)
        random_forest_predicted = Randomforest.predict(X_test)
        print("Randomforest  accuracy", accuracy_score(random_forest_predicted, Y_test) * 100)

        from sklearn.neighbors import KNeighborsClassifier

        KNN = KNeighborsClassifier()
        KNN.fit(X_train, Y_train)
        KNN_predicted = KNN.predict(X_test)
        print("KNN  accuracy", accuracy_score(KNN_predicted, Y_test) * 100)

        new_data = Patients(name=name, AID=AID, email=email,
                            age=Age,
                            gender=gender, type='DIABETES',
                            stage=prediction, treatement=treat
                            )
        new_data.save()

        message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}

        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "mgadam2020@gmail.com"
        receiver_email = email
        password = 'ali927580000000000'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Patient Medical Report"
        message["From"] = sender_email
        message["To"] = receiver_email
        data = 'data'
        # Create the plain-text and HTML version of your message
        text = """\
                Hi,
                How are you?
                Real Python has many great tutorials:
                www.realpython.com"""
        html = """\
                <html>
                  <body>
                    <p>Hi,<br>
                     <p ><span style="width" class="">Patient Name :{0}   </span></p>
                <p ><span style="width" class="">Patient AID : {1}  </span></p>
                <p ><span style="width" class="">Patient Email : {2}  </span></p>
                <p ><span style="width" class="">Patient Age :{3}   </span></p>

                <p ><span style="width" class="">Patient Type : {4}  </span></p>
                <p ><span style="width" class="">Disease Stage :  {5} </span></p>
                <p ><span style="width" class="">Patient Treatment :{6}   </span></p>

                    </p>
                    <p>
                  </body>
                </html>
                """.format(name, AID, email, Age, "Diabetes", prediction, treat)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

            from sklearn.metrics import confusion_matrix
            cm1 = confusion_matrix(prediction2, Y_test)
            print(cm1)
            import seaborn as sns
            import matplotlib.pyplot as plt
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm1, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Tree_Predicted')
            plt.show()

            cm2 = confusion_matrix(random_forest_predicted, Y_test)
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm2, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Forest_Predicted')
            plt.show()

        return render(request, 'doctors/diabetesresults.html', {'name':name,'AID':AID
                      ,'email':email,'gender':gender,'type':'DIABETES',
                      'stage':prediction,'treatement':treat})

    return render(request, 'doctors/diabetes.html')

#------------------------------------------------Diabetes_Result---------------------------------------
@login_required(login_url='/doctors/login')
def diabetesresults(request):

    return render(request, 'doctors/diabetesresults.html')



#---------------------------------------------------------Heart---------------------------------------
@login_required(login_url='/doctors/login')
def heart(request):
    # auth.heart(request)
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()


        name = request.POST['name']
        AID = request.POST['AID']
        email = request.POST['email']
        Age = request.POST['Age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']

        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        oldpeak=float(oldpeak)
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
        print(name, AID, email, Age, sex, cp, trestbps, chol, fbs,
              restecg,thalach,exang,oldpeak,slope,ca,thal)
        import pandas as pd
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split

        str = 'doctors/heart.csv'

        read = pd.read_csv(str)

        X = read.loc[0:,
            ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca',
             'thal']]
        print(X)

        Y = read.loc[0:, ['target']]

        # print(Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

        # print(len(X_train))

        # print(len(Y_train))

        # print(len(X_test))

        # print(len(Y_test))
        message=''
        model2 = DecisionTreeClassifier()
        model2.fit(X_train, Y_train.values.ravel())
        prediction2 = model2.predict(X_test)
        print('TREE algorithm ranges', accuracy_score(Y_test, prediction2) * 100)
        print('Tree Prediction', model2.predict([[Age, sex, cp, trestbps, chol, fbs,
              restecg,thalach,exang,oldpeak,slope,ca,thal]]))
        prediction = model2.predict([[Age, sex, cp, trestbps, chol, fbs,
              restecg,thalach,exang,oldpeak,slope,ca,thal]])
        print(prediction)
        if prediction == [0]:
            print('no heart disease')
            treat='no heart disease'
        elif prediction == [1]:
            print('medications should be given accordingly')
            treat ='medications should be given accordingly'
        else:
            treat=" couldn't able to find the stage "
            print(" couldn't able to find the stage ")
#----------------------------------------
        Randomforest = RandomForestClassifier(n_estimators=5)
        Randomforest.fit(X_train, Y_train)
        random_forest_predicted = Randomforest.predict(X_test)
        print("Randomforest  accuracy", accuracy_score(random_forest_predicted, Y_test) * 100)

        from sklearn.neighbors import KNeighborsClassifier

        KNN = KNeighborsClassifier()
        KNN.fit(X_train, Y_train)
        KNN_predicted = KNN.predict(X_test)
        print("KNN  accuracy", accuracy_score(KNN_predicted, Y_test) * 100)

#---------------------------------
        new_data = Patients(name=name, AID=AID, email=email,
                            age=Age,
                            gender=sex, type='Heart',
                            stage=prediction, treatement=treat
                            )
        new_data.save()

        message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}

        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "mgadam2020@gmail.com"
        receiver_email = email
        password = 'ali927580000000000'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Patient Medical Report"
        message["From"] = sender_email
        message["To"] = receiver_email
        data = 'data'
        # Create the plain-text and HTML version of your message
        text = """\
                        Hi,
                        How are you?
                        Real Python has many great tutorials:
                        www.realpython.com"""
        html = """\
                        <html>
                          <body>
                            <p>Hi,<br>
                             <p ><span style="width" class="">Patient Name :{0}   </span></p>
                        <p ><span style="width" class="">Patient AID : {1}  </span></p>
                        <p ><span style="width" class="">Patient Email : {2}  </span></p>
                        <p ><span style="width" class="">Patient Age :{3}   </span></p>

                        <p ><span style="width" class="">Patient Type : {4}  </span></p>
                        <p ><span style="width" class="">Patient Stage :  {5} </span></p>
                        <p ><span style="width" class="">Patient Treatment :{6}   </span></p>

                            </p>
                            <p>
                          </body>
                        </html>
                        """.format(name, AID, email, Age, type, prediction, treat)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
#--------------------------------------
            # from sklearn.metrics import confusion_matrix
            # cm1 = confusion_matrix(prediction2, Y_test)
            # print(cm1)
            # import seaborn as sns
            # import matplotlib.pyplot as plt
            # plt.figure(figsize=(10, 7))
            # sns.heatmap(cm1, annot=True)
            # plt.ylabel('Truth')
            # plt.xlabel('Tree_Predicted')
            # plt.show()

            # cm2 = confusion_matrix(random_forest_predicted, Y_test)
            # plt.figure(figsize=(10, 7))
            # sns.heatmap(cm2, annot=True)
            # plt.ylabel('Truth')
            # plt.xlabel('Forest_Predicted')
            # plt.show()
#-----------------------------------------------
        return render(request, 'doctors/heartresults.html',{'name':name,'AID':AID
                      ,'email':email,'gender':sex,'type':'HEART',
                      'stage':prediction,'treatement':treat})

    return render(request, 'doctors/heart.html')


#-----------------------------------------------Heart_Result---------------------------------------
@login_required(login_url='/doctors/login')
def heartresults(request):

    return render(request, 'doctors/heartresults.html')


#-----------------------------------------------LUNG---------------------------------------
@login_required(login_url='/doctors/login')
def lung(request):
     # auth.lung(request)
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()
        name = request.POST['name']
        AID = request.POST['AID']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        Air_Pollution = request.POST['Air_Pollution']
        Alcohol_use = request.POST['Alcohol_use']
        Dust_Allergy = request.POST['Dust_Allergy']
        OccuPational_Hazards = request.POST['OccuPational_Hazards']
        Genetic_Risk = request.POST['Genetic_Risk']
        chronic_Lung_Disease = request.POST['chronic_Lung_Disease']
        Balanced_Diet = request.POST['Balanced_Diet']
        Obesity = request.POST['Obesity']
        Smoking = request.POST['Smoking']
        Passive_Smoker = request.POST['Passive_Smoker']
        Chest_Pain = request.POST['Chest_Pain']
        Coughing_of_Blood = request.POST['Coughing_of_Blood']
        Fatigue = request.POST['Fatigue']
        Weight_Loss = request.POST['Weight_Loss']
        Shortness_of_Breath = request.POST['Shortness_of_Breath']
        Wheezing = request.POST['Wheezing']
        Swallowing_Difficulty = request.POST['Swallowing_Difficulty']
        Clubbing_of_Finger_Nails = request.POST['Clubbing_of_Finger_Nails']
        Frequent_Cold = request.POST['Frequent_Cold']
        Dry_Cough = request.POST['Dry_Cough']
        Snoring = request.POST['Snoring']
        message=''

        print( name, AID, email, age, gender, Air_Pollution, Alcohol_use, Dust_Allergy, OccuPational_Hazards, Genetic_Risk, chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood, Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring)


        import pandas as pd
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split
        message=''

        str = 'doctors/lungcancer.xlsx'

        read = pd.read_excel(str)

        X = read.loc[0:,
            ['Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk',
             'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Smoking', 'Passive Smoker', 'Chest Pain', 'Coughing of Blood',
             'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails',
             'Frequent Cold', 'Dry Cough', 'Snoring']]

        print(X)

        Y = read.loc[0:, ['Level']]

        # print(Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state = 1)

        # print(len(X_train))

        # print(len(Y_train))

        # print(len(X_test))

        # print(len(Y_test))
        name, AID, email, age, gender, Air_Pollution, Alcohol_use, Dust_Allergy, OccuPational_Hazards, Genetic_Risk, chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood, Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring


        Descisiontree = DecisionTreeClassifier()
        Descisiontree.fit(X_train, Y_train.values.ravel())
        prediction2 = Descisiontree.predict(X_test)
        print('TREE algorithm ranges', accuracy_score(Y_test, prediction2) * 100)
        print('Tree Prediction', Descisiontree.predict([[ age, gender, Air_Pollution, Alcohol_use, Dust_Allergy, OccuPational_Hazards
        ,Genetic_Risk, chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood
        ,Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold
        ,Dry_Cough, Snoring ]]))
        copdpred=Descisiontree.predict([[ age, gender, Air_Pollution, Alcohol_use, Dust_Allergy, OccuPational_Hazards
        ,Genetic_Risk, chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood
        ,Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold
        ,Dry_Cough, Snoring ]])

        if copdpred=='High':
            treat='1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators,bullectomy,3.lung  transplant'
        elif  copdpred=='Low':
            treat='1.quit smcoking,pulmonary rehab,2.short-acting bronchodilators '
        else: #Medium
             treat='1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators'

        descision_tree_predicted=Descisiontree.predict(X_test)
        print("Descion tree accuracy",accuracy_score(descision_tree_predicted,Y_test)*100)


        Randomforest=RandomForestClassifier(n_estimators=5)
        Randomforest.fit(X_train,Y_train)
        random_forest_predicted = Randomforest.predict(X_test)
        print("Randomforest  accuracy", accuracy_score(random_forest_predicted, Y_test) * 100)


        from sklearn.neighbors import KNeighborsClassifier

        KNN=KNeighborsClassifier()
        KNN.fit(X_train,Y_train)
        KNN_predicted=KNN.predict(X_test)
        print("KNN  accuracy", accuracy_score(KNN_predicted, Y_test) * 100)

        new_data = Patients(name=name,AID=AID,email=email,
                             age=age,
                             gender=gender, type='LUNG Cancer',
                             stage=copdpred, treatement=treat
                             )
        new_data.save()

        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "mgadam2020@gmail.com"
        receiver_email = email
        password = 'ali927580000000000'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Patient Medical Report"
        message["From"] = sender_email
        message["To"] = receiver_email
        data = 'data'
        # Create the plain-text and HTML version of your message
        text = """\
        """
        html = """\
        <html>
          <body>
            <p>Hi,<br>
             <p ><span style="width" class="">Patient Name :{0}   </span></p>
        <p ><span style="width" class="">Patient AID : {1}  </span></p>
        <p ><span style="width" class="">Patient Email : {2}  </span></p>
        <p ><span style="width" class="">Patient Gender :{3}   </span></p>

        <p ><span style="width" class="">Patient Type : {4}  </span></p>
        <p ><span style="width" class="">Disease Stage :  {5} </span></p>
        <p ><b><span style="width" class="">Patient Treatment :{6}  </span></b></p>

            </p>
            <p>
          </body>
        </html>
        """.format(name,AID,email,gender,"LUNG Cancer",copdpred,treat)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

            from sklearn.metrics import confusion_matrix
            cm1 = confusion_matrix(descision_tree_predicted, Y_test)
            print(cm1)
            import seaborn as sns
            import matplotlib.pyplot as plt
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm1, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Tree_Predicted')
            plt.show()

            cm2 = confusion_matrix(random_forest_predicted, Y_test)
            plt.figure(figsize=(7, 5))
            sns.heatmap(cm2, annot=True)
            plt.ylabel('Truth')
            plt.xlabel('Forest_Predicted')
            plt.show()



        return render(request, 'doctors/lungresults.html', {'name':name,'AID':AID
                      ,'email':email,'gender':gender,'type':'LUNG Cancer',
                      'stage':copdpred,'treatement':treat})

        message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}

        return render(request, 'doctors/lung.html', context)

    return render(request,'doctors/lung.html')

#------------------------------------------------------------Lung_Result--------------------------
@login_required(login_url='/doctors/login')
def lungresults(request):

    return render(request, 'doctors/lungresults.html')


#-----------------------------------------------------------account-updation----------------------
@login_required(login_url='/doctors/login')
def accountUpdate(request):
    global loginUser,loginName
    message = ""
    print("Login Flag:",loginFlag)
    if loginFlag == False:
        return redirect('login')

    loginObj = str(Doctors.objects.filter(doc_id=loginUser)[0]).split(";")

    if request.method == 'POST':
        dept = request.POST['dept']
        contact = request.POST['contact']
        email = request.POST['email']
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        confnewpass = request.POST['confnewpass']

        if oldpass == "" or newpass == "" or confnewpass == "":
            Doc(doc_id=loginUser,name=loginObj[1],password=loginObj[4],dept=dept,phone=contact,
             email=email,gender=loginObj[2]).save()
            message = message + "Account Updated Successfully.\n"
        else:
            oldpassDB = loginObj[4]
            if oldpass == oldpassDB:
                if newpass == confnewpass:
                    if len(newpass)>6:
                        flag1,flag2,flag3 = 0,0,0
                        for i in range(len(newpass)):
                            ele = ord(newpass[i])
                            if ele>96 and ele<123:
                                flag1 = 1
                            elif ele>47 and ele<58:
                                flag2 = 1
                            elif ele>64 and ele<91:
                                flag3 = 1
                        if flag1 == 1 and flag2 == 1 and flag3 == 1:
                            encrpytPass = newpass
                            Doctors(doc_id=loginUser,name=loginObj[1],password=encrpytPass,dept=dept,phone=contact,
                            email=email,gender=loginObj[2]).save()
                            message = message + "Account Updated Successfully.\n"
                        else:
                            message = message +"Re-enter The Password. Does'nt Follow Password Constraints.\n"
                    else:
                        message = message + "Password Length is less than 7 Characters."
                else:
                    message = message + "New Passwords Does Not Match."
            else:
                message = message + "Old Password Does Not Match."

        loginObj = str(Doctors.objects.filter(doc_id=loginUser)[0]).split(";")

        context = {"empID":loginObj[0],"name":loginObj[1],"dept":loginObj[5],"contact":loginObj[6],"gender":loginObj[2],"email":loginObj[3],"message":message}
        return render(request,'doctors/accountUpdate.html',context)
    else:
        # GET METHOD
        context = {"empID":loginObj[0],"name":loginObj[1],"dept":loginObj[5],"contact":loginObj[6],"gender":loginObj[2],"email":loginObj[3]}
        return render(request,'doctors/accountUpdate.html',context)
