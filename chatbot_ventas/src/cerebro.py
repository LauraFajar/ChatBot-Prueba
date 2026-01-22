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
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
            print("⚠️ ADVERTENCIA: No se encontró GEMINI_API_KEY. Usando modo 'básico' sin IA.")

    def procesar_mensaje(self, mensaje_usuario):
        """
        Esta es la lógica principal.
        En un sistema real, aquí usaríamos 'Function Calling' de la IA.
        Para esta prueba, haremos una lógica híbrida simple.
        """
        mensaje = mensaje_usuario.lower()
        
        # 1. Detección de intención básica (Simulando lo que haría la IA para decidir herramientas)
        if "precio" in mensaje or "cuánto cuesta" in mensaje or "buscar" in mensaje or "tienes" in mensaje:
            # Extraer posible nombre del producto (muy simplificado)
            palabras_clave = ["lavadora", "nevera", "licuadora", "televisor", "microondas", "sony", "samsung", "lg", "oster", "haceb"]
            producto_buscado = next((palabra for palabra in palabras_clave if palabra in mensaje), None)
            
            if producto_buscado:
                resultados = self.inventario.buscar_producto(producto_buscado)
                if resultados:
                    respuesta = "🔍 **Esto es lo que encontré en bodega:**\n"
                    for p in resultados:
                        estado = "✅ Disponible" if p['stock'] > 0 else "❌ Agotado"
                        respuesta += f"- {p['nombre']}: ${p['precio']:,.0f} ({estado})\n"
                    respuesta += "\n¿Te gustaría agregar alguno al carrito?"
                    return respuesta
                else:
                    return f"No encontré nada relacionado con '{producto_buscado}' en el inventario."
                    
        elif "comprar" in mensaje or "pagar" in mensaje or "carrito" in mensaje:
             # Simulación de cierre de venta
             return "🛒 Para procesar tu compra, necesito que confirmes el producto. (En el modo real, aquí generaríamos el link de pago: https://pagos-prueba.com/link-generado)"

        # 2. Si no es una orden directa de inventario, usamos la IA para conversar (Saludo, dudas generales, etc)
        if self.model:
            try:
                # Prompt del sistema para darle personalidad
                prompt_sistema = """
                Eres 'ElectroBot', un asistente de ventas amable y experto en electrodomésticos.
                Tu objetivo es vender. Sé persuasivo pero honesto.
                Habla en español, usa emojis y sé breve (es un chat de WhatsApp).
                El usuario te dijo: 
                """
                response = self.model.generate_content(prompt_sistema + mensaje_usuario)
                return response.text
            except Exception as e:
                return f"Error conectando con la IA: {str(e)}"
        
        return "Hola, soy el asistente de ventas. ¿En qué puedo ayudarte? (Configura tu API Key para hablar fluido)."

