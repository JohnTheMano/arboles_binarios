def crear_nodo(patente):
    return [patente, None, None]

def insertar(raiz, patente):
    if raiz is None:      # Caso base de la recursividad
        return crear_nodo(patente)
    if patente == raiz[0]:
        print(f"La patente {patente} ya existe!")
        return raiz
    elif patente < raiz[0]:
        raiz[1] = insertar(raiz[1], patente)  # Llamada recursiva Izquierda
    else:
        raiz[2] = insertar(raiz[2], patente)  # Llamada recursiva Derecha
    print("===============================")    
    mostrar_arbol(raiz)
    print("===============================") 
    return raiz

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
    if raiz is not None:  # Caso base de la recursividad
        mostrar_arbol(raiz[2], nivel + 1, prefijo="    " * nivel + "D--> ")
        print(prefijo + raiz[0])
        mostrar_arbol(raiz[1], nivel + 1, prefijo="    " * nivel + "I--> ")
        



def profundidad(raiz):
    if raiz is None: # Caso base de la recursividad
        return 0
    return 1 + max(profundidad(raiz[1]), profundidad(raiz[2]))
    

def recorrido_inorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:  # Caso base de recursividad
            return
        recorrido(nodo[1])       # recorrer izquierda
        resultado.append(nodo[0]) # visitar nodo
        recorrido(nodo[2])       # recorrer derecha

    recorrido(raiz)
    return resultado


def recorrido_preorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:    # Caso base de recursividad
            return
        resultado.append(nodo[0]) # visitar nodo
        recorrido(nodo[1])       # recorrer izquierda
        recorrido(nodo[2])       # recorrer derecha

    recorrido(raiz)
    return resultado



def recorrido_postorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:    # Caso base de recursividad
            return
        recorrido(nodo[1])       # recorrer izquierda
        recorrido(nodo[2])       # recorrer derecha
        resultado.append(nodo[0]) # visitar nodo

    recorrido(raiz)
    return resultado

def main():
    raiz = None
    while True:
        print("\n====== MENU ======")
        print("1. Agregar patentes")
        print("2. Mostrar árbol")
        print("3. Ver profundidad del árbol")
        print("4. Recorrido INORDEN")
        print("5. Recorrido PREORDEN")
        print("6. Recorrido POSTORDEN")
        print("7. Salir")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            print("Ingresá patentes (escribí 'exit' para volver al menú):")
            while True:
                patente = input("Patente: ").strip()
                if patente.lower() == "exit":
                    break
                raiz = agregar_patente(raiz, patente)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "2":
            print("\nÁrbol binario de búsqueda:")
            mostrar_arbol(raiz)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "3":
            print("Profundidad del árbol:", profundidad(raiz))
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "4":
            print("Recorrido INORDEN:", recorrido_inorden(raiz))
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "5":
            print("Recorrido PREORDEN:", recorrido_preorden(raiz))
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "6":
            print("Recorrido POSTORDEN:", recorrido_postorden(raiz))
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intentá de nuevo.")
            input("\nPresioná Enter para volver al menú...")


main()