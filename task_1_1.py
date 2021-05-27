duration = int(input("Ведите продалжительность временного интервала в секундах: "))
if duration >= 86400:            # проверяем введенное значение больше одних суток?
    days = duration // 86400     # получаем количество дней, запоминаем
    duration = duration % 86400  # уменьшаем введенное значение до пределов одних суток
else:
    days = 0                     # если введеное значение менее 86400, значит вычисляем в пределах одного дня

hour = duration // 3600             # получаем количество часов
minutes = (duration % 3600) // 60   # получаем минуты
seconds = (duration % 3600) % 60    # получаем количество секунд
if days == 0:
    if hour == 0:
        if minutes == 0:
            print("{} сек".format(seconds))
        else:
            print("{} мин {} сек".format(minutes, seconds))
    else:
        print("{} час {} мин {} сек".format(hour, minutes, seconds))
else:
    print("{} дн {} час {} мин {} сек".format(days, hour, minutes, seconds))
