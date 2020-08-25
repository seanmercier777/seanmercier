from django.shortcuts import render







def index(request):
    return render(request, "index.html", {"context" : "index"})

def cv(request):
    return render(request, "cv.html", {"context" : "cv"})

def projects(request):
    return render(request, "projects.html", {"context" : "projects"})

def contact(request):
    return render(request, "contact.html", {"context" : "contact"})