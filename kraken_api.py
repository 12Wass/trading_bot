import requests
import pandas
import json
import time
import hmac
import hashlib
import base64
from pathlib import Path
import urllib
from urllib.parse import urlencode

kraken_secret_key = ''
kraken_headers = {
    'API-Key': ''
}
url_path = 'https://api.kraken.com'


def kraken_generate_nonce():
    return str(int(time.time() * 1000))


def kraken_signature(post_data, uri_path):
    url_encoded_post_data = urllib.parse.urlencode(post_data)
    encoded = (str(post_data['nonce']) + url_encoded_post_data).encode()

    message = uri_path.encode() + hashlib.sha256(encoded).digest()
    kraken_signed = hmac.new(base64.b64decode(kraken_secret_key), message, hashlib.sha512)
    kraken_signature_digest = base64.b64encode(kraken_signed.digest())
    return kraken_signature_digest


def kraken_get_something(headers, uri_path, post_data):
    url = url_path + uri_path
    post_data['nonce'] = kraken_generate_nonce()
    kraken_headers['API-Sign'] = kraken_signature(post_data, uri_path)
    response = requests.post(url, data=post_data, headers=headers)
    result = response.json()
    return result


def get_asset_pairs():
    asset_pairs = kraken_get_something(kraken_headers, '/0/public/AssetPairs', {})
    asset_pairs_string = ','.join(str(v) for v in asset_pairs['result'].keys())
    return asset_pairs_string


def kraken_parse_result(result):
    if result:
        print(result['result']['unixtime'])


def kraken_save_tickers():  # Rajouter la date de création du fichier Tickers
    tickers_path = Path("/tickers.json")
    if tickers_path.is_file():
        type_open = "x"
    else:
        type_open = "w"

    f = open('tickers.json', type_open)
    f.write(json.dumps(kraken_get_something(kraken_headers, '/0/public/Ticker', {'pair': get_asset_pairs()})['result']))
    f.close()


def kraken_trading_bot():
    while 1:
        print('Welcome to the Kraken Trading Bot')
        print('Checking for open orders')
        isOrders = kraken_get_something(kraken_headers, '/0/private/OpenOrders', {})
        if not len(isOrders['result']['open']):
            print('No orders -> Submitting new order')


# Private
# kraken_get_something(kraken_headers, '/0/private/Balance', {}) -> Balance de notre compte (tous cryptoactifs)
# kraken_get_something(kraken_headers, '/0/private/OpenOrders', {}) -> Ordres ouverts / en attente

# Public
# kraken_get_something(kraken_headers, '/0/public/Ticker', {'pair': get_asset_pairs()}) -> Tous les tickers
# kraken_get_something(kraken_headers, '/0/public/Time', {}) -> Récupérer le temps serveur Kraken
