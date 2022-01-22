from django.shortcuts import render
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import urllib.request
from .models import Crypto_detail, CryptoRates


def index(request):
    queryset = Crypto_detail.objects.all()
    return render(request, "home.html", {"queryset": queryset})


def crypto(request):
    data = get_data()
    for c_data in data["crypto_data"]:
        c_ins = Crypto_detail.objects.filter(crypto_code=c_data["symbol"]).first()
        print(c_ins)
        if c_ins:
            d = c_data['last_updated']
            CryptoRates.objects.update_or_create(
                crpto_name=c_ins,
                price_date=d.split('T')[0],
                defaults={
                    'crypto_price': int(c_data['quote']['INR']['price'])
                }
            )
    # print(data)
    return render(request, "index.html", data)
    # return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def crypto_nomic(request):
    data = get_nomic_data()
    return render(request, "crypto_nomic.html",  data)


def get_nomic_data():
    url = "https://api.nomics.com/v1/currencies/ticker?key=f5360d3109559d7c9b9f90d1369c7a705c87334c&ids=BTC,ETH,XRP,BCH,UNI,LTC,WBTC,MATIC,KSM,&interval=1d,30d&convert=INR&per-page=100&page=1"
    ret_data = dict()
    try:
        d = urllib.request.urlopen(url).read()
        ret_data["crypto_data"] = json.loads(d)
        # prints

    except Exception as e:
        print(e)
    return ret_data


# def coin_layer(request):
#     data = get_coin_data()
#     return render(request, "coin_layer.html",  data)
#
#
# def get_coin_data():
#     url = "http://api.coinlayer.com/api/live?access_key=58de3f16419f0b3e1c0de328ed44340c"
#     get_data = dict()
#
#     try:
#         d = urllib.request.urlopen(url).read()
#         get_data["coin_data"] = json.loads(d)
#         # prints
#
#     except Exception as e:
#         print(e)
#     return get_data


def get_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'INR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'bd782133-1987-4dcd-8337-9d0413fd1743',
    }

    session = Session()
    session.headers.update(headers)
    ret_data = dict()

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        ret_data["crypto_data"] = data["data"]
        # print(ret_data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:

        print(e)
        ret_data["crypto_data"] = []
    return ret_data


# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print("ejhj")
        print(e)
        data = dict()

    return data
