import json
from itertools import zip_longest
result = dict()  # инициализируем конечный словарь
with open('users.csv', encoding='utf-8') as f_users:  # открыли на чтение файл пользователей
    with open('hobby.csv', encoding='utf-8') as f_hobby:  # открываем на чтение файл с хобби
        # проверка на количество строк в файле с хобби, если строк больше чем пользователей то выходим с кодом 1
        if len(f_users.readlines()) < len(f_hobby.readlines()):
            exit(1)
        # после проверки надо вернуться в начало файла
        f_users.seek(0)
        f_hobby.seek(0)
        # сразу идем по строкам обоих файлов используем zip_longest для случая когда для пользователя отсутствует хобби
        namesakes_count = 1  # переменная для изменения ключа полных тезок
        for line_users, line_hobby in zip_longest(f_users, f_hobby):
            # проверяем есть ли очередной ключ в результирующем словаре
            if line_users.strip().replace(',', ' ') in result.keys():  # если да, то немного меняем его
                line_users = str(namesakes_count)+' '+line_users.strip()
                namesakes_count += 1
            if line_hobby:  # проверяем есть ли хобби, если нет, то записываем None
                result.setdefault(line_users.strip().replace(',', ' '), line_hobby.strip().replace(',', ' '))
            else:
                result.setdefault(line_users.strip().replace(',', ' '))
with open('task_6_3.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)  # записываем в файл словарь
with open('task_6_3.json', 'r', encoding='utf-8') as f:
    result_load = json.loads(f.read())      # считываем из файла словарь, специально ввел другую переменную
print(type(result_load), result_load)  # проверяем ей тип - тип dict
