from django.shortcuts import render
from pages.models import Etud_Cours
# Create your views here.
def Dep_inf(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/infou.html',contexx)

def Dep_math(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/math.html',contexx)


def Dep_st(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/st.html',contexx)

def Dep_bio(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/bio.html',contexx)


def Dep_sm(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/sm.html',contexx)

def Dep_sport(request):
    empp = Etud_Cours.objects.all()
    contexx = {
        'empiii':empp,
    }
    return render(request,'facs/sport.html',contexx)