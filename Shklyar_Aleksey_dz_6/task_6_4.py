from itertools import zip_longest
with open('users_hobby.txt', 'w', encoding='utf-8') as f_base:  # открываем файл через менеджер контекста на запись и
    # работаем в области его видимости
    with open('users.csv', encoding='utf-8') as f_users:  # открыли на чтение файл пользователей
        with open('hobby.csv', encoding='utf-8') as f_hobby:  # открываем на чтение файл с хобби
            # проверка на количество строк в файле с хобби, если строк больше чем пользователей то выходим с кодом 1
            if len(f_users.readlines()) < len(f_hobby.readlines()):
                exit(1)
            # после проверки надо вернуться в начало файла
            f_users.seek(0)
            f_hobby.seek(0)
        # сразу идем по строкам обоих файлов используем zip_longest для случая когда для пользователя отсутствует хобби
        # так как уже работаем не с объектом типа dict(), то можно не проверять на тезок
            for line_users, line_hobby in zip_longest(f_users, f_hobby):
                line_users = line_users.strip().replace(',', ' ')
                if line_hobby:
                    line_hobby = line_hobby.strip().replace(',', ' ')
                f_base.write(f'{line_users}: {line_hobby}\n')
