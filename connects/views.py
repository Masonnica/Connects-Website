from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def tools(request):
    return render(request, 'tools.html')

def library(request):
    return render(request, 'library.html')

def documents(request):
    return render(request, 'documents.html')
