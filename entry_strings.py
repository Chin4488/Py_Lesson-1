# Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

def entrystrings(text1, text2):
    if len(text1) > len(text2):
        lenmin = len(text2)
        endindex = len(text1) - lenmin + 1
        textmin = text2
        textmax = text1
    
    else:
        lenmin = len(text1)
        endindex = len(text2) - lenmin + 1
        textmin = text1
        textmax = text2
    
    count = 0
    for i in range(0, endindex):
        if textmax[i:i+lenmin] == textmin:
            count +=1
    return count

    
text1 = input('Введите первую строку: ')
text2 = input('Введите вторую строку: ')

result = entrystrings(text1, text2)
if result == 0:
    print('Вхождения отсутствуют')
else:
   print('Количество вхождений: ', result)