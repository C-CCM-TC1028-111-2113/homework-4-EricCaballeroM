def main():
    #escribe tu código abajo de esta línea
    #Promedio con Decisión
sum=0
div=0

while sum>=0:
    tot=float(input("ingrese un número: "))

    if tot<0:
        break

    sum=sum+tot
    div+=1

prom=sum/div
print(prom)

    pass
if __name__=='__main__':
    main()
