import pytest
from price import calculate_price

@pytest.mark.parametrize("price, quantity, discount, expected", [
    (1500, 3, 10, 4050.0),  # обычный случай с скидкой
    (1500, 3, 0, 4500.0),   # без скидки
    (1500, 3, 100, 0.0),    # скидка 100%
    (1500, 1, 10, 1350.0),  # минимальное количество
    (1500, 3, 101, "Ошибка: скидка должна быть в диапазоне от 0 до 100."),
    (1500, 3, -10, "Ошибка: скидка должна быть в диапазоне от 0 до 100."),
    (1500, 0, 10, "Ошибка: количество должно быть больше нуля."),
    (1500, -1, 10, "Ошибка: количество должно быть больше нуля."),
    (-1500, 3, 10, "Ошибка: цена не может быть отрицательной.")
], ids=[
    "discount_10",
    "discount_0",
    "discount_100",
    "one_item",
    "discount_101",
    "discount_negative",
    "quantity_0",
    "quantity_negative",
    "price_negative",
])
def test_calculate_price(price, quantity, discount, expected):
    assert calculate_price(price, quantity, discount) == expected
