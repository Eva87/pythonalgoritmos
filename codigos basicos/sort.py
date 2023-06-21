lista = [3, 6, 12, 17, 15, 43, 38, 22, 19, 88, 66, 55, 76, 58, 33, 94, 95, 97, 98, 99, 59, 58, 45, 48, 24, 18, 5, 10, 9,
         4, 7, 1, 2]
print(lista)
lista=range (40)
print(list(lista))

def ordenamientoconteo(l, k):
    resultado = [0] * (len(l))
    c = [0] * (k + 1)
    numeroelementosiguales(l, c)
    numeroelementosmenores(c)
    for i in range(len(l) - 1, -1, -1):
        c[l[i]] -= 1
        resultado = [c[l[i]]] = l[i]
    return resultado


def numeroelementosiguales(l, c):
    for i in range(len(l)):
        c[l[i]] += 1


def numeroelementosmenores(c):
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]


ordenamientoconteo(lista, 25)
