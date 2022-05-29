# Подсчитать сумму цифр в вещественном числе.

import random
randomNumber = (random.uniform(-100, 100))
randomNumber = round(randomNumber, 2)
print('Выбранное число: ', randomNumber)
randomNumber = str(randomNumber)
sumDigit = 0
for i in randomNumber:
    if i != "." and i != "-":
        sumDigit += int(i)
print('Сумма цифр числа: ', sumDigit)