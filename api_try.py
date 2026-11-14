import requests

new_post = {
    "title": "Мой первый пост",
    "body": "Текст поста",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post,
)

test_create_post_status_201 = {
    "title": "Мой второй пост",
    "body": "Текст второго поста",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=test_create_post_status_201,
)

print(response.status_code)
print(response.json())

test_create_post_returns_sent_data = {
    "title": "Мой третий пост",
    "body": "Текст третьего поста",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=test_create_post_returns_sent_data,
)

print(response.status_code)
print(response.json())