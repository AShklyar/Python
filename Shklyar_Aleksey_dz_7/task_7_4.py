import os
files_size = []
for root, directory, files in os.walk(r'/Users/alekseyshklyar/Downloads/some_data'):
    for file in files:
        files_size.append(os.stat(os.path.join(root, file)).st_size)  # создаем список значений размера файла

max_size = max(files_size)  # определяем максимальный размер файла для определения максимального значение в группе
result_dict = dict()
i = 1
groups = []
for idx in range(len(str(max_size))):  # создаем группу значений типа 10, 100, 1000, 10000 и т.д.
    i *= 10
    groups.append(i)
result_dict = result_dict.fromkeys(groups, 0)  # инициализируем словарь  из полученной последовательности

for value in files_size:
    # вычисляем ближайшее большее число из groups, куда и посчитаем файл
    put_to_group = min(filter(lambda x: value < x, groups))
    result_dict[put_to_group] += 1

print(result_dict)
