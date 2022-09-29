from dataclasses import field
from rest_framework import serializers
from .models import CryptoCurrency


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = [
            'name',
            'price',
            'change_percentage_1h',
            'change_percentage_2h',
            'change_percentage_7d',
            'market_cap',
            'volume',
            'supply',
        ]
