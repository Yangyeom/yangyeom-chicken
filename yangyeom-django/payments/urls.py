from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('pay/', views.pay, name='pay'),
    path('success/', views.success, name='success'),
]