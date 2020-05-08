from django.urls import path
from . import views

app_name = 'store'

urlpatterns=[
    path('', views.store, name='list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<id>/', views.detail, name='detail'),

]
