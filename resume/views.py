from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'home':'active'}
    return render(request, 'resume/home.html',context)


def services(request):
    context = {'services':'active'}
    return render(request, 'resume/services.html',context)


def skills(request):
    context = {'skills':'active'}
    return render(request, 'resume/skills.html',context)

def contact(request):
    context = {'contact':'active'}
    return render(request, 'resume/contact.html',context)