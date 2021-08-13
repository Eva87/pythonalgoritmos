lista=range (40)
print(list(lista))


def busquedadelbunariorecorrido(numeroelementos, inicio, final, valorabuscar):
    if inicio is final:
        return numeroelementos[inicio] is valorabuscar
    centro =((final-inicio)//2)+inicio
    if valorabuscar < numeroelementos[centro]:
        return busquedadelbunariorecorrido(numeroelementos,inicio, centro, valorabuscar)
    elif valorabuscar > numeroelementos[centro]:
        return busquedadelbunariorecorrido(numeroelementos,centro+1, final, valorabuscar)
    return True

def busquedabinaria(numeroelementos, valorabuscar):
    if numeroelementos is None or len(numeroelementos) == 0:
        return False
    return busquedadelbunariorecorrido(numeroelementos,0,len(numeroelementos)-1,valorabuscar)

print (busquedabinaria(lista,22))