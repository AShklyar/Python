from utils import currency_rates

while True:
    enter_val = input('Введите валюту. Для выхода введите exit: ')
    if enter_val.upper() != 'EXIT':     # проверка вдруг криво введут exit, можно приводить lowe() разницы нет
        currency_rates(enter_val)
    else:
        break
