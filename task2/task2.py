# Напишите программу, которая рассчитывает положение точки относительно
# окружности.
# Координаты центра окружности и его радиус считываются из файла 1

def read_info_circle(name):
    with open(name, encoding="UTF-8") as file_in:
        line = file_in.readline().split()
        x, y = float(line[0]),float(line[1])
        r = float(file_in.readline())
    return x, y, r
    
def read_info_coordinates(name):
    points = []
    with open(name, encoding = "UTF-8") as file_in:
        for line in file_in:
            x, y = map(float, line.split())
            points.append((x, y))
    return points 

def chek_is_in_circle(x, y, r, x1, y1):
    chek = (x - x1) **2 + (y - y1) **2 - r **2
    if chek == 0:
        return 0
    elif chek <= 0:
        return 1
    else:
        return 2
    

x, y, r = read_info_circle(input())
points = read_info_coordinates(input())
for point in points:
    res = chek_is_in_circle(x, y, r, point[0], point[1])
    print(res)