from random import randint

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from discotech.models import users, products, transactions
from discotech.auth import Authetic
from discotech.twofa import sendemail
from django.template import loader
from django.db import IntegrityError

from django.contrib import messages


def mainpage(request):
    return render(request, "mainPage.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        given_password = request.POST.get('pass')
        result = users.objects.filter(email=email)
        password = ''
        for index in result:
            password = index.password
        authobject = Authetic(password)
        decrypt_password = authobject.decrypt(password)
        if given_password == decrypt_password:
            code = randint(1111, 9999)
            sendemail(email, code)
            if request.method == 'POST': # 2fa problem
                submittedcode = request.POST.get('code')
                if submittedcode == str(code):
                    print("login succesfull")
                    return redirect('/')
                else:
                    print('try again')
                return render(request, "2fa.html")
            #for index in result:
                #idiotita = index.idiotita

            #request.session['username'] = username
            #request.session['idiotita'] = idiotita
            # test
            # if request.session:
            #   return HttpResponse( request.session['username'])


        else:
            arguments = {}
            arguments['mnm'] = "! Wrong Password or Username !"
            return TemplateResponse(request, 'login.html', arguments)
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        password = str(password)
        authobject = Authetic(password)
        #return HttpResponse(str(Authetic.encrypt(authobject)))
        try:
            newuser = users.objects.create(firstname=firstname, lastname=lastname, email=email, telephone=telephone, password=str(Authetic.encrypt(authobject)))
            arguments = {}
            arguments['mnm'] = "Try to login with your new account"
            return TemplateResponse(request, 'login.html', arguments)
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "email exist"
            return TemplateResponse(request, 'register.html', arguments)
    else:
        arguments = {}
        arguments['mnm'] = ""
        return TemplateResponse(request, 'register.html', arguments)



def proionta(request):
    result = products.objects.all()

    return render(request, "proionta.html", {'products': result})


def transaction(request):
    #building purposes
    email = 'sperako948@gmail.com'
    prod_id = '001'
    #transaction code
    user = users.objects.filter(email=email)
    product = products.objects.filter(id=prod_id)
    if request.method == 'POST':
        cardnumber = request.POST.get('cardnumber')
        cardcode = request.POST.get('cardcode')
        #need to add encryption for card number and card code
        try:
            transaction = transactions.objects.create(prod_id=product.id, email=user.email, cardnumber=cardnumber,
                                                      cardcode=cardcode)
            arguments = {}
            arguments['mnm'] = "Transaction successful"
            return TemplateResponse(request, 'mainPage.html', arguments)
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "Sorry there was an error"
            return TemplateResponse(request, 'transactions.html.html', arguments)
    return render(request, "transactions.html", {'product': product, 'user': user})

#for testing purposes of the 2factor system
def twofa(request):
    code = randint(1111, 9999)
    #sendemail(email, code)
    if request.method == 'POST':
        submittedcode = request.POST.get('code')
        if submittedcode == str(code):
            print("login succesfull")
            return redirect('/')
        else:
            print('try again')
    return render(request, "2fa.html")

def logout(request):
    if request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

        #messages.info(request, "Logged out succesfully!")