from django.shortcuts import render
from .models import Product, Watches, HomeAppliances


# Create your views here.

def products(request):
    shoe = Product.objects.all()
    watches = Watches.objects.all()
    return render(request, 'products.html', {'shoe': shoe, 'watches': watches})

def shoes(request):
    shoe = Product.objects.all()
    return render(request, 'shoes.html', {'shoe': shoe})

def sneakers(request):
    shoe = Product.objects.all()
    return render(request, 'sneakers.html', {'shoe': shoe})

def sliders(request):
    shoe = Product.objects.all()
    return render(request, 'sliders.html', {'shoe': shoe})

def football_boots(request):
    shoe = Product.objects.all()
    return render(request, 'football-boots.html', {'shoe': shoe})

def boots(request):
    shoe = Product.objects.all()
    return render(request, 'boots.html', {'shoe': shoe})

def loafers(request):
    shoe = Product.objects.all()
    return render(request, 'loafers.html', {'shoe': shoe})

def flat_shoes(request):
    shoe = Product.objects.all()
    return render(request, 'flats.html', {'shoe': shoe})

def watches(request):
    watch = Watches.objects.all()
    return render(request, 'watches.html', {'watches': watch})

def watches_men(request):
    watch = Watches.objects.all()
    return render(request, 'watches.html', {'watches': watch})

def watches_ladies(request):
    watch = Watches.objects.all()
    return render(request, 'watches.html', {'watches': watch})

def home_appliances(request):
    home_applainces = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'home_appliances': home_applainces})

def utensils(request):
    home_applainces = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'home-appliances': home_applainces})

def kitchen_ware(request):
    home_applainces = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'home-appliances': home_applainces})

def kitchen_appliances(request):
    home_applainces = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'home-appliances': home_applainces})