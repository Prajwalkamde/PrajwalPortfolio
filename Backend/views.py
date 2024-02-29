from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from App.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.

def Backend(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]
        messages.add_message(request,messages.SUCCESS,"Wellcome, Prajwal 😎.")

        data = {
            "template": template,
            "mess":mess,
        }
        return render(request, "backend/template_add.html", data)
    else:
        return redirect('login')


# Template section
def SiteAdd(request):

    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            logo = request.POST['logo']
            fullname = request.POST['fullname']
            phone = request.POST['phone']
            email = request.POST['email']
            footer = request.POST['footer']
            add = Template(logo=logo, full_name=fullname, phone=phone, email=email, footer=footer)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("site-show")

        return render(request, "backend/template_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')


def SiteShow(request):
    if request.user.is_authenticated:
        show = Template.objects.all()[::-1]
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,

        }
        return render(request, "backend/template_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def SiteUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = Template.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.logo = request.POST['logo']
            update.fullname = request.POST['fullname']
            update.phone = request.POST['phone']
            update.email = request.POST['email']
            update.footer = request.POST['footer']
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("site-show")

        return render(request, "backend/template_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')


def SiteDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Template.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("site-show")
        return render(request, "backend/template_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# Skill Section

def SkillAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]
        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            skill_name = request.POST['skill_name']
            skill_percentage = request.POST['skill_percentage']

            add = Skill(skill_name=skill_name, skill_percentage=skill_percentage)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("skill-show")

        return render(request, "backend/skill_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def SkillShow(request):
    if request.user.is_authenticated:
        show = Skill.objects.all()[::-1]
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,

        }
        return render(request, "backend/skill_show.html", data)
    else:
        return redirect('/')

def SkillUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = Skill.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.skill_name = request.POST['skill_name']
            update.skill_percentage = request.POST['skill_percentage']
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("skill-show")

        return render(request, "backend/skill_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def SkillDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Skill.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("skill-show")

        return render(request, "backend/skill_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# Social Media Section

def SocialAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess
        }
        if request.method == "POST":
            name = request.POST['name']
            icon = request.POST['icon']
            link = request.POST['link']

            add = Social(name=name, icon=icon, link=link)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("social-show")

        return render(request, "backend/social_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def SocialShow(request):
    if request.user.is_authenticated:
        show = Social.objects.all()[::-1]
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,

        }
        return render(request, "backend/social_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def SocialUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = Social.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.name = request.POST['name']
            update.icon = request.POST['icon']
            update.link = request.POST['link']
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("social-show")

        return render(request, "backend/social_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')
def SocialDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Social.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("social-show")

        return render(request, "backend/social_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# Portfolio Section
def PortfolioAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            image = request.FILES.get('image')
            project_name = request.POST['project_name']
            description = request.POST['description']
            link = request.POST['link']

            add = Portfolio(image=image, project_name=project_name, description=description, link=link)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("portfolio-show")

        return render(request, "backend/portfolio_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def PortfolioShow(request):
    if request.user.is_authenticated:
        show = Portfolio.objects.all()
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,

        }
        return render(request, "backend/portfolio_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def PortfolioUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        update = Portfolio.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess

        }
        if request.method == "POST":
            update.image = request.FILES.get('image')
            update.project_name = request.POST['project_name']
            update.description = request.POST['description']
            update.link = request.POST['link']
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("portfolio-show")

        return render(request, "backend/portfolio_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def PortfolioDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Portfolio.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("portfolio-show")

        return render(request, "backend/portfolio_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# Eduction Section

def EducationAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            graduation = request.POST['graduation']
            year = request.POST['year']
            course = request.POST['course']
            complete = request.POST['dropdown']

            add = Educataion(graduation=graduation, year=year, course=course, complete=complete)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("education-show")

        return render(request, "backend/education_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def EducationShow(request):
    if request.user.is_authenticated:
        show = Educataion.objects.all()
        template = Template.objects.last()
        mess = Contact.objects.all()[3:0:-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,

        }
        return render(request, "backend/education_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def EducationUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = Educataion.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.graduation = request.POST['graduation']
            update.year = request.POST['year']
            update.course = request.POST['course']
            update.complete = request.POST['dropdown']
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("education-show")

        return render(request, "backend/education_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def EducationDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Educataion.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("education-show")

        return render(request, "backend/education_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# Certificate Section
def CertificateAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            name = request.POST['name']
            image = request.FILES.get('image')

            add = Certificate(name=name, image=image)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("certificate-show")

        return render(request, "backend/certificate_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def CertificateShow(request):
    if request.user.is_authenticated:
        show = Certificate.objects.all()
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        data = {
            'show': show,
            "template": template,
            'mess':mess,
        }
        return render(request, "backend/certificate_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def CertificateUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = Certificate.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.name = request.POST['name']
            update.image = request.FILES.get('image')
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("certificate-show")

        return render(request, "backend/certificate_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def CertificateDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = Certificate.objects.get(id=id)
            delete.delete()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("certificate-show")
        return render(request, "backend/certificate_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

# About Section
def AboutAdd(request):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            "template": template,
            'mess':mess,
        }
        if request.method == "POST":
            image = request.FILES.get('image')
            name = request.POST['name']
            greating = request.POST['greating']
            about_text = request.POST['about_text']
            resume = request.FILES.get('resume')

            add = AboutContent(image=image, name=name, greating=greating, about_text=about_text, resume=resume)
            add.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Added Successfully.")
            return redirect("about-show")
        return render(request, "backend/about_add.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def AboutShow(request):
    if request.user.is_authenticated:
        show = AboutContent.objects.all()[::-1]
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            'show': show,
            "template": template,
            'mess':mess,
        }
        return render(request, "backend/about_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')

def AboutUpdate(request, id):
    if request.user.is_authenticated:
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]


        update = AboutContent.objects.get(id=id)
        data = {
            'update': update,
            "template": template,
            'mess':mess,

        }
        if request.method == "POST":
            update.image = request.FILES.get('image')
            update.name = request.POST['name']
            update.greating = request.POST['greating']
            update.about_text = request.POST['about_text']
            update.resume = request.FILES.get('resume')
            update.save()
            messages.add_message(request, messages.SUCCESS, "Data Has Been Updated Successfully.")
            return redirect("about-show")
        return render(request, "backend/about_update.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')


def AboutDelete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            delete = AboutContent.objects.get(id=id)
            delete.delete()

            messages.add_message(request, messages.SUCCESS, "Data Has Been Deleted Successfully.")
            return redirect("about-show")
        return render(request, "backend/about_show.html")
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')


# Contact Section
def ContactShow(request):
    if request.user.is_authenticated:
        show = Contact.objects.all()[::-1]
        template = Template.objects.last()
        mess = Contact.objects.all()[3::-1]

        data = {
            'show': show,
            'template': template,
            'mess':mess,
        }
        return render(request, "backend/contact_show.html", data)
    else:
        messages.add_message(request, messages.WARNING, "Operation Is Invalid.")
        return redirect('/')


def LoginPage(request):
    if request.method =="POST":
        user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            return redirect("backend")
        else:
            return redirect("login")
    return render(request,"login.html")


def LogOut(request):
    logout(request)
    if logout:
        return HttpResponseRedirect("login")