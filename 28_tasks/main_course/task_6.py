"""
Поступил крупный заказ на автоматизацию процесса подсчёта результатов выборов.

В систему поступает количество голосов, отданных за каждого из кандидатов. Она должна обработать их и определить один из трёх вариантов результата:

- победитель, набравший больше всех голосов и при этом более 50% голосов;

- победитель, набравший больше всех голосов и при этом менее или ровно 50% голосов;

- перевыборы (выявлено несколько победителей с одинаковым количеством голосов).

Например, список голосов, отданных за пятерых кандидатов, первый случай:
60, 10, 10, 15, 5. Победил первый кандидат с результатом 60%.

Cписок голосов, отданных за трёх кандидатов, второй случай:
10, 15, 10. Победил второй кандидат с результатом 42.85%.

Перевыборы, четыре кандидата: 111, 111, 110, 110

Точность результата округляется до трёх знаков после запятой.

Функция

string MassVote(int N, int [] Votes)
получает на вход количество кандидатов N >= 1 и массив, содержащий N голосов, отданных за соответствующих кандидатов.
На выходе формируется строка в одном из трёх форматов:

1) "majority winner K" если имеется победитель с номером K (начиная с 1), набравший более 50% голосов. 
Для случая 60, 10, 10, 15, 5 строка примет вид

majority winner 1
2) "minority winner K" если имеется победитель с номером K (начиная с 1), набравший менее 50% голосов. 
Для случая 10, 15, 10 строка примет вид

minority winner 2
3) "no winner" если победителя не выявлено.
"""

def MassVote(N, Votes):
    intermediate_list = []
    for i in Votes:
        intermediate_list.append(i)
    MAJOR_WIN = "majority winner"
    MINOR_WIN = "minority winner"
    for k in range(0, N):
        assert sum(Votes)>0
        votes_ratio = round(Votes[k]/sum(Votes)*100, 3)
        if votes_ratio > 50:
            output_message = MAJOR_WIN + " " + str(k+1)
            return output_message
        else:
            intermediate_list.remove(intermediate_list[k])
            if (Votes[k] not in intermediate_list) and (round(Votes[k]/sum(Votes)*100, 3) <= 50) and (Votes[k] == max(Votes)):
                output_message = MINOR_WIN + " " + str(k+1)
                return output_message
            intermediate_list.insert(k, Votes[k])
    NO_WIN = "no winner"
    output_message = NO_WIN
    return output_message
