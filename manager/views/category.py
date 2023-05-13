from django.shortcuts import render
from manager.models import SubCategory, Component

def home(request,id):
    category = SubCategory.objects.get(id=id)
    components = Component.objects.filter(subcategory_id=category)
    categories = SubCategory.objects.all()
    
    return render(request, "category.html", {
        "category": category,
        "components": components,
        'categories': categories
    })

def plain(request):
    categories = SubCategory.objects.all()
    return render(request, "category_plain.html",
    {
        'categories': categories
    })