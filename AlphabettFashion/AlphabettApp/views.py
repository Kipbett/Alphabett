from django.shortcuts import render

from .models import Product, Watches, HomeAppliances


# Create your views here.

def products(request):
    shoe = Product.objects.all()
    watches = Watches.objects.all()
    homeappliances = HomeAppliances.objects.all()
    return render(request, 'products.html', {'shoe': shoe, 'watches': watches, 'home_appliances': homeappliances})

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
    homeappliances = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'home_appliances': homeappliances})

def utensils(request):
    utensil = HomeAppliances.objects.all()
    return render(request, 'utensils.html', {'utensils': utensil})

def kitchen_ware(request):
    kitcheware = HomeAppliances.objects.all()
    return render(request, 'kitchen-ware.html', {'kitchen_ware': kitcheware})

def kitchen_appliances(request):
    kitchenapplainces = HomeAppliances.objects.all()
    return render(request, 'home-appliances.html', {'kitchen_appliances': kitchenapplainces})