def createList(n):
    return [i+1 for i in range(n)]
def persamaan_1(list):
    n = len(list)
    total_x = sum(list)
    y = 1/n * total_x
    return y
def persamaan_2(list, y):
    n = len(lst)
    total_z = 0
    for x in lst:
        total_z += (x - y)**2
    z = (1/(n-1)) * total_z
    return z
n = 7
lst = createList(n)
y = persamaan_1(lst)
z = persamaan_2(lst, y)
print("Hasil Persamaan (1):", y)
print("Hasil Persamaan (2):", z)