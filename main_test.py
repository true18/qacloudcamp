import requests
import pytest


class SimpleAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_posts(self, filters=None):
        return requests.get(f'{self.api_url}/posts', params=filters)

    def add_post(self, post_info):
        return requests.post(f'{self.api_url}/posts', json=post_info)

    def remove_post(self, post_identifier):
        return requests.delete(f'{self.api_url}/posts/{post_identifier}')


# Фикстура для создания клиента API
@pytest.fixture
def client():
    return SimpleAPIClient('https://jsonplaceholder.typicode.com')


# Тесты для метода GET /posts

def test_retrieval_of_posts_with_userId(client):
    resp = client.fetch_posts({'userId': 2})
    assert resp.status_code == 200
    assert all(item['userId'] == 2 for item in resp.json())


def test_retrieval_of_posts_with_invalid_userId(client):
    resp = client.fetch_posts({'userId': 'invalid'})
    assert resp.status_code == 200
    assert not resp.json()


# Тесты для метода POST /posts

def test_post_addition_with_valid_data(client):
    post_data = {'title': 'test title', 'body': 'test body', 'userId': 1}
    resp = client.add_post(post_data)
    assert resp.status_code == 201
    assert resp.json()['title'] == 'test title'


def test_post_addition_with_missing_data(client):
    post_data = {'title': 'test title'}
    resp = client.add_post(post_data)
    assert resp.status_code == 201
    assert 'id' in resp.json()


# Тесты для метода DELETE /posts

def test_post_deletion_with_valid_id(client):
    resp = client.remove_post(1)
    assert resp.status_code == 200


def test_post_deletion_with_invalid_id(client):
    resp = client.remove_post('invalid')
    assert resp.status_code != 200


# Запуск тестов при выполнении скрипта
if __name__ == '__main__':
    pytest.main()