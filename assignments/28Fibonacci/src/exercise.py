
def main():
    #escribe tu código abajo de esta línea
    #Números de Fibonacci
def numeros(): 
    num=int(input('dame un numero entero positivo: '))

    a=0
    b=1

    for x in range(num-1):
        fib=a+b
        a=b
        b=fib
    return b

main=numeros()
print(main)
    pass

if __name__=='__main__':
    main()
