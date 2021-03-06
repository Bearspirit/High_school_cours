"""
Британские учёные перехватили трафик переговоров двух НЛО, шпионящих за Землёй. 
Как выяснилось, сигналы первой НЛО передаются в восьмеричной системе счисления, 
а сигналы второй НЛО передаются в шестнадцатеричной системе счисления.

Для быстрой расшифровки их переговоры надо представить в более привычной землянам 
десятичной системе счисления. Срочно требуется конвертор для разных систем счисления.

Функция

int [] UFO(int N, int [] data, bool octal)
получает на вход длину N цифровой записи трафика, сам трафик (последовательность положительных чисел) 
в массиве data, и флажок octal, который задаёт систему счисления входных данных: 
восьмеричная если octal = true, и шестнадцатеричная в противном случае.
Если числа подаются в восьмеричной системе счисления, гарантируется, что в них не будет цифр 8 и 9.
Функция возвращает массив длины N, содержащий исходные числа, преобразованные в десятичную систему счисления.

Например, если на вход подаётся массив из двух чисел 1234,1777 с флажком octal = false, то результат будет 4660,6007.
А если флажок для данного массива будет true, то результат будет 668,1023.
"""
def UFO(N, data, octal):
    if octal == True:
        octo = []
        for x in data:
            num_8 = str(x)
            num_str = num_8[::-1] #разворачиваем строковое представление числа в обратный порядок
            a = 0
            for i in range(0, len(num_str)):
                a += (8**i)*int(num_str[i]) #i-соответствует разряду числа, для чего на прощлом этапе число было перевернуто
            octo.append(a)
        return octo
    if octal == False:
        sxtee = []
        for k in data:
            num_16 = str(k)
            num_str = num_16[::-1]
            b = 0
            for j in range(0, len(num_str)):
                b += (16**j)*int(num_str[j])
            sxtee.append(b)
            #sxtee.append(int(str(k), 16))
        return sxtee

