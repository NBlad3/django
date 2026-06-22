from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('copy/<name>', views.copy, name='copy'),
    path('copy2/<int:age>', views.copy2, name='copy2'),
    path('points/<int:math>/<int:english>/<int:physics>/', views.points, name='points'),
    path('numbers/<int:nums>', views.numbers, name='numbers')
]