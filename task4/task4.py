"""
Дан массив целых чисел nums.
Напишите программу, выводящую минимальное количество ходов, требуемых для
приведения всех элементов к одному числу.
За один ход можно уменьшить или увеличить число массива на 1.
"""

name = input()
nums = []
res = 0

try:
    with open(name, encoding = "UTF-8") as file_in:
        for line in file_in:
            nums.append(int(line))
    while min(nums) != max(nums):
        avg = round(sum(nums)/len(nums))
        if min(nums) < avg:
            x = min(nums)
            ix = nums.index(x)
            while x != avg:
                x += 1
                res += 1
            nums[ix] = x
        elif max(nums) > avg:
            x = max(nums)
            ix = nums.index(x)
            while x != avg:
                x -= 1
                res += 1
            nums[ix] = x
    print(res)        
except FileNotFoundError:
    print("Файл не найден")
except ValueError:
    print("В файле не цифры")


    