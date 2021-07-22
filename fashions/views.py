from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'fashions/index.html')

def shoes(request):
    return render(request,'fashions/shoes.html')
