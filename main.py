# ==== GESTIÓN DE PATENTES CON ÁRBOL BINARIO DE BÚSQUEDA ====

# Crea un nuevo nodo con la patente recibida y sin hijos
def crear_nodo(patente):
    return [patente, None, None]

# Inserta una nueva patente en el árbol binario de búsqueda
def insertar(raiz, patente):
    if raiz is None:      # Si el árbol está vacío, se crea un nodo nuevo
        return crear_nodo(patente)
    if patente == raiz[0]:  # Si la patente ya existe, no se agrega
        print(f"La patente {patente} ya existe!")
        return raiz
    elif patente < raiz[0]:  # Si la patente es menor, va a la izquierda
        raiz[1] = insertar(raiz[1], patente)  # Llamada recursiva a la izquierda
    else:  # Si la patente es mayor, va a la derecha
        raiz[2] = insertar(raiz[2], patente)  # Llamada recursiva a la derecha
    
    print("===============================")    
    mostrar_arbol(raiz)  # Muestra el árbol luego de insertar
    print("===============================") 
    return raiz

# Valida la patente y la agrega al árbol
def agregar_patente(raiz, patente):
    if not isinstance(patente, str):  # Verifica que la patente sea una cadena
        print("Error: la patente debe ser una cadena")
        return raiz
    patente = patente.upper().replace("", "")  # Convierte a mayúsculas (replace no hace nada acá)
    if len(patente) not in [6, 7]:  # Verifica que tenga 6 o 7 caracteres
        print("Error: formato inválido. Debe tener 6 o 7 caracteres.")
        return raiz
    return insertar(raiz, patente)

# Muestra el árbol visualmente con indentación
def mostrar_arbol(raiz, nivel=0, prefijo=""):
    if raiz is not None:  # Si el nodo existe
        mostrar_arbol(raiz[2], nivel + 1, prefijo="    " * nivel + "D--> ")  # Muestra derecha
        print(prefijo + raiz[0])  # Muestra el nodo actual
        mostrar_arbol(raiz[1], nivel + 1, prefijo="    " * nivel + "I--> ")  # Muestra izquierda

# Calcula la profundidad (altura) del árbol
def profundidad(raiz):
    if raiz is None:  # Si el nodo es nulo, profundidad 0
        return 0
    # Devuelve 1 + el mayor valor entre la profundidad de izquierda y derecha
    return 1 + max(profundidad(raiz[1]), profundidad(raiz[2]))

# Recorre el árbol en orden: izquierda - nodo - derecha
def recorrido_inorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:  # Caso base
            return
        recorrido(nodo[1])        # Recorre la izquierda
        resultado.append(nodo[0]) # Visita el nodo actual
        recorrido(nodo[2])        # Recorre la derecha

    recorrido(raiz)
    return resultado

# Recorre el árbol en preorden: nodo - izquierda - derecha
def recorrido_preorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:  # Caso base
            return
        resultado.append(nodo[0]) # Visita el nodo actual
        recorrido(nodo[1])        # Recorre la izquierda
        recorrido(nodo[2])        # Recorre la derecha

    recorrido(raiz)
    return resultado

# Recorre el árbol en postorden: izquierda - derecha - nodo
def recorrido_postorden(raiz):
    resultado = []

    def recorrido(nodo):
        if nodo is None:  # Caso base
            return
        recorrido(nodo[1])        # Recorre la izquierda
        recorrido(nodo[2])        # Recorre la derecha
        resultado.append(nodo[0]) # Visita el nodo actual

    recorrido(raiz)
    return resultado

# Función principal que muestra el menú y maneja las opciones
def main():
    raiz = None  # El árbol empieza vacío
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
                if patente.lower() == "exit":  # Si escribe "exit", vuelve al menú
                    break
                raiz = agregar_patente(raiz, patente)  # Intenta agregar la patente
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "2":
            print("\nÁrbol binario de búsqueda:")
            mostrar_arbol(raiz)  # Muestra el árbol actual
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "3":
            print("Profundidad del árbol:", profundidad(raiz))  # Muestra la profundidad
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "4":
            print("Recorrido INORDEN:", recorrido_inorden(raiz))  # Muestra recorrido inorden
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "5":
            print("Recorrido PREORDEN:", recorrido_preorden(raiz))  # Muestra recorrido preorden
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "6":
            print("Recorrido POSTORDEN:", recorrido_postorden(raiz))  # Muestra recorrido postorden
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7":
            print("Programa finalizado.")  # Finaliza el programa
            break

        else:
            print("Opción no válida. Intentá de nuevo.")  # Opción incorrecta
            input("\nPresioná Enter para volver al menú...")

# Llama a la función principal para iniciar el programa
main()
