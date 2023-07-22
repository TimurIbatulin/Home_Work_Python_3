# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

a = ('палатка', 'спальный мешок', 'посуда',)
v = ('спальный мешок', 'посуда', 'фонарик', 'пила',)
d = ('спальный мешок', 'пила', 'фонарик', 'надувная женьщина',)
task = {'Андрей': a, 'Вадим': v, 'Дима': d}
all_1 = set()
counter = []
for q in task:
    counter.append(q)
    for q1 in task[q]:
        all_1.add(q1)
print(f'Общий список вещей: {all_1}')
general = set()
unique = set()
second = set()
h = 1
for p in task:
    empti = set()
    for p1 in task[p]:
        empti.add(p1)
    for t in empti:
        if h > 2:
            h = 0
        if t in task[counter[h]]:
            general.add(t)
        else:
            unique.add(t)
for w in unique:
    for e in task:
        if w in task[e]:
            print(f'{w} - взял с собой {e}')
for u in general:
    for o in task:
        if u not in task[o]:
            print(f'{u} - не взял с собой {o}')