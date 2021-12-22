def cost_min(costs, proces_sed):
    max_cost = float('inf')
    for key in costs.keys():
        if (costs[key] < max_cost) and (key not in proces_sed):
            min_cost = costs[key]
            track.append(key)
            return key

def track_and_cost(parents, costs):
    track = []
    for p in reversed(list(parents)):
        if p == 'end':
            track.append(p)
        elif p == parents[track[len(track) - 1]]:
            track.append(p)
    track.append(parents[p])
    track_cost = costs[track[0]]
    return ('Продолжительность {}, Путь {}'. format(track_cost, track))

graph = {'start': {'a': 5, 'b': 2}, 'a': {'c': 4, 'd':2}, 'b': {'a': 8, 'd': 7},
         'c': {'end': 3, 'd': 6}, 'd': {'end': 1}, 'end': {}}  # граф

infinity = float("inf")
costs = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, 'end': infinity}  # цены вершин
parents = {'a': 'start', 'b': 'start', 'c': 'a', 'd': 'b', 'end': None}  # родители вершин
proces_sed = []  # список обработанных вершин
track =[]    #  окончательный путь

node = cost_min(costs, proces_sed)
while node is not None:
    cost = costs[node]  # цена вершины node
    childs = graph[node]  # потомки вершины node
    for nod in childs.keys():  # перебор потомков node
        new_cost = cost + childs[nod]  # расчет новой цены потомка
        if costs[nod] > new_cost:  # Если текущая цена costs[nod] большей новой
            costs[nod] = new_cost  # Устанавливаем новую минимальную цену для потомка nod
            parents[nod] = node   # Устанавливаем родителя для потомка nod

    proces_sed.append(node)  # Добавление обработанной вершины в список
    node = cost_min(costs, proces_sed)  # Новый шаг

print(parents)
print(costs)
print(track_and_cost(parents, costs))




