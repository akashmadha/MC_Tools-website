from django.shortcuts import render,redirect
from .models import ConstructionTools,PavingBreaker,Specification

def index(request):
    return render(request,'index.html')

def navbar(request):
    return render(request,'Navbar/navbar.html')

def Faqpage(request):
    return render(request,'Navbar/Faqpage.html')



 
#Database IMG fetch to Decstop 
def products(request):
    pl = ConstructionTools.objects.all()
    return render(request, 'products.html', {'pl': pl})

# def Paving_Breaker(request, pb_id):
#     pl = get_object_or_404(PavingBreaker, id=pb_id)
#     return render(request, 'ConstructionTools/Paving_Breakers/PavingBreaker.html', {'pl': pl})

def pavingb_list(request):
    pb = PavingBreaker.objects.all()
    return render(request, 'ConstructionTools/Paving_Breakers/pavingb_list.html', {'pb': pb})

def PavingBreaker_Specification(request, pb_id):
    # Get the specific PavingBreaker object
    pl = get_object_or_404(PavingBreaker, id=pb_id)
    
    # Fetch specifications related to this PavingBreaker
    ps = Specification.objects.filter(paving_breaker=pl)
    
    return render(request, 'ConstructionTools/Paving_Breakers/PavingBreaker.html', {
        'pl': pl,       # Pass the selected PavingBreaker object
        'ps': ps        # Pass the related Specification objects
    })

    

from django.shortcuts import render, get_object_or_404
from .models import Product,Pro_name,Pro_SPE


def product_detail(request, pd_id):
    pd = get_object_or_404(Product, id=pd_id)
    return render(request, 'product_detail.html', {'pd': pd})

def product_list(request):
    pl = Product.objects.all()
    return render(request, 'product_list.html', {'pl': pl})





def productname(request):
    pl = Pro_name.objects.all()
    return render(request, 'product_name.html', {'pl': pl})


def productSPE(request, spe_id):
    spe = get_object_or_404(Pro_SPE, id=spe_id)
    return render(request, 'product_spe.html', {'spe': spe})



def proname(request):
    pl = Pro_name.objects.all()
    return render(request, 'pro.html', {'pl': pl})


def spe(request, spe_id):
    spe = get_object_or_404(Pro_SPE, id=spe_id)
    return render(request, 'spe.html', {'spe': spe})