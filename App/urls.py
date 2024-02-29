from django.urls import path
from .views import *

urlpatterns = [
    path("",Home,name="home"),
    path("about/",About,name="about"),
    path("certificate/",Certificate_page,name="certificate"),
    path("portfolio/",Portfolio_page,name="portfolio"),
    path("contact",Contact_page,name="contact"),
]