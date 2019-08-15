# Интерфейс для перевода через Yandex Translate API

Пример:

    In [1]: from main import Translate as T
    
    In [2]: t = T('hello world')
    
    In [3]: t.translate()
    Out[3]: {'code': 200, 'lang': 'en-ru', 'text': ['Привет мир']}