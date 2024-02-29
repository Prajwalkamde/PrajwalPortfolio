from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
# Template section
class Template(models.Model):
    logo = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    footer = models.CharField(max_length=50, null=True, default="Design By ")
    footer_hero = models.CharField(max_length=50, null=True, default=full_name)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Template")
        verbose_name_plural = ("Templates")

    def __str__(self):
        return self.full_name


# Social media section
class Social(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

    class Meta:
        verbose_name = ("Social")
        verbose_name_plural = ("Socials")

    def __str__(self):
        return self.name


# Skills section
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.IntegerField()

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    def __str__(self):
        return self.skill_name


# Education section

class Educataion(models.Model):
    Choice = [
        ("Completed", "Completed"),
        ("Running", "Running"),
        ("Droped", "Droped"),
    ]
    graduation = models.CharField(max_length=100)
    year = models.IntegerField()
    course = models.CharField(max_length=200)
    complete = models.CharField(max_length=50, choices=Choice)

    class Meta:
        verbose_name = ("Educataion")
        verbose_name_plural = ("Educataions")

    def __str__(self):
        return self.graduation


# About Page section
class AboutContent(models.Model):
    image = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=100)
    greating = models.TextField()
    about_text = RichTextField()
    resume = models.FileField(upload_to="resume/", max_length=500)

    class Meta:
        verbose_name = ("AboutContent")
        verbose_name_plural = ("AboutContents")

    def __str__(self):
        return self.name


# Certificate section
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="certificate/")

    class Meta:
        verbose_name = ("Certificate")
        verbose_name_plural = ("Certificates")

    def __str__(self):
        return self.name


# Portfolio Section
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/")
    project_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolios")

    def __str__(self):
        return self.project_name


# Contact section
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name
