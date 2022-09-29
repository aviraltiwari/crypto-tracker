from django.db import models


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    change_percentage_1h = models.CharField(max_length=100)
    change_percentage_2h = models.CharField(max_length=100)
    change_percentage_7d = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    supply = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
