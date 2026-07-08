

juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}


def stock_plataforma(plataforma):
    total = 0
    for codigo in juegos:
        if juegos[codigo][1].lower() == plataforma.lower():
            total += inventario[codigo][1]
    print(f"El total de stock disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    encontrados = []
    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if p_min <= precio <= p_max and stock != 0:
            titulo = juegos[codigo][0]
            encontrados.append(f"{titulo}--{codigo}")

    encontrados.sort()

    if len(encontrados) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print(f"Los juegos encontrados son: {encontrados}")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in inventario:
        inventario[codigo][0] = nuevo_precio
        return True
    else:
        return False


def eliminar_juego(codigo):
    codigo = codigo.upper()
    if codigo in juegos:
        del juegos[codigo]
        del inventario[codigo]
        return True
    else:
        return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    codigo = codigo.upper()
    if codigo in juegos:
        return False
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo] = [precio, stock]
    return True


def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.upper() not in juegos

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_plataforma(plataforma):
    return plataforma.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion in ('E', 'T', 'M')

def validar_multiplayer(valor):
    return valor in ('s', 'n')

def validar_editor(editor):
    return editor.strip() != ""

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_stock(stock):
    try:
        return int(stock) >= 0
    except ValueError:
        return False



def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")


while True:
    mostrar_menu()
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        plataforma = input("Ingrese plataforma a consultar: ")
        stock_plataforma(plataforma)

    elif opcion == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min, p_max)

    elif opcion == "3":
        while True:
            codigo = input("Ingrese código del juego: ")

            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    else:
                        print("El precio debe ser un entero positivo")
                except ValueError:
                    print("El precio debe ser un entero positivo")

            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")

            repetir = input("¿Desea actualizar otro precio (s/n)?: ")
            if repetir.lower() != "s":
                break

    elif opcion == "4":
        codigo = input("Ingrese código del juego: ")
        titulo = input("Ingrese título: ")
        plataforma = input("Ingrese plataforma: ")
        genero = input("Ingrese género: ")
        clasificacion = input("Ingrese clasificación: ")
        multiplayer_str = input("¿Es multiplayer? (s/n): ")
        editor = input("Ingrese editor: ")
        precio_str = input("Ingrese precio: ")
        stock_str = input("Ingrese stock: ")

        if not validar_codigo(codigo):
            print("El código no es válido o ya existe")
        elif not validar_titulo(titulo):
            print("El título no es válido")
        elif not validar_plataforma(plataforma):
            print("La plataforma no es válida")
        elif not validar_genero(genero):
            print("El género no es válido")
        elif not validar_clasificacion(clasificacion):
            print("La clasificación debe ser 'E', 'T' o 'M'")
        elif not validar_multiplayer(multiplayer_str):
            print("Debe ingresar 's' o 'n'")
        elif not validar_editor(editor):
            print("El editor no es válido")
        elif not validar_precio(precio_str):
            print("El precio debe ser un entero mayor que cero")
        elif not validar_stock(stock_str):
            print("El stock debe ser un entero mayor o igual a cero")
        else:
            multiplayer = multiplayer_str == "s"
            precio = int(precio_str)
            stock = int(stock_str)
            if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
                print("Juego agregado")
            else:
                print("El código ya existe")

    elif opcion == "5":
        codigo = input("Ingrese código del juego: ")
        if eliminar_juego(codigo):
            print("Juego eliminado")
        else:
            print("El código no existe")

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida")