from django.urls import path
from .views import *

urlpatterns = [
    path("", Backend, name="backend"),
#     Login Page
    path("login",LoginPage,name="login"),
#     Logout Page
    path("logout",LogOut,name="logout"),
    # Template Section
    path("site-add", SiteAdd, name="site-add"),
    path("site-show", SiteShow, name="site-show"),
    path("site-update/<int:id>", SiteUpdate, name="site-update"),
    path("site-delete/<int:id>", SiteDelete, name="site-delete"),
    # Skill Section
    path("skill-add", SkillAdd, name="skill-add"),
    path("skill-show", SkillShow, name="skill-show"),
    path("skill-update/<int:id>", SkillUpdate, name="skill-update"),
    path("skill-delete/<int:id>", SkillDelete, name="skill-delete"),

    # Social Media Section
    path("social-add", SocialAdd, name="social-add"),
    path("social-show", SocialShow, name="social-show"),
    path("social-update/<int:id>", SocialUpdate, name="social-update"),
    path("social-delete/<int:id>", SocialDelete, name="social-delete"),

    # Portfolio Section
    path("portfolio-add", PortfolioAdd, name="portfolio-add"),
    path("portfolio-show", PortfolioShow, name="portfolio-show"),
    path("portfolio-update/<int:id>", PortfolioUpdate, name="portfolio-update"),
    path("portfolio-delete/<int:id>", PortfolioDelete, name="portfolio-delete"),

    # Education Section
    path("education-add", EducationAdd, name="education-add"),
    path("education-show", EducationShow, name="education-show"),
    path("education-update/<int:id>", EducationUpdate, name="education-update"),
    path("education-delete/<int:id>", EducationDelete, name="education-delete"),

    # Certificate Section
    path("certificate-add", CertificateAdd, name="certificate-add"),
    path("certificate-show", CertificateShow, name="certificate-show"),
    path("certificate-update/<int:id>", CertificateUpdate, name="certificate-update"),
    path("certificate-delete/<int:id>", CertificateDelete, name="certificate-delete"),

    # About Section
    path("about-add", AboutAdd, name="about-add"),
    path("about-show", AboutShow, name="about-show"),
    path("about-update/<int:id>", AboutUpdate, name="about-update"),
    path("about-delete/<int:id>", AboutDelete, name="about-delete"),

    # Conatct Section
    path("contact-show", ContactShow, name="contact-show"),


]