import csv
import json

def cargar_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        return {"nombre_negocio": "Negocio", "moneda": "MXN"}

config = cargar_config()

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
    print("✅ Producto agregado.")

def mostrar_inventario():
    inventario = cargar_inventario()
    print("\n📦 Inventario actual:")
    for p in inventario:
        print(f"Código: {p[0]} | Nombre: {p[1]} | Precio: ${p[2]} {config['moneda']} | Stock: {p[3]}")

def buscar_producto():
    clave = input("Buscar por nombre o código: ").lower()
    inventario = cargar_inventario()
    encontrados = [p for p in inventario if clave in p[0].lower() or clave in p[1].lower()]
    if encontrados:
        for p in encontrados:
            print(f"Código: {p[0]} | Nombre: {p[1]} | Precio: ${p[2]} | Stock: {p[3]}")
    else:
        print("❌ Producto no encontrado.")

def menu():
    print(f"\n🧾 {config['nombre_negocio']} - Sistema de Inventario")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Salir")

while True:
    menu()
    opcion = input("Opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        print("👋 Cerrando sistema.")
        break
    else:
        print("⚠️ Opción inválida.")