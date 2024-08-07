# Ex10: Тест на короткую фразу
# В рамках этой задачи с помощью pytest необходимо написать тест,
# который просит ввести в консоли любую фразу короче 15 символов.
# А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
# Запуск кода командой python -m pytest -s ex_10_short_phrase_tests.py

import pytest


def test_check_phrase_len():
    phrase = input("Введите фразу: ")
    if len(phrase) == 0:
        print('')
    assert len(phrase) < 15, f"Длина фразы {len(phrase)}. Введите фразу короче 15 символов"
