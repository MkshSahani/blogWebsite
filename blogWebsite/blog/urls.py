from django.urls import path

from . import views # get the views,  

urlpatterns = [
    path('', views.HomeRender, name = 'Home'), 
]   
