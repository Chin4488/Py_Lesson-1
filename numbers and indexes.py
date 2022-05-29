# Написать программу получающую набор произведений чисел от 1 до N. 
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
N = int(input('Ведите показатель N : '))
if N == 0 :
    print("Введён 0, список пуст")
elif N == 1 :
    print("[1]")
else:
    list = []
    list.append(1)
    temp = 2
    for i in range(3, N + 2):
        list.append(temp)
        temp *= i
    print(list)