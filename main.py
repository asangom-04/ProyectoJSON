import funciones
import json

with open('json.json', 'r') as file:
        base_datos = json.load(file)
        #return base_datos
        #print(base_datos)
        


def mostrar_menu():
    print("Menú de opciones")
    print("1. Listar tablas")
    print("2. Contar productos")
    print("3. Buscar producto")
    print("4. Mostrar proveedores")
    print("5. Resumen de ventas")
    print("0. Salir")

while True:
    
    mostrar_menu()
    opcion = input("Introduce la opción: ")
    if opcion == '1':
        funciones.listar_tablas(base_datos)
    elif opcion == '2':
        funciones.contar_productos(base_datos)
    elif opcion == '3':
        funciones.buscar_producto(base_datos)
    
    elif opcion == '4':
        funciones.mostrar_proveedores(base_datos)
    elif opcion == '5':
        funciones.resumen_ventas(base_datos)
    elif opcion == '0':
        break
    else:
        print("Opción inválida")
