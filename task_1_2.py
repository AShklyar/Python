some_list = []

for idx in range(1, 1001):       # заполняем лист нечетными числами
    if idx % 2 != 0:
        some_list.append(idx ** 3)
total_sum = 0                  # переменная для записи итоговой суммы
for idx in some_list:
    some_sum = 0                # промежуточная переменная для суммы цыкла

    for some_count in str(idx):  # приводим к строке и идем по ней суммируя значания в промежуточную переменную
        some_sum += int(some_count)
    if some_sum % 7 == 0:
        total_sum += some_sum
print(f'Часть а. Сумма всех чисели {total_sum}')

# Чась б.
total_sum = 0
for idx in some_list:
    idx += 17  # все то же самое, только при извлечении элемента из списка увеличиваем его значание на 17
    some_sum = 0
    for some_count in str(idx):
        some_sum += int(some_count)
    if some_sum % 7 == 0:
        total_sum += some_sum
print(f'Часть б. Сумма всех чисел {total_sum}')
