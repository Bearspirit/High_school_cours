"""
РАЙНЕХАРТ

Наша компания - ведущая компания по разработке программного обеспечения в мире. 
И это все благодаря тому, что каждый отдельный служащий понимает, что он - часть целого. 
Таким образом, если служащий имеет проблему, это означает, что вся компания имеет проблему.
Пока ваша самая большая проблема, мистер Андерсон, что вы не выполнили в срок рабочее задание.
Пришло время делать выбор, мистер Андерсон. Либо вы сейчас же реализуете вычисление разностей BigInteger, 
либо вы будете вынуждены искать другую работу. Я ясно выражаюсь?


Требуется вычислить разницу между двумя целыми неотрицательными числами, заданными своим строковым 
представлением (например, "1234567890" и "321").
Числа задаются в диапазоне от 0 до 10^16 (включительно).

В некоторых языках есть поддержка так называемых BigInteger, которые потенциально не ограничены диапазонами, 
однако арифметические операции над ними выполняются не процессором, а эмуляционным кодом. 
По сути, для этих операций просто вызываются функции стандартных библиотек.

Возможно, в выбранном вами языке имеется поддержка BigInteger, однако в данной миссии надо обойтись без них.
Придумайте, как вычислять разность для любых заданных значений.

Функция

string BigMinus(string s1, string s2)
получает на вход два числа в формате строки (числа всегда корректные -- набор цифр), и возвращает абсолютное 
значение (модуль) разности -- первое число s1 минус второе число s2, также в формате строки.
Например,
BigMinus("1234567891", "1") = "1234567890"
BigMinus("1", "321") = "320"
"""

def BigMinus(s1, s2):
    d1 = 0
    x1 = len(s1)-1
    y1 = 0
    while x1 >= 0:
        d1 = d1 + (int(s1[y1])*(10**x1))
        x1 -= 1
        y1 += 1
    d2 = 0
    x2 = len(s2)-1
    y2 = 0
    while x2 >= 0:
        d2 = d2 + (int(s2[y2])*(10**x2))
        x2 -= 1
        y2 += 1
    
    if d1 >= d2:
        return str(d1-d2)
    else:
        return str(d2-d1)
