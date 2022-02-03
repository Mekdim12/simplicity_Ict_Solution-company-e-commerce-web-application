
from datetime import time
from os import startfile

from django.shortcuts import render, redirect
from django.urls import conf
from pyasn1_modules.rfc2459 import CommonName

import pyrebase

import firebase_admin.messaging
from firebase_admin import credentials
from firebase_admin import db






cofig = {

    "apiKey": "AIzaSyBmnhaFGTVelDMkPQ3pjvdPMQc28c-JrTs",
    "authDomain": "simplicityictorg.firebaseapp.com",
    "databaseURL": "https://simplicityictorg-default-rtdb.firebaseio.com",
    "projectId": "simplicityictorg",
    "storageBucket": "simplicityictorg.appspot.com",
    "messagingSenderId": "293438070731",
    "appId": "1:293438070731:web:7ad82694864d02ed2ca04e",
    "measurementId": "G-LDE2RYMN2X"
}



cred = credentials.Certificate({

    
  "type": "service_account",
  "project_id": "simplicityictorg",
  "private_key_id": "f7b1421c8fc71652b4d0e515b9c0284d25b919f8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCyk+CUB5F7UoX6\nEjQHctnPFncDFiJnxZjQKOE+5STVuBhBadEtvRxurhVaeYd1mo3iob1p8iClWmuv\nDc44SmFfRUO165IemPAPNfyPXacpptpC6Sd4k9htJ20Nzik6+dBT5cFRDjlXpaDe\nzM0+CbpCwr704HGVYqGrh35IVmZufG7YpbwmIVGZd0+YASB9KD4Esd8u1QVz+fj1\n/CDcgHwV84Q3MXEkfEE74z8N6NXlsAIjSDOGxNOWBnsKqIf8xRsppBtS0ko/CSv9\n+3S56y/HR24vAWwjR7KhNYcYKVynAQ8Jc+tkxgO++AvTp10MqofqEJaaHjQt+WVF\nPExEnCrRAgMBAAECggEAB8P/XPKWDo/GcpssautBOmSgwugpUXvN1xYDAw0cCKT1\nfZE6Yue9kvjUJgPBSrGAlGuaCP+Z8LTdmE6Ecm1WHgptHQ3wJA9cp52udKXTA1A9\nnzGkSTWdMJR5hSNbJsTWrNJRwXqJzvRdejjb30P1Jwpw20VgHRndm8/j44WJ1Wm2\nRoOShecpXT0vaJNUf1RlAU3ujRclldvBcmkwVlV4o7ZQHaPUcZa2fiX1ELpfs61x\n4JNipJCIPqDbsGqYNxVSxLuvhyfQma7NgqHGiU3H8H4ruHdjQf54uXlyrxdj2Wtu\nsqDk01qDEAbRTTu5uWsgmVQoQbqT0unL0gh03fAqwQKBgQDtGRmt+cfWGyIdW6vO\n8/ZrbGsv0I7stJy6TLWt3O2wbkdjtqN2Xh6GC0HLy8Dw8ogCmQoVIDv/oWdGYshO\ncKgCIRE7m6ii94aL5Z6a73W7pUFoq58NylGAhD7nLnqAcILHZyb98n4UZxg0JYlj\nq7B5mPEJCool5cdufxxvo0QfkQKBgQDA0HFKEqo/AoZireXCNX3aahDnNGWZSH+r\n4vWvISnNS2+fLbvbSWizFwja5V7YraPJFLE5GbBitvxtp3OoWWXDkGgjTq+lYcgw\nnXW+4uQkmzCKdJTKp73N6p9grVGO5/n3TReAb8CbiYlpPr2whD3M55fm0FGhRGIz\nyA8VoQg3QQKBgAz0iyerd1TmpKWQBcJIKFXUVcMGFVkvwUSYvnCimsZCMFptd18X\nY3mVkeHN31wLFI13yUpAOacNLbR131YR58w9/FASgFNvTQXF5TW4EenP7NQIVKeP\nP4bTMxC0xHLSMwMsSsAjiOoafAMVbf1pOzpZtgn1bnkFpjEOdwJOnIFRAoGAEggs\nYCIIu+XPjZD3yMbZ40BCHm0/ByvJjNin4131m9ZvNPLA+8wMt5ry4A3NZfQvOhHu\nVQm6/jBgwRyE63yY0MZDhvHH6W6Qm0NOjLCJZ4b/7iLi+2TeklBb4V20H+o/7UnP\nZdqNp74gFLCiasyjPvN1uEdJKwzLJk6SYpJxw0ECgYAqsoYXNcKGoHArWqPagaM5\nb863WFZWQfOgpoNmvS8FHWHY7BpxtNBmG6OwId5RBtjyYVu9AaZUHPR2UEdXxJDd\n85yLJdveItihd4w+7/AQ7/xZ16VPwaMmv+fEeIZ/8OIS3qSXNB2kQZW6mIb39jco\n9JqyqtplWp4kv73WTU0q9w==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-wvp9y@simplicityictorg.iam.gserviceaccount.com",
  "client_id": "103227847160919157530",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wvp9y%40simplicityictorg.iam.gserviceaccount.com"



})

firebase_admin.initialize_app( cred, cofig)










firebase = pyrebase.initialize_app(cofig)

database = firebase.database()

auth_ = firebase.auth()


def HomePage(request):
    context = {}
    ct = {}
    try:
        ref = db.reference('PageInforamtion')
        for timestamp in ref.get():
            data = ref.get()[timestamp]
            Description = data['Description']
            companyname = data['companyname']

            temp = {
                "companyname":companyname,
                "Description":Description,
            }

            ct[timestamp] = temp
            temp = {}
        context['data'] = ct
    except Exception as rr:
        print(rr)
        print("#################################### 111")
    
    return render(request, 'MainApplication/public/Home.html', context)


def PublicAboutUs(request):
    return render(request, 'MainApplication/public/AboutUs.html')


def PublicContactUs(request):
    context= {}
    context ['flag'] = "0"
    
    if request.method == 'POST':
        
        data = dict(request.POST)

        name = data['name'][0]
       
        

        comment = data['comment'][0]

        if name.strip() == "" and comment.strip() == "":
            context = {"flag":"3"}
        elif name.strip() == "":
            context = {"flag":"1"}
        elif comment.strip() == "":
            context = {"flag":"2"}
        else:
            import datetime
            month = int( datetime.datetime.now().strftime('%m'))
            
            try:
                ref = db.reference('CommentOrFeedBack').child(str(month))
                import datetime
                dt = datetime.datetime.now().strftime('%d-%B-%Y')
                temp = {
                    'name':name,
                    'comment':comment,
                    'createdOn':dt
                }
                
                ref.push(temp)
                
                return redirect('PublicContactUs')

            except Exception as er:
                print(er)
                print("############ 753")
       
    return render(request, 'MainApplication/public/ContactUs.html', context)


def Login(request):
    
    """
    guest_Email
    guest_password
    UserName_staff
    password_staff
    remberme
    """
    context = {}
    context["error"] = "0"
    

    if request.method == "POST":
        datas = request.POST
        if datas["CHECKER"] == "home":

            email = datas["guest_Email"]
            password = datas["guest_password"]
            try:
                temp = []
                userId = auth_.sign_in_with_email_and_password(email, password)

                ref =list(  db.reference('User').child('Customer').get())
                for keys in ref:
                    
                    ref2 =   db.reference('User').child('Customer').get()[keys] ['Detail']
                    ref2 = ref2.get('email')
                    temp.append(ref2)
                    
                    
                    
                if email.strip() in temp:
                    request.session["UserTokenId"] = str(userId['idToken'])
                    return redirect('dashboard')
                else:
                    context['error'] = "2"
                    
                
               
                
                
                
            except Exception as e:

                import ast
                

                errorMessage = str(e)
                starting = errorMessage.find('{')
                errorMessage = errorMessage[starting:]
                # print(errorMessage)
                try:
                    dictionary = ast.literal_eval(errorMessage)
                    errorMessage = dictionary['error']['message']
                    code = dictionary['error']['code']
                    
                    

                    if int(code) == 400:
                        
                        if errorMessage == "MISSING_PASSWORD":
                            context['error'] = "1"
                        elif errorMessage == "INVALID_EMAIL":
                            context['error'] = "2"
                        elif errorMessage == "INVALID_PASSWORD":
                            context["error"] = "4"
                        elif errorMessage == "EMAIL_NOT_FOUND":
                            context["error"] = "5"
                        elif errorMessage == "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":
                            context['error'] = "3"
                    
                except Exception as er:
                    print("################ it means another error  ############ another one :)")
                    print(er)


            



            

        elif datas["CHECKER"] == "away":
            emailOrUserName = datas["UserName_staff"]
            password = datas["password_staff"]

            try:
                userId = auth_.sign_in_with_email_and_password(
                    emailOrUserName, password)
                temp = []
                ref =list(  db.reference('User').child('Company').get())
                for keys in ref:
                    
                    ref2 =   db.reference('User').child('Company').get()[keys] ['Detail']
                    print(ref2)
                    ref2 = ref2.get('companyEmail')
                    temp.append(ref2)
                    
                    
                    
                if emailOrUserName.strip() in temp:
                    request.session["UserTokenId"] = str(userId['idToken'])
                    return redirect('dashboardstaff')
                else:
                    context['error'] = "2"


            except Exception as e:
                import ast

                errorMessage = str(e)
                starting = errorMessage.find('{')
                errorMessage = errorMessage[starting:]
                

                try:
                    dictionary = ast.literal_eval(errorMessage)
                    errorMessage = dictionary['error']['message']
                    code = dictionary['error']['code']
                    
                    

                    if int(code) == 400:
                        
                        if errorMessage == "MISSING_PASSWORD":
                            context['error'] = "1"
                        elif errorMessage == "INVALID_EMAIL":
                            context['error'] = "2"
                        elif errorMessage == "INVALID_PASSWORD":
                            context["error"] = "4"
                        elif errorMessage == "EMAIL_NOT_FOUND":
                            context["error"] = "5"
                        elif errorMessage == "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":
                            context['error'] = "3"
                    
                except Exception as er:
                    print("################ it means another error  ############ another one :)")
                    print(er)
    return render(request, 'MainApplication/LogIn.html', context)


def SignUp(request):
    context = {}
    context ["error"] = "0" 
   

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
        datas = request.POST
        # dbQuery = database.child("User").child("Customer")
        dbQuery = db.reference("User").child("Company")
        dbQuery2 = db.reference('User').child("Customer")

        email = ""
        password1 = ""
        password2 = ""
        detail = None
        if datas.get('CHECKER') == "away":
            fullName = datas.get('Full_Name_company')
            companyName = datas.get('Company_Name')
            companyEmail = datas.get('Company_Email')
            companyPhoneNumber = datas.get('Phone_Number_Company')
            passwordOne = datas.get('Password_One_company')
            passwordTwo = datas.get('Password_Two_company')

            companyAdress = datas.get('Adress')
            companyType = datas.get('Company_Type')

            dbQuery.child("Company")

            password1 = passwordOne
            password2 = passwordTwo
            
            email = companyEmail

            
            
            if password1.strip() != password2.strip():
                context = {"error": "1"}
            elif fullName.strip() == "":
                context = {"error": "2"}
            elif email.strip() == "":
                context = {"error": "3"}
            elif companyName.strip() == "":
                context = {"error": "4"}
            elif companyPhoneNumber.strip() == "":
                context = {"error": "5"}


            

            detail = {"fullName": fullName, "companyName": companyName, "companyEmail": companyEmail,
                      "companyPhoneNumber": companyPhoneNumber, "companyAdress": companyAdress, "companyType": companyType}

        elif datas.get('CHECKER') == "home":
            fullName = datas.get('First_Name')+" " + datas.get('Last_Name')
            email = datas.get('Email')
            passwordOne = datas.get('Password_One')
            passwordTwo = datas.get('Password_Two')
            gender = datas.get('gender')
            phoneNumber = datas.get('Phone_Number')
            securityDetail = {
                datas.get('Security_Questions'):  datas.get('Security_Answers')}
            dbQuery.child("Individual")

            password1 = passwordOne
            password2 = passwordTwo

            if password1.strip() != password2.strip():
                context = {"error": "7"}
            elif fullName.strip() == "":
                context = {"error": "8"}
            elif email.strip() == "":
                context = {"error": "9"}
            elif phoneNumber.strip() == "":
                context = {"error": "6"}

            detail = {"fullName": fullName, "email": email, "gender": gender,
                      "phoneNumber": phoneNumber, "securityDetail": securityDetail}

        if password1 == password2:

            try:
                user = auth_.create_user_with_email_and_password(
                    email, password2)
                uid = user['localId']
                if  datas.get('CHECKER') == "home":

                    dbQuery2.child(str(uid)).set({"Detail": detail, "Status": "1"})
                               
                elif datas.get('CHECKER') == "away":
                    
                    dbQuery.child(str(uid)).set({"Detail": detail, "Status": "1"})
                
                return redirect('login')
            except Exception as e:
                import ast

                errorMessage = str(e)
                starting = errorMessage.find('{')
                errorMessage = errorMessage[starting:]
                print(" --------------")
                print(errorMessage)
                print("* ********* * *** ")
                try:
                    dictionary = ast.literal_eval(errorMessage)
                    errorMessage = dictionary['error']['message']
                    code = dictionary['error']['code']

                    if int(code) == 400:
                        
                        if errorMessage == 'EMAIL_EXISTS':
                            
                            if  datas.get('CHECKER') == "home":
                                context = { 'error': "9"}
                            elif datas.get('CHECKER') == "away":
                                context = {'error' : "3" }
                        elif errorMessage == 'WEAK_PASSWORD : Password should be at least 6 characters':
                            if  datas.get('CHECKER') == "home":
                                context = {'error': "7"}
                            elif datas.get('CHECKER') == "away":
                                context = { 'error' : "1"}
                        if errorMessage == "MISSING_PASSWORD":
                            if  datas.get('CHECKER') == "home":
                                context = {'error': "7"}
                            elif datas.get('CHECKER') == "away":
                                context = {'error' : "1"}

                        elif errorMessage == "INVALID_EMAIL":
                            if  datas.get('CHECKER') == "home":
                                context = { 'error': "9"}
                            elif datas.get('CHECKER') == "away":
                                context = {'error' : "3" }
                        elif errorMessage == "INVALID_PASSWORD":
                            if  datas.get('CHECKER') == "home":
                                context = {'error': "7"}
                            elif datas.get('CHECKER') == "away":
                                context = { 'error' : "1"}
                
                    
                except Exception as er:
                    print("################ it means another error  ############ buffalo")
                    print(er)
        else:
            context = {"error": "1"}
        # the two password are not the same 
    print(context)
    return render(request, 'MainApplication/SignUp.html', context)


def dashBoard(request):

    context = {}
    userSession = request.session['UserTokenId']

   

    session_Information = auth_.get_account_info(userSession)
    
    localId = session_Information['users'][0]['localId']




    # companyRef = dict(database.child('User').child(
    #     'Customer').child('Company').get().val())
    IndividualRef = db.reference('User').child("Customer").get()
    
    # IndividualRef = dict(database.child('User').child(
    #     'Customer').child('Individual').get().val('Customer'))
    companyRef = db.reference('User').child('Company').get()

    




    
    companyRef = companyRef.keys()
    IndividualRef = IndividualRef.keys()

    

    if localId in companyRef:
        
        # companyRef = dict(database.child('User').child(
        #     'Customer').child('Company').child(str(localId)).get().val())
        companyRef = db.reference('User').child("Company").child(str(localId)).get()
      
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
        
        # IndividualRef = dict(database.child('User').child(
        #     'Customer').child('Individual').child(str(localId)).get().val())


        IndividualRef = db.reference('User').child('Customer').child(str(localId)).get() 

        fullName = IndividualRef['Detail']['fullName']
        email = IndividualRef['Detail']['email']
        

    import datetime
    currentTime = datetime.datetime.now()

    if currentTime.hour < 12:
        greetingMessage = 'Good morning.'
    elif 12 <= currentTime.hour < 18:
        greetingMessage = 'Good afternoon.'
    else:
        greetingMessage = 'Good evening.'

    context = {"name": fullName, "greeting": greetingMessage}

    at =  email.find('.')
    email = email[:at] + '' + email[at+1:]
    at =  email.find('@')
    email = email[:at] + '-AT-' + email[at+1:]

    try:
        
        # ref = db.reference('MarketActivity').child(email).child('Purchased') # checking if he every buys sth 
        ref = db.reference('MarketActivity').child(email)
        # before that check whether that its status if its acceppeted by the staff set it sth different
        acceptedlist = []
        try:
            referenc = (db.reference('PendingActivity').child(email).get().values())
            acceptedlist = referenc
             
        except:
            pass

        
        if ref.get() is not None or ref.get() != {}:
            tempOne = {}
            try:
                prod = ref.child('Products')
                
                for times in prod.get():
                    
                    data = prod.get()[times]
                    # ProductTimestamp = data['ProductTimestamp']
                    ProductTimestamp = data['timestampid']
                    
                    product = db.reference('Products').child(ProductTimestamp.strip()).get()

                    prodcutname= product['prodcutname']
                    createdOn= product['createdOn']
                    status = ""

                    if times in acceptedlist:
                        status = "Delivered"
                    else:
                        status = "Pending"

                    tempOne[times] = {
                        "prodcutname":prodcutname,
                        "createdOn":createdOn,
                        "status":status
                    }

                    
            except:
                pass
            tempTwo = {}
            try:
                serv = ref.child('Services')
                for times in serv.get():
                    data = serv.get()[times]
                    # ProductTimestamp = data['ProductTimestampid']
                    ProductTimestamp = data['timestampid']

                    service = db.reference('Services').child(ProductTimestamp.strip()).get()
                    servicename = service['servicename']
                    createdOn= service['createdOn']

                    status = ""
                    if times in acceptedlist:
                        status = "Delivered"
                    else:
                        status = "Pending"

                    tempTwo[times] = {
                        "servicename":servicename,
                        "createdOn":createdOn,
                        "status":status
                            }
            except:
                pass


            context['products'] = tempOne
            context['services'] = tempTwo

            numberProdcuts = len(tempOne.keys())
            numberServices = len(tempTwo.keys())
            context['prod'] = numberProdcuts
            context['serv'] = numberServices
        else:
            pass

        
    except Exception as df:
        print(df)
        print("################################## 136")



    try: # trying to get the service that is already provided to cusstomer and getting feedback on them
        referList =  list ( (db.reference('PendingActivity').child(email).get()).values()) 
        
        items = db.reference('MarketActivity').child(email).child('Purchased')
        temp = {}
        try:
            prodc = items.child('Products')
            
            for ts in referList:
                
                tmp = prodc.child(ts)
                if not tmp.get() == None:
                    newref = db.reference('Products').child(tmp.get()['ProductTimestamp'].strip()).get()        
                    name = newref['prodcutname']
                    date = tmp.get()['date']
                    temp[ts] = {
                        "name":name,
                        "date":date 
                    }

                    
        except:
            pass
        
        try:
            servi = items.child('Services')

            for ts in referList:
                tmp = servi.child(ts)
                if not tmp.get() == None:
                    newref = db.reference('Services').child(tmp.get()['ProductTimestamp'].strip()).get()
                    name = newref['servicename']
                    date = tmp.get()['date']

                    temp[ts] = {
                        "name":name,
                        "date":date 
                    }
                

        except:
            pass

          
        context['forrating'] = temp
        
        accepted = len(temp.keys())
        context['accept'] = accepted

    except Exception as r:
        print(r)
        print("##########################################  1498")
    # print(context)

    return render(request, 'MainApplication/public/DashBoardCustomer.html', context)









def reUsableForShopFunctions( request , context):
     
    userSession = request.session['UserTokenId']

   

    session_Information = auth_.get_account_info(userSession)
    
    localId = session_Information['users'][0]['localId']


    IndividualRef = db.reference('User').child("Customer").get()
    
   
    companyRef = db.reference('User').child('Company').get()

    companyRef = companyRef.keys()
    IndividualRef = IndividualRef.keys()

    

    if localId in companyRef:
        companyRef = db.reference('User').child("Company").child(str(localId)).get()
        fullName = companyRef['Detail']['companyName']
        email = companyRef['Detail']['companyEmail']

    elif localId in IndividualRef:
        IndividualRef = db.reference('User').child('Customer').child(str(localId)).get() 
        fullName = IndividualRef['Detail']['fullName']
        email = IndividualRef['Detail']['email']
        

    import datetime
    currentTime = datetime.datetime.now()

    if currentTime.hour < 12:
        greetingMessage = 'Good morning.'
    elif 12 <= currentTime.hour < 18:
        greetingMessage = 'Good afternoon.'
    else:
        greetingMessage = 'Good evening.'

    context ["name"] = fullName
    context ["greeting"] = greetingMessage


    try: # this for product handling 
        dbref = db.reference('Products')
        
        values = []
        for timestamapids in dbref.get():
            temp = {}
            data = dbref.get()[timestamapids]

            Description = data['Description']
            PriceType = data['PriceType']
            price = data['price']
            prodcutType = data['prodcutType']
            prodcutname = data['prodcutname']
            rating = str(data['rating'])
            shippementDays = data['shippementDays']
            createdOn = data['createdOn']

            if rating == '1':
                rating = '⭐'
            elif rating == '2':
                rating = '⭐⭐'
            elif rating == '3':
                rating = '⭐⭐⭐'
            elif rating == '4':
                rating = '⭐⭐⭐⭐'
            elif rating == '5':
                rating = '⭐⭐⭐⭐⭐'
            


            temp = {
                'prodcutname' : prodcutname,
                'prodcutType':prodcutType,
                'price' : price,
                'PriceType':PriceType,
                'createdOn':createdOn,
                'Description':Description,
                'shippementDays':shippementDays,
                'rating':rating,
            }
            values.append(temp)
            temp = {}
            
        keys = list(dbref.get().keys())
        
        availlabelProduct = dict(zip(keys, values))
        context['availlabelProduct'] = availlabelProduct
        context['flag'] = False
        
    except Exception as er:
        print(er)
        print("############################## 013")

    try: # this for service handling 
        dbref = db.reference('Services')
        
        values = []
        for timestamp in dbref.get():
            temp= {}
            data = dbref.get()[timestamp]

            Description = data['Description']
            PriceType = data['PriceType']
            createdOn = data['createdOn']
            price = data['price']
            rating = data['rating']
            serviceType = data['serviceType']
            servicename = data['servicename']
           
            
            if rating == '1':
                rating = '⭐'
            elif rating == '2':
                
                rating = '⭐⭐'
            elif rating == '3':
                rating = '⭐⭐⭐'
            elif rating == '4':
                rating = '⭐⭐⭐⭐'
            elif rating == '5':
                rating = '⭐⭐⭐⭐⭐'



            temp = {

                'Description':Description,
                'PriceType':PriceType,
                'createdOn':createdOn,
                'price':price,
                'rating':rating,
                'serviceType':serviceType,
                'servicename':servicename
            }
            values.append(temp)
            temp = {}
        keys = list(dbref.get().keys())
        
        availabelServices = dict(zip(keys, values))
        context['availabelServices'] = availabelServices

    except Exception as e:
        print(e)
        print("######################## 051")

    return context



def Shop(request):
    context = {}
    context['flag'] = False


   
    userSession = request.session['UserTokenId']

   

    session_Information = auth_.get_account_info(userSession)
    
    localId = session_Information['users'][0]['localId']




    # companyRef = dict(database.child('User').child(
    #     'Customer').child('Company').get().val())
    IndividualRef = db.reference('User').child("Customer").get()
    
    # IndividualRef = dict(database.child('User').child(
    #     'Customer').child('Individual').get().val('Customer'))
    companyRef = db.reference('User').child('Company').get()

    




    
    companyRef = companyRef.keys()
    IndividualRef = IndividualRef.keys()

    

    if localId in companyRef:
        
        # companyRef = dict(database.child('User').child(
        #     'Customer').child('Company').child(str(localId)).get().val())
        companyRef = db.reference('User').child("Company").child(str(localId)).get()
      
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
        
        # IndividualRef = dict(database.child('User').child(
        #     'Customer').child('Individual').child(str(localId)).get().val())


        IndividualRef = db.reference('User').child('Customer').child(str(localId)).get() 

        fullName = IndividualRef['Detail']['fullName']
        email = IndividualRef['Detail']['email']
        

    import datetime
    currentTime = datetime.datetime.now()

    if currentTime.hour < 12:
        greetingMessage = 'Good morning.'
    elif 12 <= currentTime.hour < 18:
        greetingMessage = 'Good afternoon.'
    else:
        greetingMessage = 'Good evening.'

    # context = {"name": fullName, "greeting": greetingMessage}

    at =  email.find('.')
    email = email[:at] + '' + email[at+1:]
    at =  email.find('@')
    email = email[:at] + '-AT-' + email[at+1:]

    try:
        
        # ref = db.reference('MarketActivity').child(email).child('Purchased') # checking if he every buys sth 
        ref = db.reference('MarketActivity').child(email)
        # before that check whether that its status if its acceppeted by the staff set it sth different
        acceptedlist = []
        try:
            referenc = (db.reference('PendingActivity').child(email).get().values())
            acceptedlist = referenc
             
        except:
            pass

        
        if ref.get() is not None or ref.get() != {}:
            tempOne = {}
            try:
                prod = ref.child('Products')
                
                for times in prod.get():
                    
                    data = prod.get()[times]
                    # ProductTimestamp = data['ProductTimestamp']
                    ProductTimestamp = data['timestampid']
                    
                    product = db.reference('Products').child(ProductTimestamp.strip()).get()

                    prodcutname= product['prodcutname']
                    createdOn= product['createdOn']
                    status = ""

                    if times in acceptedlist:
                        status = "Delivered"
                    else:
                        status = "Pending"

                    tempOne[times] = {
                        "prodcutname":prodcutname,
                        "createdOn":createdOn,
                        "status":status
                    }

                    
            except:
                pass
            tempTwo = {}
            try:
                serv = ref.child('Services')
                for times in serv.get():
                    data = serv.get()[times]
                    # ProductTimestamp = data['ProductTimestampid']
                    ProductTimestamp = data['timestampid']

                    service = db.reference('Services').child(ProductTimestamp.strip()).get()
                    servicename = service['servicename']
                    createdOn= service['createdOn']

                    status = ""
                    if times in acceptedlist:
                        status = "Delivered"
                    else:
                        status = "Pending"

                    tempTwo[times] = {
                        "servicename":servicename,
                        "createdOn":createdOn,
                        "status":status
                            }
            except:
                pass


            # context['products'] = tempOne
            # context['services'] = tempTwo

            numberProdcuts = len(tempOne.keys())
            numberServices = len(tempTwo.keys())
            context['prod'] = numberProdcuts
            context['serv'] = numberServices
        else:
            pass

        
    except Exception as df:
        print(df)
        print("################################## 136")



    try: # trying to get the service that is already provided to cusstomer and getting feedback on them
        referList =  list ( (db.reference('PendingActivity').child(email).get()).values()) 
        
        items = db.reference('MarketActivity').child(email).child('Purchased')
        temp = {}
        try:
            prodc = items.child('Products')
            
            for ts in referList:
                
                tmp = prodc.child(ts)
                if not tmp.get() == None:
                    newref = db.reference('Products').child(tmp.get()['ProductTimestamp'].strip()).get()        
                    name = newref['prodcutname']
                    date = tmp.get()['date']
                    temp[ts] = {
                        "name":name,
                        "date":date 
                    }

                    
        except:
            pass
        
        try:
            servi = items.child('Services')

            for ts in referList:
                tmp = servi.child(ts)
                if not tmp.get() == None:
                    newref = db.reference('Services').child(tmp.get()['ProductTimestamp'].strip()).get()
                    name = newref['servicename']
                    date = tmp.get()['date']

                    temp[ts] = {
                        "name":name,
                        "date":date 
                    }
                

        except:
            pass

          
        # context['forrating'] = temp
        
        accepted = len(temp.keys())
        context['accept'] = accepted

    except Exception as r:
        print(r)
        print("##########################################  1498")


    ret = reUsableForShopFunctions(request, context)
    return render(request, "MainApplication/public/Shop.html", context)

            

    


def Cart(request):
    context = {}
    
    if request.method == "POST":
        
        infns = dict( request.POST )
        
        quantity = infns['quantity'][0]
        type = infns['type'][0]
        timestamp = infns['val'][0]


        userSession = request.session['UserTokenId']

        session_Information = auth_.get_account_info(userSession)
        localId = session_Information['users'][0]['localId']
        """
        companyRef = dict(database.child('User').child('Customer').child('Company').get().val())
        
        
        IndividualRef = dict(database.child('User').child('Customer').child('Individual').get().val())
        """
        companyRef = db.reference('User').child('Company').get()

        
        IndividualRef = db.reference('User').child('Customer').get()

        companyRef = companyRef.keys()
        IndividualRef = IndividualRef.keys()

        if localId in companyRef:
            companyRef = db.reference('User').child('Company').child(str(localId)).get()
            fullName = companyRef['Detail']['companyName']
            email = companyRef['Detail']['companyEmail']


        elif localId in IndividualRef:
            IndividualRef = db.reference('User').child('Customer').child(str(localId)).get()
            fullName = IndividualRef['Detail']['fullName']
            email = IndividualRef['Detail']['email']
        
        at =  email.find('.')
        email = email[:at] + '' + email[at+1:]
        at =  email.find('@')
        email = email[:at] + '-AT-' + email[at+1:]

        



        ref = db.reference('MarketActivity').child(email)

        products = ref.child('Products')
        service = ref.child('Services')

        referenceHolder = ""
        try:
            products = products.get()

            for ts in products:
                data = products[ts]

                date = data['date']
                timestampid = data['timestampid']
                if timestamp.strip() == timestampid.strip():
                    referenceHolder = "Products"

        except Exception as ey:
            print(ey)
            print("################################# 5415")

        try:
            service = service.get()

            for ts in service:
                data = service[ts]

                date = data['date']

                timestampid = data['timestampid']
                

               
                if timestamp.strip() == timestampid.strip():
                    referenceHolder = "Services"

        except Exception as ey:
            print(ey)
            print("################################# 5413")

        
        ref =  ref.child(referenceHolder)
        

        for tss in ref.get():
            dt = ref.get()[tss]

            timts = dt['timestampid']
            if timestamp.strip() == timts.strip():
                ref = ref.child(tss)
                break

        
        

        purchasing = db.reference('MarketActivity').child(email).child('Purchased')

        purchasedService = purchasing.child(referenceHolder)
        

        import datetime

        date = datetime.datetime.now().strftime('%Y-%B-%d')


        cust = db.reference('User')
        customerTimestamp = ""
        for typee in cust.get():
            data = cust.get()[typee]

            for times in data:
                 infn = data[times]

                 currentEmail = ""
                 if typee == 'Company':
                     currentEmail = infn['Detail']['companyEmail']
                     
                 elif typee == 'Customer':
                     currentEmail = infn['Detail']['email']
                     
                 
                 at =  currentEmail.find('.')
                 currentEmail = currentEmail[:at] + '' + currentEmail[at+1:]
                 at =  currentEmail.find('@')
                 currentEmail = currentEmail[:at] + '-AT-' + currentEmail[at+1:]

                 if currentEmail.strip() == email.strip():
                     customerTimestamp = times
                     break

            


         

        temp = {
            "ProductTimestamp" :timestamp,
            "customerTimestamp":customerTimestamp,
            "date":date,
            "quantity":quantity,
            "type":type,
            "fullName":fullName,

        }
        


        try:
            ref.delete()
            purchasedService.push(temp)
            return redirect('cart')
        except Exception as e:
            print(e)
            print("###################### 416")
        

        # return render(request, "MainApplication/public/Cart.html", context)


    else:
        userSession = request.session['UserTokenId']

        session_Information = auth_.get_account_info(userSession)
        localId = session_Information['users'][0]['localId']

        # companyRef = dict(database.child('User').child(
        #     'Customer').child('Company').get().val())
        # IndividualRef = dict(database.child('User').child(
        #     'Customer').child('Individual').get().val())
        companyRef = db.reference('User').child('Company').get()

        
        IndividualRef = db.reference('User').child('Customer').get()

        companyRef = companyRef.keys()
        IndividualRef = IndividualRef.keys()

        if localId in companyRef:
            # companyRef = dict(database.child('User').child(
            #     'Customer').child('Company').child(str(localId)).get().val())

            companyRef = db.reference('User').child('Company').child(str(localId)).get()

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
            # IndividualRef = dict(database.child('User').child(
            #     'Customer').child('Individual').child(str(localId)).get().val())
            IndividualRef = db.reference('User').child('Customer').child(str(localId)).get()

            fullName = IndividualRef['Detail']['fullName']
            email = IndividualRef['Detail']['email']
        
        at =  email.find('.')
        email = email[:at] + '' + email[at+1:]
        at =  email.find('@')
        email = email[:at] + '-AT-' + email[at+1:]


        try: # get the reference from db
            ref = db.reference('MarketActivity').child(email)
            if ref.get() is not None:
                data = ref.get()
                try:
                     product = data['Products']
                except:# cuz it means there is no such shit
                    product = None
                try:
                    service = data['Services']
                except:
                    service = None

                # first handle all the products 
                ct = {}
                ct2 = {}
                
                if product is not None:
                    for ts in product:
                        prods = product[ts]

                        date = prods['date']
                        timstsForProd = prods['timestampid']


                        refPoduct = db.reference('Products').child(timstsForProd)

                        data = refPoduct.get()
                        
                        prodcutname = data['prodcutname']
                        prodcutType =data['prodcutType']
                        price = data['price']
                        PriceType = data['PriceType']
                        Description = data['Description']
                        rating = data['rating']
                        shippementDays = data['shippementDays']
                        createdOn = data['createdOn']

                        temp = {
                            'prodcutname':prodcutname,
                            'Description':Description,
                            'prodcutType':prodcutType,
                            'createdOn':createdOn,
                            'price':price,
                            'rating':rating,
                            'PriceType':PriceType,
                            'shippementDays':shippementDays
                        }
                        ct [timstsForProd] = temp
                        temp = {}
                if  service is not None:
                    
                    for ts in service:
                        serv = service[ts]

                        date = serv['date']
                        timstsForProd = serv['timestampid']


                        refPoduct = db.reference('Services').child(timstsForProd)

                        data = refPoduct.get()
                        
                        Description = data['Description']
                        servicename = data['servicename']
                        serviceType = data['serviceType']
                        price = data['price']
                        PriceType = data['PriceType']
                        rating = data['rating']
                        createdOn = data['createdOn']

                        temp = {
                        'servicename':servicename,
                        'Description':Description,
                        'serviceType':serviceType,
                        'createdOn':createdOn,
                        'price':price,
                        'rating': rating[0],
                        'PriceType':PriceType[0],
                        
                        }
                        ct2 [timstsForProd] = temp
                        temp = {}
                    
                
                if ( not ct) and (not ct2):
                    return redirect('nocart')


                context['Prod'] = ct

                context['serv'] = ct2

                return render(request, "MainApplication/public/Cart.html", context)

                
        except Exception as rt:
            print(rt)
            print("#######################################  900")
            return redirect('nocart')

    
    
def NoCart(request):
    return render(request,  "MainApplication/public/cartEmpty.html")



contextCheck = {}
def AddToCartButtonOperation(request, timestampid):
    global contextCheck

    userSession = request.session['UserTokenId']

    session_Information = auth_.get_account_info(userSession)
    localId = session_Information['users'][0]['localId']

    # companyRef = dict(database.child('User').child(
    #     'Customer').child('Company').get().val())
    companyRef = db.reference('User').child('Company').get()
    # IndividualRef = dict(database.child('User').child(
    #     'Customer').child('Individual').get().val())

    IndividualRef = db.reference('User').child('Customer').get()

    
    
    companyRef = list(companyRef.keys())
    IndividualRef =list( IndividualRef.keys())


   
    if localId in companyRef:
        
        companyRef = db.reference('User').child('Company').child(str(localId)).get()

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
        
        IndividualRef = db.reference('User').child('Customer').child(str(localId)).get()

        fullName = IndividualRef['Detail']['fullName']
        email = IndividualRef['Detail']['email']
    at =  email.find('.')
    email = email[:at] + '' + email[at+1:]
    at =  email.find('@')
    email = email[:at] + '-AT-' + email[at+1:]

    try:
         ref = db.reference('Cart').child(email)
    except Exception as er:
        print(er)
        print("######################### 7956 ")
    
    refrenceHolder = ""
    # checking that wherther the reqested item is prdouct or service bleow
    try:
        ProdvRef = list(db.reference('Products').get().keys())
        if timestampid in  ProdvRef:
            refrenceHolder = "Products"
    except Exception as er:
        print(er)
        print("############################### 369")
    
        
        
    try:
        ProdvRef = list(db.reference('Services').get().keys())
        if timestampid in  ProdvRef:
            refrenceHolder = "Services"

           
    except Exception as er:
        print(er)
        print("############################### 365")
    
        

    
    
    
    
   

    ref = db.reference('MarketActivity').child(email).child(refrenceHolder)
    
    
    """
        check if its already added to the cart for just fast load up below
    """
    fg = False
    try:
        ref2 = ref.get()

        if ref2 is not None:

            for timestamps in ref2:
                realData = ref2[timestamps]

                timestamp = realData['timestampid']
                temp = {}
                if timestamp == timestampid:
                    fg = True
                    contextCheck['flag'] = True
                    temp['id'] = timestampid

                    if refrenceHolder == 'Services':
                        temp['type'] = "Serv"
                        
                    elif refrenceHolder == 'Products':
                        temp['type'] = "prod"

                contextCheck['check'] = temp   
                temp = {}  


    except Exception as rt:
        print(rt)
        print("######################################### 102")
    
    print(fg)
    if not fg:
        import datetime

        date = datetime.datetime.now().strftime('%Y-%B-%d')
        
        temp = {
            "timestampid" : timestampid,
            "date":date 
        }

        try:
            ref.push(temp)
            return redirect('shop')
        except Exception as err:
            print(err)
            print("#################################################  915")
    else:
        val = reUsableForShopFunctions(request, contextCheck)
        return render(request, "MainApplication/public/Shop.html", val)



    


def DashBoardStaff(request):


    context = {}
    try: # number of customer
        
        ref = db.reference('User').child('Company')
        ref2 = db.reference('User').child('Customer')


        ref = list(ref.get().keys())
        ref2 = list(ref2.get())

        ref= int( len(ref)) 
        ref2 = int( len(ref2))

        totalCustomerAcc = ref + ref2
        context['totalCustomerAcc'] = totalCustomerAcc



    except Exception as er:
        print(er)
        print("######################################  842")

    try: # u gonna do it when u add purachesed addes in customer section cuz u gonna add date when the they made purchasing
        ref = list(db.reference('MarketActivity').get().keys())

        context['ActivelyEngaiging'] = len(ref)
        
    except Exception as r:
        print(r)
        print("###################################### 4586")

    

    try: # u have to do it after u added it that the number of customers  who send feedback 
        
        ref = db.reference('CommentOrFeedBack')
        TotalCount = 0
        for month in ref.get():
            TotalCount += len(list( ref.get()[month] ))

        

        context["PeoplesEngaging"] = str(TotalCount)

    except Exception as r:
        print(r)
        print("###################################### 1889")
        context["PeoplesEngaging"] = str(0)






    try:
        flag = False
        ActiveFeedBacks = []
        ref = db.reference('PageInforamtion')
        ref = ref.get()

        count = len(list(ref.keys()))

        if count > 3:
            flag = True
        else:
           for keys in ref:
               temp = {}
               data = ref[keys]

               Description = data['Description']
               companyname = data['companyname']

            
          
               temp = {

                    'companyname':companyname,
                    'Description':Description
                 }
               ActiveFeedBacks.append(temp)
               temp = {}
        
        key = list(ref.keys())
        
        ActiveFeedBacks = dict(zip(key, ActiveFeedBacks))
        
        context['ActiveFeedBacks'] = ActiveFeedBacks
        context['flag'] = flag

        # print(context['ActiveFeedBacks'])
        
    except Exception as r:
        print(r)
        print("###################################### 4781")



    try:
        
        
        ref = db.reference('CommentOrFeedBack')
        commentOrFeedback = []
        for month in ref.get():
            custFeedback = (ref.get())[month]
            for key in custFeedback:
                infn = custFeedback[key]
                name = infn['name']
                comments = infn['comment']
                givenOn = infn['createdOn']

                temp = {
                    "name":name,
                    "givenOn":givenOn
                }

                commentOrFeedback.append(temp)
                temp = {}
        
        key = []
        for month in ref.get():
            custFeedback = (ref.get())[month]
            for k in custFeedback:
                key.append(k)





        
        commentOrFeedback = dict(zip(list(key),list(commentOrFeedback)))
        

        context['commentOrFeedback'] = commentOrFeedback



    except Exception as r:
        print(r)
        print("###################################### 4501")




    return render(request, "MainApplication/private/staff/DashBoardStaff.html", context)


def PurchasingItems(request, timestamp):

    mainContext = {}
    if timestamp.strip() == "viewpage":
        
        """
        iterate throug all and provide and id of container time stamp for the buttons so that they can navigate easily

        infn need is just the name of prod and customer and a a date
        """

        try:
            ref = db.reference('MarketActivity')
            context = {}
            for emails in ref.get():
                try:
                    data = ref.get()[emails]['Purchased']
                    prodTemp = {}
                    try:
                        product = data['Products']
                        

                        for timestamp in product:
                            
                            infn = product[timestamp]
                            
                            ProductTimestamp = infn['ProductTimestamp']
                            customerTimestamp = infn['customerTimestamp']
                            fullName = infn['fullName']
                            date = infn['date']

                            

                            try:# get the product list 
                                reff = db.reference('Products').child(ProductTimestamp.strip())

                                prodcutname = reff.get()['prodcutname']


                                prodTemp["prodcutname"] = prodcutname
                                prodTemp["date"] = date
                                prodTemp['fullName'] = fullName
                                prodTemp['type'] = "Product"

                                context[timestamp] = prodTemp
                                prodTemp = {}



                            except Exception as t:
                                print(t)
                                print("########################### 193")

                        mainContext["product"] = context
                    except: # This is for checking if customer has purchased prodouct
                        pass
                    
                    
                    ServTemp = {}
                    try:
                        services = data['Services']
                        for timestamp in services:
                            
                            infn = services[timestamp]
                            
                            ProductTimestamp = infn['ProductTimestamp']
                            fullName = infn['fullName']
                            date = infn['date']

                            

                            try:# get the product list 
                                reff = db.reference('Services').child(ProductTimestamp.strip())

                                servicename = reff.get()['servicename']
                                

                                ServTemp["servicename"] = servicename
                                ServTemp["date"] = date
                                ServTemp['fullName'] = fullName
                                ServTemp['type'] = "Service"

                                context[timestamp] = ServTemp
                                ServTemp = {}
                            except:
                                pass
                        mainContext["Service"] = context
                        
                    except: # This is for checking if customer has purchased Customer
                        print("############################### 100")

                except:
                    print("#################################### 99")
            

        except Exception as ert:
            print(ert)
            print("#################################  4533")

    else:
        ref = db.reference('MarketActivity')
        for emails in ref.get():
            
            
            data = ref.get()[emails]
            
            for items in data:
                try:
                    if items != "Purchased":
                        continue
                    
                    PurchasedItem = data[items]

                    ref = db.reference('MarketActivity').child(emails)

                    FLAG = False
                    try: # to check if  required is product
                        refere = list((ref.child('Products').get()).keys())
                        
                        if timestamp.strip() in refere:
                            FLAG =True
                            ref = ref.child('Products').child(timestamp)
                            
                    except:
                        pass
                    if not FLAG: 
                        try:# to chech if required is service
                            refere = list((ref.child('Services').get()).keys())

                            if timestamp.strip() in refere:
                                FLAG =True
                                ref = ref.child('Services').child(timestamp)
                        except:
                            pass


                    if FLAG:
                        try:# the final case deletion
                            ref.delete()
                            return redirect('/private/staff/purchasingitems''/viewpage')
                        except Exception as err:
                            print(err)
                            print("################################# 780")

                except Exception as er:
                    print(er)
                    print("################################ 5669")
    
    
    return render(request,  "MainApplication/private/staff/PurchasingItems.html", mainContext)


def PurchasingItemsCustViewPage(request, timestampid):
    context = {}
    customerName= ""
    customerPhoneNumber =""
    customerEmail= ""

    productName =""
    ProductType =""
    productDescription = ""
    try:
        ref = db.reference('MarketActivity')
        for emails in ref.get():
            data = ref.get()[emails]
            FLAG = False
            for types in data:
                infns = data[types]
                
                if types != 'Purchased':
                    continue


            
                
                try:
                    products =list( infns['Products'].keys() )
                    

                    if timestampid.strip() in products:
                        
                        FLAG = True
                        ref = ref.child(emails).child('Purchased').child('Products').child(timestampid.strip())
                        
                        
                        # get ALL infn about the customer also prodcut
                        
                        prod = db.reference('Products').child((ref.get()['ProductTimestamp']).strip())
                        
                        
                        productDescription = prod.get()['Description']
                        productName = prod.get()['prodcutname']
                        prodcutType = prod.get()['prodcutType']
                        
                        

                        Cust = db.reference('User')
                        dt = Cust.get()
                        
                        try:
                            dtc =  dt['Company']
                            
                            cmp = list(dtc.keys())
                            customerId = (ref.get()['customerTimestamp']).strip()
                           
                            if customerId in cmp:
                                Cust = db.reference('User').child('Company').child(customerId).child('Detail')
                                Cust= Cust.get()

                                customerName = Cust['companyName']
                                customerPhoneNumber = Cust['companyPhoneNumber']
                                customerEmail = Cust['companyEmail']
                                
                                
                        except: #
                            pass
                        
                        try:
                            
                            dt =  dt['Customer']
                            
                            cmp = list(dt.keys())
                            customerId = (ref.get()['customerTimestamp']).strip()
                           
                            
                            if customerId in cmp:
                                Cust = db.reference('User').child('Customer').child(customerId).child('Detail')
                                Cust= Cust.get()
                                
                                customerName = Cust['fullName']
                                customerPhoneNumber = Cust['phoneNumber']
                                customerEmail = Cust['email']
                                
                        except:
                                pass
                        
                        CHECKER = False 
                        try:## check if its aready been set to pending status
                            
                            crtref = db.reference('PendingActivity').child(emails) #.push([timestampid.strip()])
                            crtref = list((crtref.get()).values())

                            if timestampid.strip() in crtref:
                                CHECKER = True
                                pass # it means its already here no need to 


                        except:
                            pass
                        
                        
                        
                        if not CHECKER:
                            
                            crtref = db.reference('PendingActivity').child(emails).push(timestampid.strip())
                        
                        break

                except:
                    pass
                

                print(FLAG)
                
                if not FLAG:
                    
                    try:
                        Service =list( infns['Services'].keys() )
                        

                        
                        if timestampid.strip() in Service:
                            FLAG = True
                            ref = ref.child(emails).child('Purchased').child('Services').child(timestampid.strip())
                            
                            
                            # get ALL infn about the customer also prodcut
                            
                            prod = db.reference('Services').child((ref.get()['ProductTimestamp']).strip())
                            
                            productDescription = prod.get()['Description']
                            productName = prod.get()['servicename']
                            prodcutType = prod.get()['serviceType']


                            Cust = db.reference('User')
                            dt = Cust.get()
                            
                            try:
                                dtcc =  dt['Company']
                                cmp = list(dtcc.keys())
                                customerId = (ref.get()['customerTimestamp']).strip()
                            

                                if customerId in cmp:
                                    Cust = db.reference('User').child('Company').child(customerId).child('Detail')
                                    Cust= Cust.get()

                                    customerName = Cust['companyName']
                                    customerPhoneNumber = Cust['companyPhoneNumber']
                                    customerEmail = Cust['companyEmail']
                                    
                            except: #
                                pass

                            try:
                                dt =  dt['Customer']
                                cmp = list(dt.keys())
                                customerId = (ref.get()['customerTimestamp']).strip()
                            
                                
                                if customerId in cmp:
                                    Cust = db.reference('User').child('Customer').child(customerId).child('Detail')
                                    Cust= Cust.get()

                                    customerName = Cust['fullName']
                                    customerPhoneNumber = Cust['phoneNumber']
                                    customerEmail = Cust['email']
                            except:
                                    pass

                            CHECKER = False 
                            try:## check if its aready been set to pending status
                                
                                crtref = db.reference('PendingActivity').child(emails) #.push([timestampid.strip()])
                                crtref = list((crtref.get()).values())
                                
                                if timestampid.strip() in crtref:
                                    CHECKER = True
                                    pass # it means its already here no need to 


                            except:
                                pass
                            
                            if not CHECKER:
                                crtref = db.reference('PendingActivity').child(emails).push(timestampid.strip())
                            
                            break
                    except:
                        pass

        temp = {
            "customerName" :customerName,
            "customerEmail":customerEmail,
            "customerPhoneNumber":customerPhoneNumber,
            "prodcutType":prodcutType,
            "productDescription":productDescription,
            "productName":productName
        }          
        
        context= temp
        
    except Exception as e:
        # print(e)
        # print(rty)
        print("##################################### 4987")
    return render(request, "MainApplication/private/staff/CustomerDetailInfnShowingPage.html", context)


def productAndService(request):
    dictone= {}
    dicttwo = {}
    context = {}
    try:
        ref = db.reference('Services')
        ref = ref.get()
        if ref is not None:
            for items in ref:
                data = ref[items] 
                dictone[items] = data
            pack = []
            for data in list(ref.values()):
            
                Description = data['Description']
                servicename = data['servicename']
                serviceType = data['serviceType']
                price = data['price']
                PriceType = data['PriceType']
                rating = data['rating']
                createdOn = data['createdOn']

                temp = {
                'servicename':servicename,
                'Description':Description,
                'serviceType':serviceType,
                'createdOn':createdOn,
                'price':price,
                'rating':rating,
                'PriceType':PriceType,
                }
                
                pack.append(temp)
                temp = {}

            keyonly = list(ref.keys())

            dictone=dict(zip(keyonly, pack))
            pack = []
            context["service"] = dictone
        else:

            pass
    except Exception as e:
        print(e)
        context["service"] = {}
        print("########################## 758")
        pass

    try:
        ref2 = db.reference('Products')
        ref2 = ref2.get()

        
        if ref2 is not None:

            for items in ref2:
                data = ref2[items]
                dicttwo[items] = data

            pack = []
            for data in list(ref2.values()):
            
                Description = data['Description']
                prodcutname = data['prodcutname']
                prodcutType = data['prodcutType']
                price = data['price']
                PriceType = data['PriceType']
                rating = data['rating']
                createdOn = data['createdOn'] 
                shippementDays = data['shippementDays'] 


                temp = {
                'prodcutname':prodcutname,
                'Description':Description,
                'prodcutType':prodcutType,
                'createdOn':createdOn,
                'price':price,
                'rating':rating,
                'PriceType':PriceType,
                }
                
                pack.append(temp)
                temp = {}

            keyonly = list(ref2.keys())

            dicttwo=dict(zip(keyonly, pack))
            
            context['product']= dicttwo
        else:
            pass




    except Exception as e:
        print(e)
        context['product']= {}
        print("######################## 458")

       
    


    


    return render(request,  "MainApplication/private/staff/productAndService.html", context)


def FormForProducts(request , timestamp):
    if timestamp.strip() == '-1':
        if request.method == 'POST':
            allTheData = dict( request.POST)
            imageFile = allTheData['imageFile']
            prodcutname = str(allTheData['prodcutname'][0])
            prodcutType = str(allTheData['prodcutType'][0])

            price = str(allTheData['price'][0])
            PriceType = str(allTheData['PriceType'][0])
            Description = str(allTheData['Description'][0])
            rating = str(allTheData['rating'][0])
            shippementDays = str(allTheData['shippementDays'][0])
            import datetime

            currentDate = datetime.datetime.now().strftime('%Y-%B-%d')

            dbQUERY = db.reference('Products')
            details = {

                "prodcutname": prodcutname,
                "prodcutType":prodcutType,
                "price":price,
                'PriceType':PriceType,
                'Description':Description,
                'rating':rating,
                'shippementDays':shippementDays,
                'createdOn':currentDate

            }

            try:
                dbQUERY.push(details)
                return redirect('productandservice')
            except:
                print("####################  er 456 ")


            """
            <QueryDict: {'csrfmiddlewaretoken': ['3M5UtUB7DOvumdOimfFJBJnSx8CM7m9pNoKUlrMJkNiKxxRLlErF9LTP523yFzyQ'], 'imageFile': [''], 'prodcutname': [''], 'prodcutType': [''], 'price': [''], 'PriceType': [''], 'Description': [''], 'rating': [''], 'shippementDays': ['']}>
           """
    else:
        try:
            if request.method == "POST":
                ref = db.reference('Products').child(str(timestamp))
                
                allTheData = dict(request.POST)
                imageFile = allTheData['imageFile']
                prodcutname = str(allTheData['prodcutname'][0])
                prodcutType = str(allTheData['prodcutType'][0])
                price = str(allTheData['price'][0])
                PriceType = str(allTheData['PriceType'][0])
                Description = str(allTheData['Description'][0])
                rating = str(allTheData['rating'][0])
                shippementDays = str(allTheData['shippementDays'][0])
                import datetime

                currentDate = datetime.datetime.now().strftime('%Y-%B-%d')

                details = {

                    "prodcutname": prodcutname,
                    "prodcutType":prodcutType,
                    "price":price,
                    'PriceType':PriceType,
                    'Description':Description,
                    'rating':rating,
                    'shippementDays':shippementDays,
                    'createdOn':currentDate

                }

                try:

                    ref.update(details)
                    return redirect('productandservice')
                except:

                    print("###################################### 98  errrrrr")
            else:
                ref = db.reference('Products').child(str(timestamp))
                data = ref.get()
                
                prodcutname = data['prodcutname']
                prodcutType =data['prodcutType']
                price = data['price']
                PriceType = data['PriceType']
                Description = data['Description']
                rating = data['rating']
                shippementDays = data['shippementDays']
                createdOn = data['createdOn']

                temp = {
                    'prodcutname':prodcutname,
                    'Description':Description,
                    'prodcutType':prodcutType,
                    'createdOn':createdOn,
                    'price':price,
                    'rating':rating,
                    'PriceType':PriceType,
                    'shippementDays':shippementDays
                }
                
                context = {"flag":True, "data":temp}
                
                return render(request,"MainApplication/private/staff/FormForProducts.html" , context )


        except:
            print("##############################33 produuuuuuuuuuuuuuuuct")
    
    
    
    
    
    
    return render(request, "MainApplication/private/staff/FormForProducts.html")









def FormForServices(request, timestamp):
    """
    {'csrfmiddlewaretoken': ['2ozBUY0qKtnnE9isrF2sbU7LNAhcrdf6M0eBMvb2rsaDPtlVq4OoJWDIluIYZqEx'], 'imageFile': [''], 
    'servicename': [''], 'serviceType': [''], 'price': [''], 
    'PriceType': ['Negotiable'], 'Description': [''], 'rating': ['']}
    """
    if timestamp.strip() == '-1':

        if request.method == 'POST':
            allTheData = dict(request.POST)
            imageFile = (allTheData['imageFile'])
            servicename = str(allTheData['servicename'][0])
            serviceType = str(allTheData['serviceType'][0])
            price = str(allTheData['price'][0])
            PriceType = str(allTheData['PriceType'][0])
            Description = str(allTheData['Description'][0])
            rating = str(allTheData['rating'][0])
            
            import datetime

            currentDate = datetime.datetime.now().strftime('%Y-%B-%d')

            dbQUERY = database.child('Services')
            details = {
                "servicename":servicename,
                "serviceType":serviceType,
                "price":price,
                'PriceType':PriceType,
                'Description':Description,
                'rating':rating,
                'createdOn': str(currentDate)

            }

            try:
                dbQUERY.push(details)
                return redirect('productandservice')
            except:
                print("########################################### 987")
    else:
        try:
            
            if request.method == "POST":

                ref = db.reference('Services').child(str(timestamp))
                allTheData = dict(request.POST)
                imageFile = (allTheData['imageFile'])
                servicename = str(allTheData['servicename'][0])
                serviceType = str(allTheData['serviceType'][0])
                price = str(allTheData['price'][0])
                PriceType = str(allTheData['PriceType'][0])
                Description = str(allTheData['Description'][0])
                rating = str(allTheData['rating'][0])
                
                import datetime

                

                currentDate = datetime.datetime.now().strftime('%Y-%B-%d')

                details = {
                    "servicename":servicename,
                    "serviceType":serviceType,
                    "price":price,
                    'PriceType':PriceType,
                    'Description':Description,
                    'rating':rating,
                    'createdOn': str(currentDate)

                }
                try:

                    ref.update(details)
                    return redirect('productandservice')
                except:

                    print("###################################### 98  errrrrr")
            else:

                ref = db.reference('Services').child(str(timestamp))
                data = ref.get()
                
                Description = data['Description']
                servicename = data['servicename']
                serviceType = data['serviceType']
                price = data['price']
                PriceType = data['PriceType']
                rating = data['rating']
                createdOn = data['createdOn']

                temp = {
                'servicename':servicename,
                'Description':Description,
                'serviceType':serviceType,
                'createdOn':createdOn,
                'price':price,
                'rating':rating,
                'PriceType':PriceType,
                }

                context = {"flag":True, "data":temp}
                return render(request,"MainApplication/private/staff/FormServices.html" , context )

        except:
            print("##############################33 Serviceeeeeeeee")

    return render(request,"MainApplication/private/staff/FormServices.html" )


def FormPageContent(request,timestamp):


    """
    'imageFile': [''], 'companyname': [''], 'Description': ['']}
    
    """

    if timestamp == '-1':
        if request.method == 'POST':
            try:
                datas = dict(request.POST)
                companyname = datas['companyname'][0]
                Description = datas['Description'][0]


                details = {
                    "companyname":companyname,
                    "Description":Description
                }
                
                
                ref = db.reference('PageInforamtion')
                try:

                    rlen = len(list(ref.get()))
                    if rlen <3:
                        ref.push(details)
                except:

                    ref.push(details)
            except Exception as e:
                print(e)
                print("############################### 882")
    else:
        if request.method == 'POST':
            datas = dict(request.POST)
            companyname = datas['companyname'][0]
            Description = datas['Description'][0]


            details = {
                "companyname":companyname,
                "Description":Description
            }
            
            
            ref = db.reference('PageInforamtion').child(timestamp)
            try:
                ref.set(details)
                return redirect('dashboardstaff')

            except Exception as er:
                print(er)
                print("############################# 802 ")

        else:
            ref = db.reference('PageInforamtion').child(timestamp)

            ref = ref.get()

            Description = ref['Description']
            companyname = ref['companyname']

            temp = {
                "Description":Description,
                "companyname":companyname
            }
            
            context = {
                "flag":True,
                "temp":temp
            }
            return render(request,"MainApplication/private/staff/FormPageContent.html", context)



    return render(request,"MainApplication/private/staff/FormPageContent.html")






# https://stackoverflow.com/questions/69217118/getting-specific-errors-type-message-from-httperror-while-working-django-fireba

def ItemDeleter(reff):
    try:
        reff[0].delete()
        reff=[]
        return 
    except Exception as e:
        print(e)
        print("######################################### 355 errrrr")
        

reff = []
def DeleteItem(request, timestampid):
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        r = db.reference('Services').child(timestampid)
        reff.append(r)
    elif timestampid == '-1':
        ItemDeleter(reff)
        return redirect('productandservice')
    

    




    return render(request, "MainApplication/private/staff/DeleteConfirmationPage.html")



def DeleteProd(request, timestampid):
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        r = db.reference('Products').child(timestampid)
        reff.append(r)
    elif timestampid == '-1':
        ItemDeleter(reff)
        return redirect('productandservice')

    return render(request, "MainApplication/private/staff/DeleteConfirmationPageForProduct.html")



def DeletePageConent(request , timestampid):
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        r = db.reference('PageInforamtion').child(timestampid)
        reff.append(r)
    elif timestampid == '-1':
        try:
            reff[0].delete()
        except Exception as r:
            print(r)
        print("###################################   411 ")
        return redirect('dashboardstaff')

    return render(request, "MainApplication/private/staff/DeleteConfirmationPageForPageContent.html")



def ViewFullInfn(request, timestampid):
    

    try:
        ref = db.reference('CommentOrFeedBack')

        for months in ref.get():
            data = ref.get()[months].keys()
            if timestampid in list(data):
                data = ref.child(months).child(timestampid).get()
                
                comment = data['comment']
                createdOn= data['createdOn']
                name = data['name']

                temp = {
                     "name":data['name'],
                     "createdOn":data['createdOn'],
                     "comment":data['comment']
                 }
                return render(request, "MainApplication/private/staff/InfnViewPage.html", {"temp":temp})

            

    except Exception as er:
        print(er)
        print("##################################3 114")

    return render(request, "MainApplication/private/staff/InfnViewPage.html")


def DeleteFeedback(request ,timestampid):
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        ref = db.reference('CommentOrFeedBack')
        for months in ref.get():
            
            data = ref.get()[months].keys()
            
            if timestampid in list(data):
                data = ref.child(months).child(timestampid)
                reff.append(data)
                break

    elif timestampid == '-1':
        try:

            reff[0].delete()
            return redirect('dashboardstaff') 
            

        except Exception as r:
            print(r)
            print("###################################   411 ")
            return redirect('dashboardstaff')


    return render(request, "MainApplication/private/staff/DeleteConfirmationPagePepolesFeedBack.html")


def DeleteCartItems(request, timestampid):
    global reff
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        userSession = request.session['UserTokenId']

        session_Information = auth_.get_account_info(userSession)
        localId = session_Information['users'][0]['localId']

        companyRef = dict(database.child('User').child(
            'Customer').child('Company').get().val())
        IndividualRef = dict(database.child('User').child(
            'Customer').child('Individual').get().val())

        companyRef = companyRef.keys()
        IndividualRef = IndividualRef.keys()

        if localId in companyRef:
            companyRef = dict(database.child('User').child(
                'Customer').child('Company').child(str(localId)).get().val())
            fullName = companyRef['Detail']['companyName']
            email = companyRef['Detail']['companyEmail']


        elif localId in IndividualRef:
            IndividualRef = dict(database.child('User').child(
                'Customer').child('Individual').child(str(localId)).get().val())
            fullName = IndividualRef['Detail']['fullName']
            email = IndividualRef['Detail']['email']
        
        at =  email.find('.')
        email = email[:at] + '' + email[at+1:]
        at =  email.find('@')
        email = email[:at] + '-AT-' + email[at+1:]


        ref = db.reference('MarketActivity').child(email)

        # for checking create two d/n db instances 

        try:
            prod = ref.get()
            if prod is not None:

                for times in prod:
                    data = prod[times]
                    if times == 'Purchased':
                        continue
                    

                    for sects in data:
                        data2 = data[sects]
                        

                        timestampP = data2['timestampid']

                        if timestampP.strip() ==  timestampid.strip():
                            
                            ref = ref.child(times).child(sects.strip())



        except Exception as t:
            print(t)
            print("################## 1498")
        




        reff.append(ref)

        

    elif timestampid == '-1':
        try:

            reff[0].delete()
            reff = []
            return redirect('cart') 
            

        except Exception as r:
            print(r)
            print("###################################   411 ")
            return redirect('cart')

    return render(request, "MainApplication/public/DeleteConfirmationPageForCartItems.html")



def SaveItemRating(request, timestampid):
    
    global reff
    # print(request.POST)
    if timestampid.strip() != '-1' and timestampid.strip() != '1':
        import datetime
        dt = datetime.datetime.now().strftime('%d-%B-%Y')
        temp = {
            'timestampOfItem': timestampid,
            "date":dt
        }


        
        reff.append(temp)
        

    elif timestampid == '-1':
        try:
            ref = db.reference('ItemsRating').push(reff[0])
            reff = []
            return redirect('dashboard') 
            

        except Exception as r:
            print(r)
            print("###################################   411 ")
            return redirect('dashboard')


    return render(request, "MainApplication/public/SaveConfirmationPage.html")