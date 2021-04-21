from django.urls import path, include
from rest_framework import routers

'''Vytvorime default instanaci routeru'''
router = routers.DefaultRouter()

'''Pridame do urlpatterns vsechny urls z routeru'''
urlpatterns = [
    path('', include(router.urls)),
]
