from requests import get
from decimal import Decimal
import datetime


def currency_rates(some_cash):
    get_val = get('http://www.cbr.ru/scripts/XML_daily.asp')
    date_conversation = get_val.text[get_val.text.find('Date')+6:get_val.text.find('Date')+16]
    date_conversation = datetime.datetime.strptime(date_conversation,"%d.%m.%Y")
    # print(type(date_conversation)) так можно проверить что действительно объект типа date
    # переводим в верхний регистра
    some_cash = some_cash.upper()
    # знаяю структуру XML, зная что валюта обозначается 3 заглавными буквами можно сразу
    # посмотрет есть такая валюта в строке или нет
    if some_cash in get_val.text:
        start = get_val.text.find('<Value>',get_val.text.find(some_cash))  # смотрим первое вхождение <Value> после того
                                                                           # как нашли валюту
        value = get_val.text[start+7:start+14]
        value = value.replace(',','.')  # для Decimal оказалось критично, меняем запятую на точку
        print(f'{some_cash} {Decimal(value).quantize(Decimal("1.00"))} {date_conversation.strftime("%d.%m.%Y")}') # выводим значание и округляем его до сотых
    else:
        print('Такой валюты нет')


some_cash = input('Введите валюту: ')
currency_rates(some_cash)
