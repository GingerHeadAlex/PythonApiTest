# Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ.
# Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам.
# В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще не готова,
# ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.
# Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job
# Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:
# * seconds - количество секунд, через сколько задача будет выполнена
# * token - тот самый токен, по которому можно получить результат выполнения нашей задачи
# Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:
# * error - будет только в случае, если передать token, для которого не создавалась задача.
# В этом случае в ответе будет следующая надпись - No job linked to this token
# * status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
# * result - будет только в случае, если задача готова, это поле будет содержать результат
# Наша задача - написать скрипт, который делал бы следующее:
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
# Как всегда, код нашей программы выкладываем ссылкой на комит.

import time
import json
import requests

print(f"Создаем новую задачу...")
req1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
res1 = json.loads(req1.text)
token1 = res1.get("token")
seconds1 = res1.get("seconds")


print(f"Делаем запрос с токеном до готовности задачи")
req2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": {token1}})
res2 = json.loads(req2.text)
status_before = res2.get("status")
print(f"Проверка поля статус...")
assert status_before == 'Job is NOT ready', 'Статус не соответствует "Job is NOT ready"'
print(f"Значение верное...")

for i in range(seconds1,-1,-1):
    print(f'\rЖдем готовности задачи {i} секунд', end='', flush=True)
    time.sleep(1)
print('\rЗадача готова...')

print(f"Делаем запрос с токеном по факту готовности задачи")
req3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": {token1}})
res3 = json.loads(req3.text)
status_after = res3.get("status")
print(f"Проверка поля статус...")
assert status_after == 'Job is ready', 'Статус не соответствует "Job is NOT ready"'
assert "result" in res3, 'В ответе отсутвует поле "result"'
print(f"Значение поля status верное, поле result присутствует...")
