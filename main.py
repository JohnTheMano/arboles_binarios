#arboles-patentes
def agregar_patente(raiz,patente):
    if not isinstance (patente, str):
        print("Error: la patente debe ser una cadena")
        return raiz
    patente=patente.upper().replace("","")
    if len(patente) not in [6, 7]:
        print("Error: formato inválido. Debe tener 6 o 7 caracteres.")
        return raiz
    return insertar(raiz, patente)

def mostrar_arbol(raiz, nivel=0, prefijo=""):
    if raiz is not None:
        mostrar_arbol(raiz[2], nivel + 1, prefijo="    " * nivel + "D--> ")
        print(prefijo + raiz[0])
        mostrar_arbol(raiz[1], nivel + 1, prefijo="    " * nivel + "I--> ")


def profundidad(raiz):
    if raiz is None:
        return 0
    return 1 + max(profundidad(raiz[1]), profundidad(raiz[2]))