from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['logo', 'full_name', 'phone', 'email', 'footer', 'footer_hero', 'date']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'link']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'skill_percentage']


@admin.register(Educataion)
class EducataionAdmin(admin.ModelAdmin):
    list_display = ['graduation', 'year', 'course', 'complete']


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['id','image', 'name', 'about_text', 'resume', ]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['image', 'project_name', 'description', 'link']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']







