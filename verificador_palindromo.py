from cola_doble import ColaDoble


def verificadorPalindromo(cadena):

    cola_doble_caracteres = ColaDoble()
    for caracter in cadena:
        cola_doble_caracteres.agregarFinal(caracter)

    aun_iguales = True

    while cola_doble_caracteres.tamano() > 1 and aun_iguales:
        primero = cola_doble_caracteres.removerFrente()
        ultimo = cola_doble_caracteres.removerFinal()
        if primero != ultimo:
            aun_iguales = False

    return aun_iguales
