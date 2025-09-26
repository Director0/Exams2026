f = open("27_A_23766.txt")

# data = [[x, y] for x, y in map(float, f.readline().split())]
data = []

for s in f: # Собрать данные из файла в список типа: [x, y] - координаты всех точек
    lst = list(map(float, s.split()))
    data.append(lst) # Внести файл в список

def dist(p1, p2): # Расстояние м/ду 2мя точками
    return ((p1[0] - p2[0])**2 + ((p1[1] - p2[1])**2)) ** 0.5

def get_cluster(p0): # Собрать точки в кластер методом DBSCAN
    clst = [p for p in data if dist(p0, p) <= 1] # Берем произвольную точку класетра, и ищем ее соседей. Соседи - точки, расстояние до которых меньше 1, собираем их в список

    for a in clst: # Удалить из списка отобранные точки
        data.remove(a)

    clst1 = [get_cluster(p) for p in clst] # Берем соседа и производим рекурсивную ф-юю, то есть так же находим ее соседей, собираем в список
    clst += sum(clst1, []) # Убираем лишние скобки списка т.к. мы работали с координатами

    return clst # Возврат кластера

# /////////////////////////////////////////////////////////
def centroid(clst): # Найти сумму расстояний от какой то любой p1 кластера до всех, минимальная - значит точка == центроид кластера
    min_dist = 10**20
    for p1 in clst: # Выбрать любую p1
        sum_dist = 0

        for p2 in clst: # Сложить расстояние от нее до всех точек кластера
            sum_dist += dist(p1, p2)

        if sum_dist < min_dist: # Проверить на минимальность
            min_dist = sum_dist
            p_min = p1 # Отобрать мин знач

    return p_min # Вернуть мин знач

print(len(data))

clst1 = get_cluster(data[0])
clst2 = get_cluster(data[0])
cen1 = centroid(clst1)
cen2 = centroid(clst2)

print(int(min(cen1[0], cen2[0]) * 10000), int(min(cen1[1], cen2[1]) * 10000))
print(len(clst1), len(clst2))
