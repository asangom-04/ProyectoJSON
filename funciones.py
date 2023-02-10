import json
with open('json.json', 'r') as file:
        base_datos = json.load(file)
        print(base_datos)


def listar_tablas(base_datos):
    tablas = base_datos['baseDatos']['TABLAS']
    for tabla in tablas:
        nombre = tabla['nombre']
        print(nombre)


def contar_productos(base_datos):
    cont=0
    tablas = base_datos["baseDatos"]["TABLAS"]
    for tabla in tablas:
        if tabla["nombre"] == "productos":
            cont=cont+1
    print("Número de productos registrados:")



def buscar_producto(base_datos):
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    tablas = base_datos["baseDatos"]["TABLAS"]
    for tabla in tablas:
        for producto in tablas:
            if producto["nombre"] == nombre_producto:
                print("Producto encontrado: ")
                print("Nombre: ", producto["nombre"])
                print("Descripción: ", producto["descripcion"])
                print("Precio: ", producto["precio"])
                print("Stock: ", producto["stock"])
                return
    print("Producto no encontrado")


buscar_producto(base_datos)
def mostrar_proveedores(base_datos):
    proveedores = [tabla for tabla in base_datos['TABLAS'] if tabla['nombre'] == 'proveedores']
    compras = [tabla for tabla in base_datos['TABLAS'] if tabla['nombre'] == 'compras']
    print("Proveedores registrados:")
    for proveedor in proveedores[0]['columnas']:
        print(" - Nombre: " + proveedor['nombre'])
        print("   Teléfono: " + proveedor['telefono'])
        print("   Email: " + proveedor['email'])
        print("   Dirección: " + proveedor['direcion'])
        compras_proveedor = [compra for compra in compras[0]['columnas'] if compra['proveedor_id'] == proveedor['id']]
        print("   Compras realizadas: " + str(len(compras_proveedor)))

def resumen_ventas(base_datos):
    fecha=input("Introduce la fecha: ")
    ventas = [tabla for tabla in base_datos['tablas'] if tabla['nombre'] == 'ventas']
    clientes = [tabla for tabla in base_datos['tablas'] if tabla['nombre'] == 'clientes']
    productos = [tabla for tabla in base_datos['tablas'] if tabla['nombre'] == 'productos']
    if not ventas or not clientes or not productos:
        print("No se encontraron datos en la base de datos")
        return

    ventas_fecha = [venta for venta in ventas[0]['columnas'] if venta['fecha'] == fecha]
    if not ventas_fecha:
        print("No se encontraron ventas en la fecha especificada")
        return

    resumen = []
    for venta in ventas_fecha:
        cliente_id = venta['cliente_id']
        producto_id = venta['producto_id']
        cantidad = venta['cantidad']
        
        cliente = [c for c in clientes[0]['columnas'] if c['id'] == cliente_id]
        producto = [p for p in productos[0]['columnas'] if p['id'] == producto_id]
        if not cliente or not producto:
            print("No se encontró el cliente o producto correspondiente a la venta")
            continue
        
        resumen.append({
            'cliente': cliente[0]['nombre'],
            'producto': producto[0]['nombre'],
            'cantidad': cantidad,
            'total': cantidad * producto[0]['precio']
        })
    
    print("Resumen de ventas del " + fecha)
    for item in resumen:
        print("Cliente: " + item['cliente'])
        print("Producto: " + item['producto'])
        print("Cantidad: " + str(item['cantidad']))
        print("Total: " + str(item['total']))
        print("")
