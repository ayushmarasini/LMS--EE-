from django.urls import path,include
from .views import catalog, teams, item ,category

urlpatterns = [
    path('', catalog.home ,name='home') ,
    path('teams/', teams.home ,name='teams') ,
    path('component/<int:id>/', item.home ,name='component'),    
    path('categories/<int:id>/', category.home ,name='category')    ,
    path('categories/', category.plain ,name='category')    
] 