from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def master(request):
    template = Template.objects.last()
    data = {
        'template': template,
    }
    return render(request, "master.html", data)


def Home(request):
    template = Template.objects.last()
    about = AboutContent.objects.last()
    social = Social.objects.all()
    skill = Skill.objects.all()
    certificate = Certificate.objects.all()[:3]
    portfolio = Portfolio.objects.all()[:2]

    data = {
        'template': template,
        'social': social,
        'skill': skill,
        'about': about,
        'certificate': certificate,
        "portfolio": portfolio,
        'navbar':'page1'

    }
    return render(request, "frontend/index.html", data)


def About(request):
    template = Template.objects.last()
    about = AboutContent.objects.last()
    skill = Skill.objects.all()
    education = Educataion.objects.all()
    data = {
        'template': template,
        'about': about,
        'skill': skill,
        'education': education,
        'navbar':'page2'
    }
    return render(request, "frontend/about.html", data)


def Certificate_page(request):
    template = Template.objects.last()
    certificate = Certificate.objects.all()
    data = {
        'template': template,
        'certificate': certificate,
        'navbar':'page3'
        
    }
    return render(request, "frontend/certificate.html", data)


def Portfolio_page(request):
    template = Template.objects.last()
    portfolio = Portfolio.objects.all()
    data = {
        'template': template,
        'portfolio': portfolio,
        'navbar':'page4'
    }
    return render(request, "frontend/portfolio.html", data)


def Contact_page(request):
    template = Template.objects.last()
    social = Social.objects.all()
    data = {
        'template': template,
        'social' :social,
        'navbar':'page5'
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        create = Contact(name=name, email=email, phone=phone, message=message)
        create.save()
        return redirect('/')

    return render(request, "frontend/contact.html", data)