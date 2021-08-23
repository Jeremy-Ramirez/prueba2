
def hello(nombre='kike'):
    print('hello',nombre)


#hello('jeremy')
#hello()


def longitud(cadena):
    contador=0
    for i in cadena:
        contador=contador+1
    print(contador)

longitud('hola')
print(len('hola'))