from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio_view, name='inicio_view'),
    path('Acerca de/', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
]