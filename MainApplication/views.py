from os import startfile
from django.shortcuts import render, redirect

import pyrebase


cofig =  {
  "apiKey": "AIzaSyBmnhaFGTVelDMkPQ3pjvdPMQc28c-JrTs",
  "authDomain": "simplicityictorg.firebaseapp.com",
  "databaseURL": "https://simplicityictorg-default-rtdb.firebaseio.com",
  "projectId": "simplicityictorg",
  "storageBucket": "simplicityictorg.appspot.com",
  "messagingSenderId": "293438070731",
  "appId": "1:293438070731:web:7ad82694864d02ed2ca04e",
  "measurementId": "G-LDE2RYMN2X"
}



firebase = pyrebase.initialize_app(cofig)

database = firebase.database()

auth_ = firebase.auth()









def HomePage(request):
    return render(request,'MainApplication/public/Home.html' )



def PublicAboutUs(request):
    return render(request,'MainApplication/public/AboutUs.html' )



def PublicContactUs(request):
    return render(request,'MainApplication/public/ContactUs.html' )




def Login(request):
    """
    guest_Email
    guest_password
    UserName_staff
    password_staff
    remberme
    """
    print(request.POST)
    if request.method == "POST":
        datas = request.POST
        if datas["CHECKER"] == "home":

            email = datas["guest_Email"]
            password = datas["guest_password"]
            userId = auth_.sign_in_with_email_and_password(email,password)
            request.session["UserTokenId"] = str(userId['idToken'])
            return redirect('dashboard')

        elif datas["CHECKER"] == "away":
            emailOrUserName = datas["UserName_staff"]
            password = datas["password_staff"]
            userId = auth_.sign_in_with_email_and_password(emailOrUserName,password)
            print(userId)
            request.session["UserTokenId"] = str(userId)
            return redirect('dashboard')

            

    
    
    
    
    return render(request,'MainApplication/LogIn.html')




def SignUp(request):

    datas = request.POST

    
    """
     First_Name
     Last_Name
     Password_One
     Password_Two
     gender
     Email
     Phone_Number
     Security_Questions
     Security_Answers

     Full_Name


     Full_Name_company
     Company_Name
     Company_Email
     Phone_Number_Company
     Password_One_company
     Password_Two_company
     Adress
     Company_Type
    """

    if request.method == "POST":
        dbQuery = database.child("User").child("Customer")
        email= ""
        password1 = ""
        password2 = ""
        detail = None
        if datas.get('CHECKER') == "away":
            fullName = datas.get('Full_Name_company')
            companyName =  datas.get('Company_Name')
            companyEmail = datas.get('Company_Email')
            companyPhoneNumber =  datas.get('Phone_Number_Company')
            passwordOne = datas.get('Password_One_company')
            passwordTwo = datas.get('Password_Two_company')
            

            companyAdress =  datas.get('Adress')
            companyType = datas.get('Company_Type')

            dbQuery.child("Company")
            
            password1 = passwordOne
            password2 = passwordTwo
            email = companyEmail

            detail = {"fullName": fullName, "companyName":companyName, "companyEmail":companyEmail,
            "companyPhoneNumber":companyPhoneNumber ,"companyAdress":companyAdress,"companyType":companyType }

        elif datas.get('CHECKER') == "home":
            fullName = datas.get('First_Name')+" "+ datas.get('Last_Name')
            email = datas.get('Email')
            passwordOne = datas.get('Password_One') 
            passwordTwo = datas.get('Password_Two')
            gender = datas.get('gender')
            phoneNumber = datas.get('Phone_Number')
            securityDetail = {datas.get('Security_Questions') :  datas.get('Security_Answers')}
            dbQuery.child("Individual")
            
            password1 = passwordOne
            password2 = passwordTwo

            detail = {"fullName":fullName, "email":email,"gender":gender ,"phoneNumber":phoneNumber ,"securityDetail":securityDetail}
        
        
        if password1 == password2:
            
            try:
                user = auth_.create_user_with_email_and_password(email, password2)
                uid = user['localId']
                dbQuery.child(str(uid)).set({"Detail":detail, "Status" :"1"})
                return redirect('login')
            except Exception as e:
                import ast 

                errorMessage =str( e )
                starting = errorMessage.find('{')
                errorMessage = errorMessage[starting:]

                
                try:
                    dictionary = ast.literal_eval(errorMessage)
                    errorMessage = dictionary['error']['message']
                    code = dictionary['error']['code']

                    if int(code) == 400:
                        if errorMessage == 'EMAIL_EXISTS':
                            pass
                        elif errorMessage == 'WEAK_PASSWORD : Password should be at least 6 characters':
                            pass


                    print(errorMessage)
                except Exception as er:
                     print("################ it means another error  ############")
                     print(er)

            
        
            # 
    return render(request, 'MainApplication/SignUp.html')



def dashBoard(request):
    
    userSession = request.session['UserTokenId']
   
    session_Information = auth_.get_account_info(userSession)
    localId = session_Information['users'][0]['localId']
    
    companyRef =dict(database.child('User').child('Customer').child('Company').get().val())
    IndividualRef =dict( database.child('User').child('Customer').child('Individual').get().val())
    
    companyRef = companyRef.keys()
    IndividualRef = IndividualRef.keys()

    if localId in companyRef:
        companyRef = dict(database.child('User').child('Customer').child('Company').child(str(localId)).get().val())
        fullName = companyRef['Detail']['companyName'] 
        email = companyRef['Detail']['companyEmail'] 


        """
        companyAdress:
        companyEmail
        companyName
        companyPhoneNumber
        companyType
        fullName
        """

    elif localId in IndividualRef:
        IndividualRef = dict(database.child('User').child('Customer').child('Individual').child(str(localId)).get().val())
        fullName = IndividualRef['Detail']['fullName'] 
        email = IndividualRef['Detail']['email'] 


    
    import datetime
    currentTime = datetime.datetime.now()

    if currentTime.hour < 12:
         print('Good morning.')
    elif 12 <= currentTime.hour < 18:
        print('Good afternoon.')
    else:
        print('Good evening.')
        

        
        
    

    
    
    return render(request,'MainApplication/public/DashBoardCustomer.html')




# https://stackoverflow.com/questions/69217118/getting-specific-errors-type-message-from-httperror-while-working-django-fireba
