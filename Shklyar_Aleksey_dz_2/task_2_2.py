input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
special_symbol = ('+', '-', '%', '<')  # более универсальный варинат для обработки чисел с префиксом
result_list = []
print(f'Входна последовательность: {input_list}')
for idx in range(len(input_list)):
    if input_list[idx].isdigit():
        result_list.append('"')
        result_list.append(f'{int(input_list[idx]):02d}')
        result_list.append('"')
    elif input_list[idx][:1] in special_symbol:
        if input_list[idx][1:].isdigit():
            result_list.append('"')
            result_list.append(f'{input_list[idx][:1]}{int(input_list[idx][1:]):02d}')
            result_list.append('"')
    else:
        result_list.append(f'{input_list[idx]}')
print(f'Итогова последовательно:   {result_list}')
print(f'Итоговая строка:           {" ".join(result_list)}')
