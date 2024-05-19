from django.urls import path
from .views import index, about, services, price, contacts, reg, auth, logoutuser, panel, zap

urlpatterns = [
    path('', index),
    path('about', about),
    path('services', services),
    path('price', price),
    path('contacts', contacts),
    path('reg', reg),
    path('auth', auth),
    path('logoutuser', logoutuser),
    path('panel', panel),
    path('zap', zap)
]


