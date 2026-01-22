import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.inventario import InventarioService

# Cargar variables de entorno (API KEY)
load_dotenv()

class Brain:
    def __init__(self):
        self.inventario = InventarioService()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.carrito = [] # Memoria simple para esta sesión
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            try:
                # Intentamos usar gemini-pro que es más estable en versiones v1beta legacy
                self.model = genai.GenerativeModel('gemini-pro')
            except:
                 self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
            print("⚠️ ADVERTENCIA: No se encontró GEMINI_API_KEY. Usando modo 'básico' sin IA.")

    def procesar_mensaje(self, mensaje_usuario):
        """
        Lógica híbrida: Reglas fijas + IA
        """
        mensaje = mensaje_usuario.lower()
        
        # 0. PRIORIDAD MÁXIMA: Intención de Compra
        if "comprar" in mensaje or "pagar" in mensaje or "carrito" in mensaje:
            # Simulación simple: Extraer monto aproximado o genérico
            # En un caso real, sumaríamos el carrito.
            link = self.inventario.crear_link_pago_simulado(2000000) 
            return f"🎉 ¡Excelente elección! \n\n🛒 Para finalizar tu compra de la nevera (o lo que lleves), ingresa aquí:\n👉 {link}\n\nCuando pagues, te pediré tus datos de envío."

        # 1. Palabras clave de intención de Búsqueda
        palabras_activacion = ["precio", "cuesta", "vale", "buscar", "busco", "quiero", "necesito", "tienes", "hay", "stock"]
        
        if any(palabra in mensaje for palabra in palabras_activacion):
            # Extraer posible nombre del producto
            # Lista de productos comunes en electrodomésticos para buscar coincidencia
            palabras_clave_productos = ["lavadora", "nevera", "licuadora", "televisor", "tv", "microondas", "sony", "samsung", "lg", "oster", "haceb", "estufa", "horno"]
            
            producto_buscado = next((p for p in palabras_clave_productos if p in mensaje), None)
            
            # Si no encontró una categoría obvia, intenta buscar la última palabra del mensaje (hack simple)
            if not producto_buscado and len(mensaje.split()) < 5:
                # Evitar usar palabras comunes como "una", "el", "yo" como productos
                ultima_palabra = mensaje.split()[-1]
                if len(ultima_palabra) > 3:
                    producto_buscado = ultima_palabra
            
            if producto_buscado:
                print(f"DEBUG: Buscando '{producto_buscado}' en Sheets...")
                resultados = self.inventario.buscar_producto(producto_buscado)
                if resultados:
                    respuesta = "🔍 **Encontré esto en el inventario:**\n"
                    for p in resultados:
                        # Manejo seguro de datos del Sheet
                        precio = p.get('precio', 0)
                        nombre = p.get('nombre', 'Producto')
                        stock = p.get('stock', 0)
                        estado = "✅ Disponible" if int(stock) > 0 else "❌ Agotado"
                        
                        # Formato de moneda
                        try:
                            respuesta += f"- {nombre}: ${float(precio):,.0f} ({estado})\n"
                        except:
                            respuesta += f"- {nombre}: ${precio} ({estado})\n"
                            
                    respuesta += "\n¿Te interesa alguno?"
                    return respuesta
                else:
                    pass # Cae al bloque de abajo (IA)

        # 2. IA Conversacional (Gemini fallback)
        if self.model:
            try:
                # Usamos una lista de modelos para probar cuál funciona
                response = self.model.generate_content(mensaje_usuario)
                return response.text
            except Exception as e:
                print(f"⚠️ Error IA: {e}")
                # Fallback amable si muere la IA
                return "¿Podrías repetir eso? Estoy buscando en el sistema... Prueba decir 'precio lavadora' o 'pagar'."
        
        return "No entendí bien. Prueba escribiendo 'buscar lavadora' o 'pagar'."

