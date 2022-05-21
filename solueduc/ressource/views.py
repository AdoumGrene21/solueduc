from django.shortcuts import render, redirect


def index(request):
    
    return render(request, 'dashboard/index.html')

def formations(request):
    
    return render(request, 'dashboard/formations.html')

def orientations(request):
    
    return render(request, 'dashboard/orientations.html')

def forums(request):
    
    return render(request, 'dashboard/forums.html')

def activites(request):
    
    return render(request, 'dashboard/activites.html')