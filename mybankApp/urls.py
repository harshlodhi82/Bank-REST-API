from django.urls import path
from .models import Bank
from .views import MyBankGetByIFSC, MyBGetByCityName, bankView
urlpatterns = [
    path('', bankView, name = 'Home'),
    path('bank/', MyBankGetByIFSC.as_view(), name = 'Bank'),
    path('bankinfo/', MyBGetByCityName.as_view(), name = 'BankInfo')
]