# Вводите числа, пока не введёте 0
# Надо отобразить все числа до 0 в списке
# Ввод:
# 8
# 4
# 11
# 0

# Вывод:
# [8, 4, 11]

result = []
while True:
    num = int(input())

    if num == 0: # False
        break

    result.append(num)

print(result)
