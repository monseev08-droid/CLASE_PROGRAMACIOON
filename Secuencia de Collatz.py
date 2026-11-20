limite = 1000000
numero_ganador = 1
terminos_ganador = 1

for semilla in range(1, limite):
    actual = semilla
    contador = 1
    while actual != 1:
        if actual % 2 == 0:
            actual = actual // 2
        else:
            actual = 3 * actual + 1
        contador = contador + 1
    if contador > terminos_ganador:
        terminos_ganador = contador
        numero_ganador = semilla

print("Número inicial con la cadena más larga:", numero_ganador)
print("Cantidad de términos de la cadena:", terminos_ganador)