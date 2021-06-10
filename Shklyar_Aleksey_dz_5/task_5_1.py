
# Задача 1 с использованием yield
def odd_nums(max_num):
    for num in range(1, max_num+1, 2):
        yield num

odd_to_15 = odd_nums(15)
for i in range (1, 9):
    print(next(odd_to_15))
