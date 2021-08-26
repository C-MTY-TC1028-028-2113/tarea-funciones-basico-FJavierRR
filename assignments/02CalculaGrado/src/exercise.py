def calcula_grado(g):
    if g < 0.0 or g > 1.0:
        nota = "score incorrecto"
    elif g > 0.9:
        nota = "A"
    elif g > 0.8:
        nota = "B"
    elif g > 0.7:
        nota = "C"
    elif g > 0.6:
        nota = "D"
    else:
        nota = "F"
    return nota


def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
