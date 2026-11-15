def calculate_price(price, quantity, discount=0):
    if quantity <= 0:
        return "Ошибка: количество должно быть больше нуля."
    elif discount < 0 or discount >= 100:
        return "Ошибка: скидка должна быть в диапазоне от 0 до 100."
    elif price < 0:
        return "Ошибка: цена не может быть отрицательной."
    else:
        total = price * quantity
        discount_rub = total * discount / 100
        return total - discount_rub

def ipone_sell(id, status, price, quantity):
    if status == "paid":
        return "Ошибка: заказ уже выкуплен."
    elif not id:
        return "Ошибка: заказ не найден."
    elif price < 0:
        return "Ошибка: цена не может быть отрицательной."
    elif quantity <= 0:
        return "Ошибка: количество должно быть больше нуля."
    else:
        return "Заказ успешно оформлен."