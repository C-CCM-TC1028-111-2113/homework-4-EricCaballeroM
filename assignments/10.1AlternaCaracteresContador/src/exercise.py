def main():
    #escribe tu código abajo de esta línea
    #Alterna Caracteres

n=int(input("dame un número: "))
a=0

while a<n:
   a+=1
   print(str(a)+"-#")
   if a<n:
       a+=1
       print(str(a)+"-%")
    pass

if __name__=='__main__':   
    main()
