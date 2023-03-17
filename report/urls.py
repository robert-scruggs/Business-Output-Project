from django.urls import path
from . import views

#URLConfig
#when someone travels to one of these websites, they can choose from any of these endpoints
#endpoints are linked to views which are linked to the forms
#created using path objects
urlpatterns = [
    path('', views.say_Hello),
    path('firstPage/', views.firstPage, name='firstPage'),
    path('yearOne/', views.yearOne, name='yearOne'),
    path('yearTwo/', views.yearTwo, name='yearTwo'),
    path('yearThree/', views.yearThree, name='yearThree')
]