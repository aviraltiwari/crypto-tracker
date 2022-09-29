from django.shortcuts import render
from rest_framework import generics
from .models import CryptoCurrency
from .serializers import CryptoCurrencySerializer


class ListCryptoCurrencyView(generics.ListAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
