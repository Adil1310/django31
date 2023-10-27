from django.urls import path
from . import views

urlpatterns = [
    path('', views.cancel_transaction, name='cancel_transaction'),
]