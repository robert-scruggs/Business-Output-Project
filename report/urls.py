from django.urls import path
from . import views

#URLConfig
#when someone travels to the website, they can choose from any of these endpoints
#endpoints are linked to views which are linked to the forms
#created using path objects

# first column: which endpoint you are working on
# second column: which method from views you will use

#think of these mfs like rooms!!!!!!!!!!!!!!!!!!!!!!!!!
#create the rooms and then run a function to tell system what to show and do in room


urlpatterns = [
    path('', views.register),
    path('basicInformation/', views.basicInformation),
    path('yearOne/', views.yearOne),
    path('yearTwo/', views.yearTwo),
    path('yearThree/', views.yearThree),
    path('taxyears/', views.taxYears),
    path('success/', views.success),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('files/', views.files),
    path('report/', views.report)
]


