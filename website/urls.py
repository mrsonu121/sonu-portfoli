from django.urls import path                  # path() function import kiya
from . import views                           # website app ki views.py import ki


urlpatterns = [

    # ================= HOME PAGE =================

    path("", views.home, name="home"),


    # ================= ABOUT PAGE =================

    path("about/", views.about, name="about"),


    # ================= SKILLS PAGE =================

    path("skills/", views.skills, name="skills"),


    # ================= PROJECTS PAGE =================

    path("projects/", views.projects, name="projects"),


    # ================= RESUME PAGE =================

    path("resume/", views.resume, name="resume"),


    # ================= CERTIFICATES PAGE =================

    path("certificates/", views.certificates, name="certificates"),


    # ================= CONTACT PAGE =================

    path("contact/", views.contact, name="contact"),

]