# Интерфейс для перевода через Yandex Translate API

Получить ключ тут: https://translate.yandex.ru/developers/keys

Пример:

    In [1]: from main import Translate as T
    
    In [2]: t = T('hello world', key='trnsl.1.1.20190815T224810Z.6a200a0ae36976a0.add72ad00ac7bd0463d227d57446b55a96a82535')
    
    In [3]: t.get_price()
    Out[3]: '0.010725'
    
    In [4]: t.translate()
    Out[4]: {'code': 200, 'lang': 'en-ru', 'text': ['Привет мир']}