
# Задание task_01_11.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


# В данной задаче все значения задаются в коде (без input())

# 1. Создание словаря
# Создать пустой словарь
info = # Удалите комментарий и допишите код

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = # Удалите комментарий и допишите код
# Удалите комментарий и допишите код
# Удалите комментарий и допишите код

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк -
# наименований хобби (например "плавание" и т.д.)
# Удалите комментарий и допишите код

# Добавить "программирование" в список хобби
# Удалите комментарий и допишите код

# Создать ключ "животные" со значением = кортеж из строк -
# имен домашних животных (например "кошка Мурка" и т.д.)
# Удалите комментарий и допишите код

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
# Удалите комментарий и допишите код

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# где ключ - наименование предмета, а значение - количество баллов
# Удалите комментарий и допишите код

# Добавить экзамен, который не был сдан, после чего удалить его
# Удалите комментарий и допишите код

# Создать ключ "вузы" и поместить в него пустой словарь
# Удалите комментарий и допишите код

# В словарь info["вузы"] добавить информацию о вузах,
# где ключ - аббревиатура вуза, а значение -
# количество баллов для специальности, на которую хотели поступить
# Удалите комментарий и допишите код

# 2. Вывод на экран
print("Данные:")
# Получившийся словарь
# Удалите комментарий и допишите код

# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = # Удалите комментарий и допишите код
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = # Удалите комментарий и допишите код
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = # Удалите комментарий и допишите код
# Начинается на гласную? (True/False)
starts_with_vowel = # Удалите комментарий и допишите код
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
month = # Удалите комментарий и допишите код
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = # Удалите комментарий и допишите код
print("* родился летом или зимой:", # Удалите комментарий и допишите код)

# Количество хобби и первое из них
hobbies_count = # Удалите комментарий и допишите код
print("* у меня {} хобби, первое \"{}\"".format(# Удалите комментарий и допишите код))

# Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(# Удалите комментарий и допишите код))

# Сумма баллов по экзаменам
sum_mark = # Удалите комментарий и допишите код
print("* сумма баллов = {}".format(# Удалите комментарий и допишите код))

# Максимальный балл среди сданных
max_mark = # Удалите комментарий и допишите код
print("* макс. балл = {}".format(# Удалите комментарий и допишите код))

# Количество вузов, в которые Вы проходите по баллам
# Подсказка: определить, проходите Вы или нет, можно простым сравнением
# суммы баллов с проходным баллом вуза - ``True/False``.
# Для того, чтобы определить количество таких вузов, преобразуйте
# сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
vuz_count = # Удалите комментарий и допишите код
print("* кол-во вузов в которые прохожу: {}".format(# Удалите комментарий и допишите код))



# --------------
# Пример вывода:
#
# {'фио': 'Иванов Иван Иванович', 'место_рождения': 'Париж',
#  'дата_рождения': '01/09/1995'}
# Данные:
# {'фио': 'Иванов Иван Иванович', 'животные': ('кошка Мурка',),
#  'вузы': {'МИРЭА': 240, 'МГУ': 295, 'МГТУ им. Баумана': 255},
#  'хобби': ['игра на гитаре', 'туризм', 'программирование'],
#  'ЕГЭ': {'Математика': 90, 'Информатика': 88, 'Русский язык': 67},
#  'дата_рождения': '01/09/1995', 'место_рождения': 'Париж'}
# Предметы: Информатика, Математика, Русский язык
# Вузы: МГТУ им. Баумана, МГУ, МИРЭА

# Ответы на вопросы:
# * мое имя начинается на гласную букву: True
# * родился летом или зимой: False
# * у меня 3 хобби, первое "игра на гитаре"
# * после окончания школы сдавал 3 экз.
# * сумма баллов = 245
# * макс. балл = 90
# * кол-во вузов в которые прохожу: 1
