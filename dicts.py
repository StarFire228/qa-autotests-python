import pytest

order = {
    "id": 1,
    "product": "iPhone",
    "price": 100000,
    "quantity": 2,
    "status": "new",
}

print(f"Номер заказа: {order['id']}. Товар: {order['product']}. Цена: {order['price']}. Сумма: {order['price'] * order['quantity']} ")

order["status"] = "paid"  # изменить существующее

print(order["status"])  # paid

assert order["status"] == "paid"
assert "id" in order
assert order["price"] > 0

print("Все проверки пройдены успешно.")