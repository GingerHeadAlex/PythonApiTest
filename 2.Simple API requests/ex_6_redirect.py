# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
# С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.

import requests
import json

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count_redirect = response.history
final_url = response.url
print(f"Количество редиректов: {len(count_redirect)}\nИтоговый URL: {final_url}")
