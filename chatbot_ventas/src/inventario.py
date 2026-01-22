import csv
import json
import os

class InventarioService:
    def __init__(self, filepath="chatbot_ventas/data/inventario.csv"):
        self.filepath = filepath
        self.productos = self._cargar_inventario()

    def _cargar_inventario(self):
        """Carga los productos desde el CSV simulando Google Sheets"""
        productos = []
        if not os.path.exists(self.filepath):
            return []
            
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir tipos de datos
                row['precio'] = float(row['precio'])
                row['stock'] = int(row['stock'])
                productos.append(row)
        return productos

    def buscar_producto(self, consulta):
        """Busca productos por nombre (palabra clave)"""
        resultados = []
        consulta = consulta.lower()
        for p in self.productos:
            if consulta in p['nombre'].lower() or consulta in p['descripcion'].lower():
                resultados.append(p)
        return resultados

    def verificar_stock(self, producto_id):
        """Devuelve el stock actual de un producto"""
        for p in self.productos:
            if str(p['id']) == str(producto_id):
                return p['stock']
        return 0

    def crear_link_pago_simulado(self, total):
        """Simula la creación de un link de pago"""
        return f"https://pagos-prueba.com/checkout?monto={total}"

# Prueba rápida si se ejecuta este archivo
if __name__ == "__main__":
    servicio = InventarioService()
    print(servicio.buscar_producto("Lavadora"))
