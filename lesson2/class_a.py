class A:
    def __init__(self, age=0): # магический метод
        self.name = "Aman"
        self.age = age

    def __str__(self):
        return f"Объект {self.name} класса А"


a_1 = A(20)
print(str(a_1))

a_2 = A(40)
print(a_2)
