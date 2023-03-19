from django.urls import path
from . import views

#URLConfig
#when someone travels to one of these websites, they can choose from any of these endpoints
#endpoints are linked to views which are linked to the forms
#created using path objects

# first column: which endpoint you are working on
# second column: which method from views you will use


urlpatterns = [
    path('', views.firstPage),
    path('yearOne/', views.yearOne),
    path('yearTwo/', views.yearTwo),
    path('yearThree/', views.yearThree),
    path('success/', views.success)
    

]