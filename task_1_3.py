input_value = int(input('Введите значание процентов: '))
list_of_exceptions = [11, 12, 13, 14]  # исключение из общего правила склонения
for number in range(0, input_value + 1):  # для каждого числа от 0 до введенного выводим значание
    number = str(number)                  # приводим к строке, что бы посмотреть последний элемент последовательности
    if int(number[-1]) == 1 and int(number) != 11:
        print(f'{number} - процент')
    elif int(number[-1]) >= 5 or int(number[-1]) == 0 or int(number) in list_of_exceptions:
        print(f'{number} - процентов')
    elif 2 <= int(number[-1]) <= 4:
        print(f'{number} - процента')
