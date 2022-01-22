from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Crypto_detail(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='crypto_pics')
    crypto_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_date = models.DateField(null=True, blank=True)
    crypto_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class CryptoRates(models.Model):
    crpto_name = models.ForeignKey(Crypto_detail, on_delete=models.CASCADE)
    crypto_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_date = models.DateField(null=True, blank=True)

