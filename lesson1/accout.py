# Пробить товар
# Сравнить цену
# Расплатиться

# База данных
current_money = 2350

products = {
    '11111': ["Яблоко", 50, '01.10.2022'],
    '22222': ["Кефир", 60, '03.10.2022'],
    '45243': ["Cыр", 100, '01.08.2022'],
    # ...
}

buys = []

while True:
    # Пробить товар
    sh_code = input()

    # Сравнить цену
    price = products[sh_code][1]
    name = products[sh_code][0]
    print(f"Вы купили {name} за {price} сом")

    current_money += price
    print(f"На кассе {current_money} сом")
