# создаем гениратор нечетных чисел до n+1
n = 19
nums_gen = (num for num in range(1, n+1, 2))
print(type(nums_gen)) # проверяем класс объекта
for i in range (0, n//2+1):
    print(next(nums_gen))

print(next(nums_gen)) # этот вызов приведет к ошибке, так как генератор закончился
