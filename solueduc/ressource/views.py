from django.shortcuts import render, redirect
from .models import Cours, Type
from django.views import generic


def index(request):
    
    return render(request, 'dashboard/index.html')

def formations(request):
    cours = Cours.objects.all().order_by('libelle')
    return render(request, 'dashboard/formations.html', {"cours":cours})


def views_formation(request, cour_id):
	cour = Cours.objects.get(pk=cour_id)
	return render(request, 'dashboard/view_formation.html', {
		'cour': cour,
	})


def views_type(request):
	types = Type.objects.all()
	return render(request, 'dashboard/type.html', {
		'types': types,
	})

    
    

##def mere_list(request):
#	meres = Mere.objects.all().order_by('nom')
#	return render(request, 'naissances/mere_list.html', {'meres': meres})

def orientations(request):
    
    return render(request, 'dashboard/orientations.html')

def forums(request):
    
    return render(request, 'dashboard/forums.html')

def activites(request):
    
    return render(request, 'dashboard/activites.html')