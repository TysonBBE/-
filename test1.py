n = int(input("Введите количество элементов массива 'A': "))
arr = []

print("Введите элементы массива:")
for i in range(n):
 arr.append(float(input()))

min_i = arr.index(min(arr))
max_i = arr.index(max(arr))

start = min(min_i, max_i) + 1
end = max(min_i, max_i)

result = sum(x for x in arr[start:end] if x < 0)

print("Сумма отрицательных элементов между min и max =", result)


