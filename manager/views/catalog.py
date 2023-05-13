from django.shortcuts import render
from manager.models import Component,SubCategory

def home(request):
    components = Component.objects.all()
    categories = SubCategory.objects.all()
    return render(request, 'database.html',{
        'components' : components,
        'categories': categories
    })

