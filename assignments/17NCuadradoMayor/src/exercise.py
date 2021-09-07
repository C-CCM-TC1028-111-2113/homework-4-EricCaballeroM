

def main():
    #Escribe tu código debajo de esta línea
    #Número al cuadrado mayor que N

n=int(input("escribe un número: "))
a=0

while a**2<n:
    a+=1
    if a**2>n:
       break
print(a)
    pass

if __name__=='__main__':
    main()
