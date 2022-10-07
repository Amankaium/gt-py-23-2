# Пробить товар
# Сравнить цену
# Расплатиться

# База данных
with open("current_money.txt", mode="r+") as cm_file:
    balance = cm_file.read()
    print(type(balance), balance)
    if balance:
        current_money = int(balance)
    else:
        cm_file.write("0")
        current_money = 0


def write_balance(money):
    with open("current_money.txt", mode="w+") as cm_file:
        cm_file.write(str(money))


class Product:
    def __init__(self, name, price, packed_date):
        self.name = name
        self.price = price
        self.packed_date = packed_date

buys = []

products = {
    '11111': Product("Яблоко", 50, '01.10.2022'),  # ["Яблоко", 50, '01.10.2022'],
    '22222': Product("Кефир", 60, '03.10.2022'),  # ["Кефир", 60, '03.10.2022'],
    '45243': Product("Cыр", 100, '01.08.2022'),  # ["Cыр", 100, '01.08.2022'],
    # ...
}

while True:
    # Пробить товар
    sh_code = input()

    if sh_code == "0":
        print("Смена окончена")
        print(buys)
        break

    # Сравнить цену
    price = products[sh_code].price
    name = products[sh_code].name
    buys.append(products[sh_code])
    print(f"Вы купили {name} за {price} сом")

    current_money += price
    write_balance(current_money)
    print(f"На кассе {current_money} сом")
