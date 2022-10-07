class Balance:
    def __init__(self, money):
        self.current_balance = money
        # print(f"Баланс {money}")
        self.start_job = True
        # ... 1000 cтрок

    current_balance = 0

    def add_money(self, money):
        self.current_balance += money


class DayBalance(Balance):
    def __init__(self, money, day):
        super().__init__(money)
        self.day = day
# DayBalanceSom, DayBalanceDollar

class Valuta:
    def set_valuta(self, type):
        self.type = type


class DayBalanceValuta(DayBalance, Valuta):
    def __init__(self, money, day, valute_type):
        super().__init__(money, day)
        self.set_valuta(valute_type)

    def show_balance(self):
        print(f"{self.current_balance} {self.type}")  # cash_1.type

    def incasation(self):
        if self.current_balance > 0:
            print(f"Инкассация {self.current_balance} {self.type}")
            self.current_balance = 0
        else:
            print("Инкасация невозможна, касса пуста")


# пришёл кассир, выдаём кассу
cash_1 = DayBalanceValuta(1500, "06.10.2022", "som")
cash_1.show_balance()  # cash_1.show_balance(cash_1)  # cash_1.type
cash_1.incasation()

cash_2 = DayBalanceValuta(20000, "09.10.2022", "Tenge")
cash_2.show_balance()
cash_2.incasation()
cash_2.incasation()
