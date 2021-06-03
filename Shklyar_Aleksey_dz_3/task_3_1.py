import ast

# изначально идея была хранить словарь в файле, так как словарь можео изменять не меняя код программы, дополнять его
# после первого открытия и загрузки строки столкнулся с тем, что русская кодировка некорректно отображается
# посмотрел аргументы функции open увидел там encoding и догадался, что это должно быть связано с кодировкой)


def num_translate(eng_val):
    with open('dict.txt', encoding='utf-8') as dictionary:
        dict_string = dictionary.read()     # читаем строку
        rus_val = ast.literal_eval(dict_string)     # изучил в сети как из файла передать словарь
        return rus_val.get(eng_val)         # получил значание по ключу, если нет значание то get вернет None


enter_val = ''

while True:
    enter_val = input('Введите значаение для перевода. Для выхода введите exit: ')
    if enter_val.upper() != 'EXIT':     # проверка вдруг криво введут exit, можно приводить lowe() разницы нет
        if enter_val[0].isupper():
            # тут для меня откровение, что все же надо приводить результат выполнения к str, думал python сам догадается
            # я то понимаю что возварщается обект типа str а вот PyCharm после . не выводит метот capitalize()
            # print(type(num_translate(enter_val.lower()))) возвращает class 'str'
            print(str(num_translate(enter_val.lower())).capitalize())
        else:
            print(num_translate(enter_val))
    else:
        break
