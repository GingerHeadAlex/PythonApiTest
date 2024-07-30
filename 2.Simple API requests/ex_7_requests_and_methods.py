# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос.
# Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’.
# И так далее.
# Надо написать скрипт, который делает следующее:
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=

import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

req1 = requests.request('get', url)
print(f"1)Ответ сервера, без параметра method в запросе: {req1.text}\nСтатус код {req1.status_code}\n")

payload = {"method": "GET"}
req2 = requests.request('head', url, params = payload)
print(f"2)Ответ сервера, на запрос с невалидным параметром: {req2.text}\nСтатус код {req2.status_code}\n")

payload = {"method": "GET"}
req3 = requests.request('get', url, params = payload)
print(f"3)Ответ сервера, на запрос с валидным параметром: {req3.text}\nСтатус код {req3.status_code}\n")

http_methods = {"POST", "GET", "PUT", "DELETE"}
count = 4
for r in http_methods:
    if r != 'GET':
        req = requests.request(r, url, data={"method": r})
        print(f"{count})Ответ сервера, на {r} запрос: {req.text}\nСтатус код {req.status_code}\n")
        count += 1
    else:
        req = requests.request(r, url, params={"method": r})
        print(f"{count})Ответ сервера, на {r} запрос: {req.text}\nСтатус код {req.status_code}\n")
