import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def user_response():
    return requests.get(f"{BASE_URL}/users/1")


@pytest.fixture
def new_post():
    return {
        "title": "Мой первый пост",
        "body": "Текст поста",
        "userId": 1,
    }


def test_get_user_status_200(user_response):
    assert user_response.status_code == 200


def test_get_user_has_correct_id(user_response):
    data = user_response.json()
    assert data["id"] == 1


def test_get_user_has_email(user_response):
    data = user_response.json()
    assert "email" in data

def test_get_user_had_invalid_id():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404

def test_get_user_had_city_gwenborough(user_response):
    data = user_response.json()
    assert data["address"]["city"] == "Gwenborough"

def test_create_post_status_201(new_post):
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201

def test_create_post_returns_sent_data(new_post):
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    data = response.json()

    assert data["title"] == new_post["title"]
    assert data["userId"] == new_post["userId"]
    assert data["id"] is not None