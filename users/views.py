from distutils import text_file
import imp
from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from .forms import formprof
from .models import Professeur
# Create your views here.


def formprof1(request):
    if request.method=="POST":
        prof_form=formprof(request.POST)
        if prof_form.is_valid():
            prof_form.save()
            prof_form=formprof()
            messages.success(request, f'Your Account Has Been Created ')
    return render(request, 'users/formprof1.html', {"prof_form": formprof})


def formprof2(request):
    if request.method=="POST":
        var_prenom = request.POST.get('prenom')
        var_nom = request.POST.get('nom')
        var_mail = request.POST.get('email')
        var_contact = request.POST.get('contact_prof')
        var_date_d_adhesion = request.POST.get('date_d_adhesion')
        var_chef_departement = request.POST.get('chef_departement')
        if var_chef_departement==None:
            var_chef_departement=False
        print(var_prenom,var_nom, var_mail, var_contact, var_date_d_adhesion, var_chef_departement)
        Professeur.objects.create(prenom=var_prenom,nom=var_nom,email=var_mail,contact_prof=var_contact,date_d_adhesion=var_date_d_adhesion, chef_departement=var_chef_departement)
        messages.success(request, f'Your Account Has Been Created ')
    return render(request, "users/formprof2.html")