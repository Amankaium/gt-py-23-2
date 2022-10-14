# Пробить товар
# Сравнить цену
# Расплатиться

# v 1) Создать класс Balance с конструктором, принимающий название файла
# v 2) Добавить метод для считывания текущего баланса с файла, если файла нет или он пустой, то баланс должен быть 0
# v 3) Добавить метод для записи текущего баланса в файл
# v 4) Добавить метод для инкассации
# v 5) Добавить магический метод str который будет отображать текущий баланс


class Balance:
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_balance()
        print("Объект создан", self)

    def __str__(self):
        return f"Текущий баланс: {self.current_money}"

    def get_balance(self):
        try:
            with open(self.file_name, mode="r+") as cm_file:
                balance = cm_file.read()
            if balance:
                current_money = int(balance)
            else:
                cm_file.write("0")
                current_money = 0
        except FileNotFoundError:
            with open(self.file_name, mode="w+") as cm_file:
                cm_file.write("0")
                current_money = 0

        self.current_money = current_money

    def add_money(self, money):
        self.current_money += money
        self.write_balance()
        print(f"Добавление баланса {money}", self)

    def write_balance(self):
        with open(self.file_name, mode="w+") as cm_file:
            cm_file.write(str(self.current_money))

    def incasation(self):
        if self.current_money > 0:
            print(f"Инкассация {self.current_money}")
            self.current_money = 0
            print(self)
        else:
            print("Инкасация невозможна, касса пуста", self)


b_1 = Balance("test_1.txt")
b_1.add_money(100)
b_1.add_money(50)
b_1.incasation()
b_1.incasation()

balance_2 = Balance("my_file2.txt")
balance_2.add_money(100)
balance_2.incasation()
balance_2.add_money(200)
