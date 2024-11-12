from django.urls import path
from . import views

urlpatterns = [
    path('city/<str:city>/', views.weather_function, name='city'),
]