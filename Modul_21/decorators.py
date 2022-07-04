import json
import pytest
import requests
import os
from nikname import email, password
@pytest.fixture(scope="class")
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен успешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')

@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\Запущен тест из сьюта Дом питомца.{request.function.__name__}")

def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен успешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
