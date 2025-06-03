def contar_hasta_cero(n):
    if n <=0:
#caso base
        print("!boom!")
    else:
#caso recursivo
        print(n)
        contar_hasta_cero(n-1)
contar_hasta_cero(5)