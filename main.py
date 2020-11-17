import json

import requests
import time
import hmac
import hashlib
import base64
import urllib
from urllib.parse import urlencode

kraken_secret_key = 'XWSrt1YDjsg3nh3SzeZsT+zSkA1MHaq5hjODD0ahxF5vKbw/+CHTGBhZWtmTQuFOajQa/rL4LCvA5b6we4bRAw=='
kraken_headers = {
    'API-Key': '6/oSfuiattP+tdSD4leSF11XYGHLSJgc8dcBIGgBBsNrsd68DC2K0ir8'
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


def kraken_server_time(headers, kraken_nonce=kraken_generate_nonce()):
    uri_path = '/0/public/Time'
    url = url_path + uri_path
    kraken_post_data = {
        'nonce': kraken_nonce
    }
    kraken_headers['API-Sign'] = kraken_signature(kraken_post_data, uri_path)
    response = requests.post(url, data=kraken_post_data, headers=headers)
    result = response.json()

    print(result)


def kraken_account_balance(headers):
    uri_path = '/0/private/Balance'
    url = url_path + uri_path
    kraken_post_data = {
        'nonce': kraken_generate_nonce()
    }

    kraken_headers['API-Sign'] = kraken_signature(kraken_post_data, uri_path)
    response = requests.post(url, data=kraken_post_data, headers=headers)
    result = response.json()

    print(result)


def kraken_get_tickers(headers):
    uri_path = '/0/public/Ticker'
    url = url_path + uri_path
    kraken_post_data = {
        'nonce': kraken_generate_nonce(),
        'pair': 'BCHUSD'
    }

    kraken_headers['API-Sign'] = kraken_signature(kraken_post_data, uri_path)
    response = requests.post(url, data=kraken_post_data, headers=headers)
    result = response.json()

    print(result)


def kraken_get_something(headers, uri_path, post_data):
    url = url_path + uri_path
    post_data['nonce'] = kraken_generate_nonce()
    kraken_headers['API-Sign'] = kraken_signature(post_data, uri_path)
    response = requests.post(url, data=post_data, headers=headers)
    result = response.json()

    print(result)


kraken_get_something(kraken_headers, '/0/public/Ticker', {'pair': 'BCHUSD'})
kraken_get_something(kraken_headers, '/0/public/Time', {})
# kraken_server_time(kraken_headers)
# kraken_account_balance(kraken_headers)
# kraken_get_tickers(kraken_headers)
