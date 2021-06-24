#  coding=utf-8

import sys
from decimal import Decimal

price = sys.argv[1:]  # считываем цену
try:
    price = price[0].replace(',', '.')  # кто его знает какой там разделить десятичной части
    price = Decimal(price).quantize(Decimal("1.00"))  # чужого не надо, но и свое надо округлить правильно
except Exception as e:
    print(f'Попробуйте еще раз спокойно ввести сумму, например 100.00. Подробнее об ошибке: {e}')
    exit(1)

with open('bakery.csv', 'a', encoding='utf-8') as f: # открываем файл на запись, добавляем в конец
    f.write(str(price) + '\n')
