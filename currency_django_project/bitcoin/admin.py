from django.contrib import admin
from .models import Crypto_detail, CryptoRates
from django.contrib import admin


class CryptoRatesAdmin(admin.ModelAdmin):
    list_display = ('crpto_name', 'crypto_price', 'price_date')


class CryptoDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'crypto_code')


admin.site.register(Crypto_detail, CryptoDetailsAdmin)
admin.site.register(CryptoRates, CryptoRatesAdmin)


