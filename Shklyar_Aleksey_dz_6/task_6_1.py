with open('nginx_logs.txt', encoding='utf-8') as f:
    result = []  # объявляем результирующий список
    for raw_line in f:   # читаем построчно из файла значения в виде списка
        line = raw_line.split()  # очищаем сырую строку от управляющих символов
        result.append((line[0], line[5].replace('"', ''), line[6]))  # нам нужны 0,5,6 элементы списка
for idx in range(0, len(result)):
    print(result[idx])  # выводим результат списка в удобном виде
