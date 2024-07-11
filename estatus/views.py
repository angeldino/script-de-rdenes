from django.shortcuts import render

# Create your views here.
def zfEstatus(request):
    return render(request, "zfestatus.html")

def daimlerEstatus(request):
    return render(request, "daimler.html")