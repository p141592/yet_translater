import os

import requests

class Translate:
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = ''
    PRICE = lambda content: (len(content) / 1000000)*15

    def __init__(self, content):
        self.source = content

    def get_price(self):
        return f'{Translate.PRICE(self.source)*65}'

    def translate(self):
        response = requests.get(
            self.URL,
            params = dict(
                key=self.KEY,
                text=self.source,
                lang='en-ru',
                format='plain'
            )
        )
        if response.ok:
            return response.json()

if __name__ == '__main__':
    Translate('Hello World').translate()
