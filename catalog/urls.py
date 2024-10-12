from django.urls import path

from . import views


app_name = 'app_catalog'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('home/', views.home, name='home'),
]