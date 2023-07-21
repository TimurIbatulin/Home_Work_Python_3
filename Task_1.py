# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

originale = [1, 1, 'asd', 'dsa', 44, 'asd', 'dsa']
final_list = []
for mean in originale:
    if originale.count(mean) > 1:
        final_list.append(mean)
        originale.remove(mean)
print(final_list)

