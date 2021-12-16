"""
Оксана работает бухгалтером и каждый день выгружает из компьютера сводку за прошедшие сутки, 
которая содержит все приходы и расходы организации и итог. В сводке записаны только целые числа, 
и точно известно, что самое последнее число есть сумма всех предыдущих чисел.

Например, варианты сводок:

100 -50 10 -25 90 -35 90
5 -25 10 -35 -45
Эти сводки Оксана красиво оформляет в отчёте так:

+100 - 50 + 10 - 25 + 90 - 35 = +90
или так:

+5 - 25 + 10 - 35 = -45
Но однажды, придя на работу, Оксана обнаружила, что компьютер заразился вирусом и принялся 
из вредности путать числа в сводке. Например, вместо

5 -25 10 -35 -45 
он выдаёт явно ошибочное

10 -25 -45 -35 5
!

Оксана попросила программиста Олега, специализирующегося на искусственном интеллекте, 
помочь ей срочно подготовить правильные отчёты. Помогите Оксане -- напишите алгоритм, 
который будет находить в сводке число, равное сумме всех остальных чисел.

Функция

int SumOfThe(int N, int [] data)
получает параметром N длину всей сводки (N >= 2), и далее в массиве длиной N хранится сама сводка (целые числа).
Возвращает функция целое число из сводки, которое равно сумме всех остальных чисел.
"""
def SumOfThe(N, data):
    intermediate_list = []
    for i in data:
        intermediate_list.append(i)
    for k in range(0, N):
        intermediate_list.remove(list_1[k])
        if data[k] == sum(list_1):
            return data[k]
        intermediate_list.insert(k, data[k])



