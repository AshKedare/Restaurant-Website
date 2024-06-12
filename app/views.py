from django.shortcuts import render
from django.http import HttpResponse
from app.models import Menu_category
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def menu(request):
    categories = []
    menu_items = Menu_category.objects.all()
    for items in menu_items: 
        categories.append(items)
    print(categories)
    return render(request, 'app/menu.html', {'categories': categories, 'range':range(0,2) } )

def contact(request):
    return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')