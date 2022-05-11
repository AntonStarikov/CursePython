array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
       if array[j] < array[idx_min]:
            idx_min = j
            counter += 1
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(counter)
print(array)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter=0
for i in range(1,len(array)):
    x=array[i]
    idx = i
    while idx>0 and array[idx-1]>x:
        counter += 1
        array[idx] = array[idx-1]
        idx-=1
    array[idx]=x
print(array)
print(counter)