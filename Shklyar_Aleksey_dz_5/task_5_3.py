from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена','Алексей', 'Евгений','Борис']
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_result = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))

# print(gen_result[1]) # так как это генииратор, то нельзя обратиться по индексу, тут будет ошибка

print(type(gen_result))  # смотрим что gen_result дествительно класса генераторов
print(*gen_result, sep='\n')    # выводим результат для удобства столбиком, получили последовательноть из кортежей
