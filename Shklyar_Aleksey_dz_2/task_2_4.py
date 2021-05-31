input_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
for idx in range(len(input_list)):
    result_list = input_list[idx].split(' ')
    print(f'Првиет, {result_list[-1].capitalize()}!')
