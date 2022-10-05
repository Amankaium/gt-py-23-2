# Пробить товар
# Сравнить цену
# Расплатиться

class Product:
    name = 'my product'
    price = 50
    packed_date = '01.01.2022'

    def show_exp_date(self):
        start_day = int(self.packed_date[:2])
        start_day += 10
        exp_date = f"{start_day}{self.packed_date[2:]}"
        self.exp_date = exp_date
        print(exp_date)  # 11.01.2022


apple = Product()
print(apple.price)
print(apple.packed_date)
apple.show_exp_date()

kefir = Product()
kefir.show_exp_date()