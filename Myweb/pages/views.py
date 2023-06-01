from django.shortcuts import render,redirect
from pages.models import Etud_Cours,Etud_Questions,Comment,Admin_Ann
from django.contrib.auth.decorators import login_required
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from django.contrib import messages
from .descriptions import *
from Login.models import Etud
from django.core.mail import send_mail
from Myweb import settings
# Create your views here.

#     **** phrase cleaners ****
def clean_phrase(phrase):
    # Convert the phrase to lowercase
    phrase = phrase.lower()

    # na7i punctuation marks
    import re
    phrase = re.sub(r'[^\w\s\-\'_]', '', phrase)

    # Split  ll la phrase
    words = phrase.split()

    # na7i articles 
    stopwords = ['a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'yet', 'so',
                 'at', 'by', 'in', 'of', 'on', 'to', 'up', 'with','contains', 'good','a loot','course']
    keywords = [word for word in words if word not in stopwords]

    
    return ' '.join(keywords)

def Home(request):
    return render(request, 'home.html')

@login_required(login_url='http://127.0.0.1:8000/conecter')
def Cours(request):
    try:
        emp = Etud_Cours.objects.all()
        context = {
        'emp':emp,
        }
        return render(request,'des\Cours.html',context)
    except:
        return redirect('http://127.0.0.1:8000/conecter')

@login_required(login_url='http://127.0.0.1:8000/conecter')
def Question(request):
    try :
        empp = Etud_Questions.objects.all()
        contex = {
        'empii':empp,
        }
        return render(request,'des\Question.html',contex)
    except:
        return redirect('http://127.0.0.1:8000/conecter')


@login_required(login_url='http://127.0.0.1:8000/conecter')
def AddQuest(request):
    
    if request.method == "POST":
        Departt = request.POST.get('name1')
        Modulee = request.POST.get('name2')
        descriptionn = request.POST.get('name3')
        titlee = request.POST.get('name4')
        image = request.FILES.get('name5')
        user = request.user
        
        addQQ =  Etud_Questions(
        Depp = Departt,
        Modull = Modulee,
        descriptionn = descriptionn,
        titlee =titlee,
        image = image,
        added_by=user,
    )
        addQQ.save()
        return redirect('http://127.0.0.1:8000/question')
    
    return render(request,'des/add Question.html')



#add cours "with WORDNET test " functionality
@login_required()
def AddCours(request):
    
    if request.method == "POST":
        depart = request.POST.get('depart')
        module = request.POST.get('Module')
        description = request.POST.get('description')
        title = request.POST.get('title')
        link = request.POST.get('file')
        user = request.user  # get the current user
        my_description = ""

        # Use switch beh na3rfou dep 
        switch = {
            'infourmatique': inf_description ,
            'biologie': bio_description ,
            'sionce et tech': st_description ,
            'math': math_description,
            'sionce mathier': sm_description ,
            'sport': sport_description ,
            
        }
        my_description = switch.get(depart, '')

        # Clean phrase 
        cleaned_my_description = clean_phrase(my_description)
        cleaned_description = clean_phrase(description)

        # Tokenize the phrases 
        my_description_words = word_tokenize(cleaned_my_description)
        description_words = word_tokenize(cleaned_description)

        # Load WordNet 
        nltk.download('wordnet')

        # Lemmatize the words 
        lemmatizer = WordNetLemmatizer()
        my_description_words = [lemmatizer.lemmatize(word) for word in my_description_words]
        description_words = [lemmatizer.lemmatize(word) for word in description_words]

        # Calculate similarity 
        sim_score = len(set(my_description_words).intersection(set(description_words))) / \
                    len(set(my_description_words).union(set(description_words)))

        if sim_score >= 0.1:
            # save the cours
            adder =  Etud_Cours(
                Dep=depart,
                Modul=module,
                description=description,
                title=title,
                link=link,
                added_by=user,
            )
            adder.save()

            
            return redirect('http://127.0.0.1:8000/cours')
        else:
            
            messages.error(request, 'Invalide discriptions')
    
    
    return render(request,'des/add Cours.html')


#commentes function
@login_required(login_url='http://127.0.0.1:8000/conecter')
def Comments(request,id):
    # Get the Etud_Questions bl ID
    repons = Etud_Questions.objects.filter(id=id).first()

    if request.method == 'POST':
        # If the user submitted the comment form
        name = request.user.username
        content = request.POST.get('comment_box')
        #Comment.objects.create(post=repons, name=name, content=content)
        adderX =  Comment(
            post=repons,
            name=name,
            content=content
        )
        adderX.save()

        # Redirect the user back to the comments page
        return redirect('comments', id=id)

    # If the user didn't submit the comment form, show the comments page
    comment = Comment.objects.filter(post_id=id)
    fadi = {
        'fadii': repons, 
        'Comment': comment
    }
    return render(request, 'des/comments.html', fadi)
#contact function
def Contact(request):
    return render(request,'des/contact.html')
#dep page function
def Dep(request):
    return render(request,'des/Dipartement.html')
#profiles of departement function
def Profdep(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    
    return render(request,'des/profil Dipartement.html',contexx)
#profiles function
@login_required(login_url='http://127.0.0.1:8000/conecter')
def profile(request):
    try:
        user = request.user
        context = {
            'cnx': user.username,
        }
        return render(request, 'des/profile.html', context)
    except:
        return redirect('http://127.0.0.1:8000/conecter')



# search functions cours
def scrh(request):
    srch = Etud_Cours.objects.all()
    title = None
    if 'search_box' in request.GET:
        title = request.GET['search_box']
        if title:
            srch = srch.filter(title__icontains=title)
    
    
    
    
    emp = srch
    context = {
      'emp':emp,
   }
    return render(request,'des/srchCours.html',context)

#shcred Question
def Question_scrh(request):
    srchQ = Etud_Questions.objects.all()
    titlee = None
    if 'search_boxQ' in request.GET:
        titlee = request.GET['search_boxQ']
        if titlee:
            srchQ = srchQ.filter(titlee__icontains=titlee)
    
    
    
    
    empQ = srchQ
    contextQ = {
      'empQ':empQ,
   }
    return render(request,'des/scrchQuetsion.html',contextQ)
#annonce page
def Admin_An(request):
    emp_a = Admin_Ann.objects.all()
    context_a = {
      'emp_a':emp_a,
   }
    return render(request,'des/annoncement.html',context_a)

def update_profile(request):
    if request.method == "POST":
        email = request.POST.get('email')
        matrecule= request.POST.get('matrecule')
        passeword = request.POST.get('passeword')
        passeword1= request.POST.get('passeword1')
      
        emp = Etud(
         username = "Fadi",
         email = email,
         matruculation_etud = matrecule,
         password  = passeword ,
         password1 = passeword1 
         
      )
      
        emp.save()
        return redirect('http://127.0.0.1:8000/profile')
    
    return render(request,'des/update.html')
#CONTACT PAGE 
def send_message(request):
      
  if request.method == 'POST':
       subject = request.POST['subject']
       email = request.POST['email']
       message = request.POST['message']
       
  send_mail(
       subject,
       message,
       settings.EMAIL_HOST_USER,
       [email],
  )
       
  return render(request,'des/contact.html')