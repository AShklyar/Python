
input_list = [325.5, 254.41, 142.78, 444, 5472, 5476.2, 55.7, 777.0, 4447, 147.11, 100, 200, 300.01]
print(f'Исходная последовательность - {input_list}')
print(f'Её адрес - {id(input_list)}')
input_list.sort()
print(f'Исходная последовательность после сортировки- {input_list}')
print(f'Её адрес после сортировки - {id(input_list)}')
print(f'Пять самых дорогих цен: {input_list[-5:]}')

result_list = []
#  Преобразовываем int последовательность к str
for idx in range(len(input_list)):
    result_list.append(str(f'{input_list[idx]:.2f}'))
print(result_list)
input_list = []
for idx in range(len(result_list)):
    temp = (result_list[idx].split('.'))
    temp.insert(1, 'руб')
    temp.append('коп,')
    input_list.extend(temp)
print(input_list)
print(' '.join(input_list)[:-1])
