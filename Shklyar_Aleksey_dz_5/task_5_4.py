src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123] резульат который должны получить

result_value = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]] # первый элемент нас не интересует

print(type(result_value))
print(result_value)
