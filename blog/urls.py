from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),          
]