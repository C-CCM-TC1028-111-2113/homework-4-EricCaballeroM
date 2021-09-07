
def main():
    #Escribe tu código debajo de esta línea
    #Triángulo de asteriscos

linea=int(input('dame un numero: '))

for n in range(linea):
    a=linea-n-1
    ast=1+n
    print(' '*a+'*'*ast)


    pass


if __name__=='__main__':
    main()
