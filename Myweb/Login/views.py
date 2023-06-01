from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from .models import Etud
from django.contrib.auth import *
from django.contrib.auth import logout as auth_louhout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import datetime
from pages.models import Etud_Cours, Etud_Questions,Admin_Ann
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import re
from django.http import HttpResponse
# Create your views here.
def Login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/profile')
        else:
            messages.error(request, 'invalide username or password')
    else:
        error_message = None
           
    return render(request ,'Login/login.html') 


#login admin 
def Login_Admin(request):
    
    if request.method == 'POST':
        username = request.POST['usernameA']
        password = request.POST['passwordA']
        idd = request.POST['idd']
        #test 3la id te3 addmin
        if not re.match(r'^admin', idd):
            messages.error(request, 'Invalid idd')
            return render(request ,'Login/adminLogin.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/adminee')
        else:
            messages.error(request, 'invalide username or password')
    else:
        error_message = None
           
    return render(request ,'Login/adminLogin.html') 


def Signin(request):
    if request.method == 'POST':
        Username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        idd = request.POST['id']
        password1 = request.POST['password1']
        
        current_year = datetime.datetime.now().year
        start_year = 2010
        
        if int(idd[:4]) not in range(start_year, current_year+1):
            messages.error(request, 'NUMERO DE LA CARTE ETUDIANT EST INCORECTE !! ')
            return redirect('http://127.0.0.1:8000/register')
        
        id_validator = RegexValidator(
            regex='^(201[0-9]|20[2-9][0-9]|{})\\d{{8}}$'.format(current_year),
            message='ID should be a 12-digit number starting with the current year.'
        )
        
        try:
            id_validator(idd)
            user = User.objects.create_user(Username, email, password)
            etud = Etud.objects.create(username=Username, email=email, password=password, matruculation_etud=idd)
            return redirect('http://127.0.0.1:8000/conecter')
        except ValidationError:
           messages.error(request, 'Invalid ID.')
        
    return render(request, 'Login/sign up.html')




def MDADMIN(request):
   emp = Etud.objects.all()
   context = {
      'emp':emp,
   }
   return render (request,'Login\modifie admin.html',context)

def ADD(request):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      id = request.POST.get('address')
      passe = request.POST.get('phone')
      
      emp = Etud(
         username = name,
         email = email,
         matruculation_etud= id,
         password = passe,
      )
      emp.save()
      return redirect('http://127.0.0.1:8000/adminee')
   
   return render(request,'login\modifie admin.html')

def Edit(request):
   emp = Etud.objects.all()
   
   context = {
      'emp' :emp,
   }
   return redirect(request,'login\modifie admin.html',context)

def Update(request,id):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      matr = request.POST.get('address')
      passe = request.POST.get('phone')
      
      emp = Etud(
         id = id,
         username = name,
         email = email,
         matruculation_etud= matr,
         password = passe,
      )
      
      emp.save()
      return redirect('http://127.0.0.1:8000/adminee')
   
   return render(request,'Login\modifie admin.html',)

def Delete_A(request, id):
   emp = Etud.objects.filter(id=id)
   emp.delete()

   
   url_A = reverse('adminee')
   return redirect(url_A)
#cours managenment
def Manage_Cours(request):
   emp_C = Etud_Cours.objects.all()
   
   context_C = {
      'emp_C' :emp_C,
   }
   return render (request,'Login\manageCours.html',context_C)

@login_required
def ADD_C(request):
   if request.method == "POST":
      Dep = request.POST.get('dep')
      Modul= request.POST.get('mod')
      Title= request.POST.get('title')
      Descr= request.POST.get('descr')
      
   emp_C = Etud_Cours(
         Dep = Dep,
         Modul = Modul,
         description= Descr,
         title = Title,
         added_by = request.user,
      )
   emp_C.save()
   return redirect('http://127.0.0.1:8000/Mcours')



def Delete_C(request,id):
       
   emp_C = Etud_Cours.objects.filter(id = id)
   emp_C.delete()
  
   context_C = {
      'emp_C' :emp_C,
   }
   
   return redirect(request,'login\manageCours.html',context_C)
def Edit_C(request):
   emp_C = Etud_Cours.objects.all()
   
   context_C = {
      'emp_C' :emp_C,
   }
   return render(request,'login\manageCours.html',context_C)



def Update_C(request,id):
   if request.method == "POST":
      dep = request.POST.get('dep')
      modul= request.POST.get('mod')
      desc = request.POST.get('descr')
      titlee = request.POST.get('title')
      
      emp_C = Etud_Cours(
         Dep = dep,
         Modul = modul,
         description = desc,
         title= titlee,
         
      )
      
      emp_C.save()
      return redirect('http://127.0.0.1:8000/Mcours')
   
   return render(request,'login\manageCours.html',)
def Delete_C(request, id):
   emp_C= Etud_Cours.objects.get(id=id)
   emp_C.delete()

   
   url_C = reverse('course')
   return redirect(url_C)
#question management
def Manage_Question(request):
   emp_Q = Etud_Questions.objects.all()
   
   context_Q = {
      'emp_Q' :emp_Q,
   }
   return render (request,'Login\manageQuestion.html',context_Q)


@login_required
def ADD_Q(request):
   if request.method == "POST":
      Dep = request.POST.get('depp')
      Modul= request.POST.get('modd')
      Title= request.POST.get('titlee')
      Descr= request.POST.get('descrr')
      
   emp_Q = Etud_Questions(
         Depp = Dep,
         Modull = Modul,
         descriptionn= Descr,
         titlee = Title,
         added_by = request.user,
      )
   emp_Q.save()
   return redirect('http://127.0.0.1:8000/MQuestion')


def Delete_Q(request,id):
       
   emp_C = Etud_Cours.objects.filter(id = id)
   emp_C.delete()
  
   context_C = {
      'emp_C' :emp_C,
   }
   
   return redirect(request,'login\manageQuestion.html',context_C)


def Edit_Q(request):
   emp_Q = Etud_Questions.objects.all()
   
   context_Q = {
      'emp_Q' :emp_Q,
   }
   return render(request,'login\manageQuestion.html',context_Q)



def Update_Q(request,id):
   if request.method == "POST":
      dep = request.POST.get('depp')
      modul= request.POST.get('modd')
      desc = request.POST.get('descrr')
      titleee = request.POST.get('titlee')
      
      emp_Q = Etud_Questions(
         Depp = dep,
         Modull = modul,
         descriptionn = desc,
         titlee= titleee,
         
      )
      
      emp_Q.save()
      return redirect('http://127.0.0.1:8000/MQuestion')
   
   return render(request,'login\manageQuestion.html',)
#logout function
def logout_V(request):
   logout(request)
   return redirect('http://127.0.0.1:8000/conadmine')
#announce function
def Admin_An(request):
   emp_A = Admin_Ann.objects.all()
   
   context_A = {
      'emp_A' :emp_A,
   }
   return render (request,'Login\Annone.html',context_A)


@login_required
def ADD_Ann(request):
   if request.method == "POST":
      Dep_A = request.POST.get('deppA')
      Title_A= request.POST.get('titleeA')
      Descr_A= request.POST.get('descrrA')
      Link_A= request.POST.get('Link')
      
   emp_A = Admin_Ann(
         Dep_Ann= Dep_A,
         Description_Ann= Descr_A,
         title_Ann = Title_A,
         Link_Ann= Link_A,
         added_Ann = request.user,
      )
   emp_A.save()
   return redirect('http://127.0.0.1:8000/Annonce')
def Edit_Ann(request):
   emp_A = Admin_Ann.objects.all()
   
   context_A = {
      'emp_A' :emp_A,
   }
   return render(request,'login\Annone.html',context_A)
def Update_Ann (request,id):
   if request.method == "POST":
      Dep_A = request.POST.get('deppA')
      Title_A= request.POST.get('titleeA')
      Descr_A= request.POST.get('descrrA')
      Link_A= request.POST.get('Link')
      
      emp_A = Admin_Ann(
         Dep_Ann= Dep_A,
         Description_Ann= Descr_A,
         title_Ann = Title_A,
         Link_Ann= Link_A,
         
         
      )
      
      emp_A.save()
      return redirect('http://127.0.0.1:8000/Annonce')
 #delete ann
def Delete(request, id):
   emp_A = Admin_Ann.objects.filter(id=id)
   emp_A.delete()

   
   url_A = reverse('ann')
   return redirect(url_A)
   
#logout for the user   
def logout_E(request):
   logout(request)
   return redirect('http://127.0.0.1:8000/conecter')