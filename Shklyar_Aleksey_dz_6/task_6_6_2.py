import sys

params = sys.argv[1:3]  # считываем только первые два параметра
with open('bakery.csv', encoding='utf-8') as f:
    end_position = len(f.readlines())
    f.seek(0)
    if len(params) == 2:  # если параметров 2, тут все просто переопределяем начальное и конечные позиции
        try:   # главное что бы параметрами были целые числа
            start_position = int(params[0])
            if start_position > end_position:  # если пользователь введет начальное значение больше чем конечное
                start_position = 0             # то выводим данные с самого начала
            end_position = int(params[1])      # так как 2 параметра, то переопределяем конечную позицию
        except Exception as e:  # ну, а если все же пользователь захочет что-то от себя ввести, обозначим его границы
            print(f'Введены некорректные параметры. Введите целые числа от 0 до {end_position}. '
                  f'Информация об ошибке: {e}')
            exit(1)
    elif len(params) == 1:
        try:
            start_position = int(params[0])
            if start_position > end_position:
                start_position = 0
        except ValueError as e:
            print(f'Введен некорректный параметр. Введите целое число от 0 до {end_position}. '
                  f'Информация об ошибке: {e}')
            exit(1)
    else:
        start_position = 0
    for idx, line in enumerate(f):
        if start_position <= idx + 1 <= end_position:
            print(f'{idx+1}. {line.strip()}')
