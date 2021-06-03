

def thesaurus(*input_val):
    work_dict = {}
    work_list_key = []
    work_list_add = []
    for idx in range(len(input_val)):
        work_list_key.append(input_val[idx][0])  # формируем список клчюей
    work_list = list(set(work_list_key))    # удаляем дубликаты
    work_list.sort()    # сортируем список ключей
    for char in work_list_key:
        for name in input_val:
            if char == name[0]:
                work_list_add.append(name)
        work_list.sort()    # сортируем список значений
        work_dict[char] = work_list_add
        work_list_add = []
    return work_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Алексей', 'Матвей', 'Ольга', 'Нина', 'Мария', 'Антон'))
