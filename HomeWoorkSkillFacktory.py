def filter(func, cont):
    outp = []
    for x in cont: # проходим циклом по итерируемому объекту
        if func(x): # проверяем условие для каждого элемента
            outp.append(x) # если True, добавляем в новый список
    return outp
def positive(x):
    return x %2 == 0  #

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]