from random import randint
from datetime import datetime
start = datetime.now()
#  загадываем число
n = 100
num = randint(1, n) # 33
print(num)

#  Угадываем число - перебор / brute force - O(n)
# for i in range(1, n):
#     if num == i:
#         print("Число:", i)
#         break

prev_min = 1
prev_max = n
i = (prev_min + prev_max) // 2
k = 0

while True:
    k += 1
    # print(i)
    if i == num:
        print(i)
        break
    elif i < num:
        prev_min = i
        i = (prev_min + prev_max) // 2
    elif i > num:
        prev_max = i
        i = (prev_min + prev_max) // 2

print("шагов:", k)
end = datetime.now()
print(end - start)
