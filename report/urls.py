from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('', views.say_Hello),
    path('firstPage/', views.firstPage, name='firstPage'),
    path('yearOne/', views.yearOne, name='yearOne')
]