
# Задание task_03_03_02.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def primes(a, b):
    """Вернуть список простых чисел на отрезке от 'a' до 'b'."""
    res = []
    c = 0
    for i in range(a, b):
        for j in range(i):
            if i % (j + 1) == 0:
                c += 1
            if c == 2:
                res.append(i)

    return res
