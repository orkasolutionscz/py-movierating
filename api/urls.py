from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet

'''Vytvorime default instanaci routeru'''
router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

'''Pridame do urlpatterns vsechny urls z routeru'''
urlpatterns = [
    path('', include(router.urls)),
]
