from django.shortcuts import render

# Create your views here.

def hindex(request):
    return render(request,'health/hindex.html')

def Medial(request):
    return render(request,'health/madical.html')

def Consmatic(request):
    return render(request,'health/consmatic.html')