# Тест запроса на метод cookie
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie.
# Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print()
# понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert.

import requests

def test_check_cookie():
    req1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    cookie = dict(req1.cookies)
    assert req1.status_code == 200, "Wrong status code"
    assert cookie["HomeWork"] == "hw_value", "Wrong cookie"
