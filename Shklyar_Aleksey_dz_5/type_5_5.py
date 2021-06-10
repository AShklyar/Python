src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_1 = [idx for idx in src if src.count(idx) == 1]
result_2 = [idx for idx in src if src.count(idx) != 1]
print(f'Уникальные элементы последовательности   {result_1}')
print(f'Повторяющиеся элементы последователности {list(set(result_2))}')
