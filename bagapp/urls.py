from django.urls import path
from bagapp import views

urlpatterns = [
path('',views.index),
path('about/',views.about),
path('coming/',views.coming),
path('contact/',views.contact),
path('login/',views.login),
path('register/',views.register),
path('shop/',views.shop),
path('single/',views.single),



]