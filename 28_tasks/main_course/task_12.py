"""  Представленное ниже решение не соответствует условиям задачи

Хакер Эллиот (Мистер Робот) подбирает код для проникновения в хранилище данных "Стальная гора". 
Он собирается взломать систему климат-контроля, чтобы уничтожить все магнитные ленты Корпорации Зла. 
Помогите Эллиоту подобрать подходящий смарт-контроллер, который бы допускал потенциальную возможность взлома.


Для анализа поступает массив, в котором случайно перемешаны числа от 1 до N (без пропусков), N > 4.
Например, N=7 [1,3,4,5,6,2,7]

Хакерская утилита может делать только одну операцию: брать любые три идущие подряд элемента массива, 
и сдвигать их по кругу влево произвольное количество раз. Но эту операцию она может выполнять неограниченное количество раз.

Например:

[1,3,4,5,6,2,7] [5,6,2] -> [6,2,5] -> [2,5,6]
[1,3,4,2,5,6,7] [3,4,2] -> [4,2,3] -> [2,3,4]
[1,2,3,4,5,6,7] OK
Задача: определить, можно ли с помощью этой операции превратить массив в упорядоченный по возрастанию. 
Программа должна работать быстро (укладываться в 1 секунду при N ~= 10).

Функция

bool MisterRobot(int N, int [] data) 
получает значение N и сам массив, и возвращает true, если этот массив возможно упорядочить вышеописанным способом.
"""

def MisterRobot(N, data):
    x = 0
    y = 0
    b = 0
    list = []
    for i in range(0, N-1):         #проверка, являются ли элементы списка последовательностью
        if i == 0:                  #проверка первого элемента
            if data[i]+1 != data[i+1]: #если элементы не последовательны
                if data[i] > data[i+1]: #проверяем какой из них больше и присваиваем индикатору соответствующее значение
                    x = i                 
                    break
                else:
                    x = i+1
                    break
        elif data[i]+1 != data[i+1]:    #проверка, являются ли остальные  элементы списка последовательностью
            if data[i] < data[i+1]:
                x = i+1                 #проверяем какой из них больше и присваиваем индикатолру соответствующее значение
                break
            else:
                x = i-1
                break
    if i != 0 and x == 0:                      #если список состоит из последовательных элементов
        return True                 #получаем вывод
    if len(data[x:]) < 3:           #проверяем, что срез состоит из трех элементов
        list = data[N-3:]           #если меньше его дляна меньше, то добавляем до трех
        b = 1
    else:
        list = data[x:x+3]
    
    while y < 3:                    #цикл проверки последовательности элементов среза
        if ((list[0]+1) == list[1]) and ((list[1]+1) == list[2]):
            y = 3
        else:
            list = list[1:] + list[:1]
            y += 1
    if b == 1:
        data = data[:N-3] + list[:]
    else:
        data = data[:x] + list[:] + data[x+3:]
    
    for i in range(0, N-1):         #проверка, являются ли элементы списка последовательностью
        if data[i]+1 != data[i+1]:
            return False
    else:
        return True 

print(MisterRobot(7,[1,3,4,5,6,2,7]))
    