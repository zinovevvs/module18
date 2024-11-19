from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/', views.games_view, name='games'),
    path('cart/', views.cart_view, name='cart'),
]
