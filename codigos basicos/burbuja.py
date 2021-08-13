lista = [3, 6, 12, 17, 15, 18, 5, 10, 9, 4, 7, 1, 2]
print(lista)
for i in range(len(lista)):
    j = len(lista) - 1
    while j >= i:
        if lista[j] < lista[j - 1]:
            temporal = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = temporal
        j -= 1
print(lista)
