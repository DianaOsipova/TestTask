# Напишите программу, которая выводит путь, по которому, двигаясь интервалом 
# длины m по заданному массиву, концом будет являться первый элемент.
n = int(input())
m = int(input())

mas = [0] *n
for i in range(n):
    mas[i] = i + 1

current = 0

print(mas[current], end = "")
current = (current + m - 1) % n

while current != 0:
    print(mas[current], end = "")
    current = (current + m - 1) % n
