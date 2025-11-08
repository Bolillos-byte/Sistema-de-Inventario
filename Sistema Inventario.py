import csv

def cargar_inventario():
    try:
        with open("inventario.csv", "r") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        return []

def guardar_inventario(data):
    with open("inventario.csv", "w", newline="") as f:
        csv.writer(f).writerows(data)

def agregar_producto():
    nombre = input("Nombre: ")
    codigo = input("Código: ")
    precio = input("Precio: ")
    stock = input("Stock: ")
    inventario = cargar_inventario()
    inventario.append([codigo, nombre, precio, stock])
    guardar_inventario(inventario)
    print("Producto agregado.")

def mostrar_inventario():
    for p in cargar_inventario():
        print(f"Código: {p[0]} | Nombre: {p[1]} | Precio: ${p[2]} | Stock: {p[3]}")

# Menú principal
while True:
    print("\n1. Agregar producto\n2. Ver inventario\n3. Salir")
    op = input("Opción: ")
    if op == "1":
        agregar_producto()
    elif op == "2":
        mostrar_inventario()
    elif op == "3":
        break