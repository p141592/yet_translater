import os

import requests

class APIKeyException(BaseException):
    """Не указан API ключ"""

class Translate:
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    PRICE = lambda content: (len(content) / 1000000)*15
    KEY = ''

    def __init__(self, content, key=None):
        self.key = key or Translate.KEY
        self.source = content

    def get_price(self):
        return f'{Translate.PRICE(self.source)*65}'

    def translate(self):
        if not self.key:
            raise APIKeyException

        response = requests.get(
            self.URL,
            params = dict(
                key=self.key,
                text=self.source,
                lang='en-ru',
                format='plain'
            )
        )
        if response.ok:
            return response.json()

if __name__ == '__main__':
    Translate('Hello World').translate()
