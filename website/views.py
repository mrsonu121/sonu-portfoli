from django.shortcuts import render


# ==========================================================
# HOME PAGE
# URL : /
# ==========================================================

def home(request):

    return render(request, "home.html")


# ==========================================================
# ABOUT PAGE
# URL : /about/
# ==========================================================

def about(request):

    return render(request, "about.html")


# ==========================================================
# SKILLS PAGE
# URL : /skills/
# ==========================================================

def skills(request):

    return render(request, "skills.html")


# ==========================================================
# PROJECTS PAGE
# URL : /projects/
# ==========================================================

def projects(request):

    return render(request, "projects.html")


# ==========================================================
# RESUME PAGE
# URL : /resume/
# ==========================================================

def resume(request):

    return render(request, "resume.html")


# ==========================================================
# CERTIFICATES PAGE
# URL : /certificates/
# ==========================================================

def certificates(request):

    return render(request, "certificates.html")


# ==========================================================
# CONTACT PAGE
# URL : /contact/
# ==========================================================

def contact(request):

    return render(request, "contact.html")