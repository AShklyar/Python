from random import choice, shuffle

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопиный', 'мягкий']


def get_jokes(counts, key=True):
    """" Function maks random jokes. counts - int type (count of jokes in result list). key - bool type
         (True - replays are allowed : False - replays are not allowed)
    """
    work_list = []
    if key:
        # в этом цикле мы сразу из последовательности выбирваем случайным образом элементы последовательности
        # формируя итоговый список count раз (могу быть повторы)
        for idx in range(counts):
            work_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        return work_list
    else:
        if counts > min(len(nouns), len(adverbs), len(adjectives)):
            # максимальное количество уникальных последовательностей не более длинны минимального списка
            print('Введенное значание за границами диапозона')
            return None
        else:
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            # тут мы перемешали исходные списки случайным образом и идем по индексу каждого из них формируя итоговый
            # очевидно, что повторов в итоговом списке не будет, но есть ограничение по длине итогового списка
            for idx in range(counts):
                work_list.append(f'{nouns[idx]} {adverbs[idx]} {adjectives[idx]}')
    return work_list


flag = input('Можно повторять элементы? (yes/no): ')
if flag.lower() == 'yes':
    flag = True
    input_count = int(input('Введите число элементов итоговой последовательности: '))
else:
    flag = False
    input_count = int(input(f'Введите число элементов итоговой последовательности от 1 до '
                            f'{min(len(nouns),len(adverbs),len(adjectives))}: '))

print(get_jokes(input_count, flag))
