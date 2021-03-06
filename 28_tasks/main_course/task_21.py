"""
Вы, тренер сборной России по футболу, ухитрились вывести её в финал чемпионата мира. 
Ваша задача -- определить, можно ли улучшить расстановку игроков на поле перед решающей встречей, 
или всё бесполезно и придётся использовать текущий вариант. Но у вас в распоряжении остались только 
два тренерских приёма, времени уже нету, и использовать можно только один из них.


На входе -- массив произвольных целых чисел (значения не повторяются).

Ваша задача -- попробовать упорядочить его по возрастанию с помощью однократного применения одного из двух приёмов:
1. Поменять местами два произвольных элемента массива.
2. Изменить на обратный порядок произвольной последовательной цепочки элементов в массиве.

Например, на входе

1) 1 3 2
Упорядочиваем правилом 1, меняем местами 3 и 2:
1 2 3

2) 3 2 1

Упорядочиваем правилом 2, меняем порядок с первого элемента до последнего:
1 2 3

3) 1 7 5 3 9
Упорядочиваем правилом 1, меняем местами 7 и 3:
1 3 5 7 9

4) 9 5 3 7 1
Нельзя упорядочить.

5) 1 4 3 2 5
Упорядочиваем правилом 2, меняем порядок с второго элемента до четвёртого:
1 2 3 4 5
Функция

boolean Football(int F[], int N)
получает на вход массив F из N (N >= 1) целых неповторяющихся чисел и возвращает true, если массив можно упорядочить однократным применением одного из двух правил.
"""

def Football(F, N):
    A = F[:]
    B = F[:]
    A.sort()
    if len(F) == 1:
        return False
    elif F == A:
        return False
    elif F[::-1] == A:
        return True

    for i in range(0, len(F)-1):
        if F[i] > F[i+1]:
            B[i],B[i+1] = B[i+1], B[i]
            break
    if B == A:
        return True
    
    B = F[:]
    b = 0
    c = 0
    ordered_complete = False
    for j in range(0, len(F)-1):
        if F[j] > F[j+1]:
            b += j
            for k in range(b+1, len(F)-1):
                if F[k] > F[k+1]:
                    c = c+k+1
                    B[b],B[c] = B[c],B[b]
                    if B == A:
                        return True
                    ordered_complete = True
                    break
        if ordered_complete:
            break
    
    ordered_complete = False
    B = []
    for g in range(0, len(F)-1):
        if F[g] > F[g+1]:
            for h in range(g, len(F)-1):
                if F[h] < F[h+1]:
                    for i in range(0,g):
                       B.append(F[i])
                    for j in range(h, g-1, -1):
                        B.append(F[j])
                    for k in range(h+1, len(F)):
                        B.append(F[k])
                    if B == A:
                        return True
                    ordered_complete = True
                    break
                elif h == (len(F)-2):
                    for i in range(0,g):
                       B.append(F[i])
                    for j in range(h+1, g-1, -1):
                        B.append(F[j])
                    if B == A:
                        return True
                    ordered_complete = True
                    break
        if ordered_complete:
            break
    
    return False
    