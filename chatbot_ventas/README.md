# 🤖 ChatBot de Ventas - ElectroHogar

Este proyecto es un chatbot híbrido diseñado para automatizar las ventas y el servicio al cliente de una tienda de electrodomésticos ("ElectroHogar").

El bot combina **Lógica Basada en Reglas** (para control preciso del inventario y pagos) con **Inteligencia Artificial Generativa (Google Gemini)** para manejar conversaciones naturales cuando no se detectan comandos específicos.

## 🚀 Características

-   **🧠 Cerebro Híbrido**: Prioriza intenciones de compra y consulta de stock. Si no detecta una instrucción clara, usa Gemini para responder amablemente.
-   **🛒 Inventario en Tiempo Real**: Se conecta a **Google Sheets** para leer productos, precios y stock actualizados. (Cuenta con un sistema de respaldo en CSV si falla la conexión).
-   **💬 Integración con WhatsApp**: Funciona directamente en WhatsApp usando la API de Meta (WhatsApp Business API).
-   **🧪 Simulador Local**: Incluye un modo consola (`main_simulador.py`) para probar la lógica sin necesidad de configurar WhatsApp.
-   **💳 Simulación de Pagos**: Genera enlaces de pago simulados al detectar intenciones de compra.

## 📋 Requisitos

-   Python 3.8 o superior.
-   Una cuenta de Google Cloud (para la API de Sheets y Gemini).
-   Una cuenta de Meta Developers (para la API de WhatsApp).

## 🛠️ Instalación

1.  **Ubicación**: Asegúrate de estar dentro de la carpeta del proyecto:
    ```bash
    cd chatbot_ventas
    ```

2.  **Crear un entorno virtual** (recomendado):
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuración

1. **Variables de Entorno**:
   Crea un archivo `.env` en la raíz de `chatbot_ventas` con las siguientes claves:

   ```env
   # Credenciales de Google Gemini (IA)
   GEMINI_API_KEY=tu_api_key_de_google_ai

   # Credenciales de WhatsApp (Meta Developers) - Solo necesarias para app.py
   WHATSAPP_TOKEN=tu_token_de_acceso_whatsapp
   VERIFY_TOKEN=tu_token_personalizado_para_webhook
   PHONE_NUMBER_ID=tu_id_de_numero_de_telefono_whatsapp
   ```

2. **Google Sheets**:
   Para que el inventario funcione con Sheets, coloca tu archivo de credenciales de servicio como `credenciales_sheets.json` en la raíz. Si no existe, el sistema intentará usar un CSV local si está disponible o iniciará vacío.

## ▶️ Ejecución

### 1. Modo Simulador (Pruebas Locales)
Para probar la lógica del bot y la IA directamente en tu terminal (sin WhatsApp):

```bash
python main_simulador.py
```
*Tip: Intenta preguntar por "precio de la nevera" o di "quiero comprar".*

### 2. Servidor WhatsApp (Producción/Dev)
Para iniciar el servidor Webhook que conecta con WhatsApp:

```bash
python app.py
```
El servidor iniciará en `http://localhost:5000`.
*Nota: Para recibir mensajes de WhatsApp externamente, necesitarás exponer tu servidor local usando **ngrok** (o similar) y configurar esa URL pública en el panel de tu App en Meta.*

## 📂 Estructura del Proyecto

```text
chatbot_ventas/
├── src/
│   ├── cerebro.py       # Cerebro: Decide si usar Reglas o IA
│   └── inventario.py    # Servicio: Maneja Google Sheets y CSV
├── app.py               # API Flask para recibir Webhooks de WhatsApp
├── main_simulador.py    # Script CLI para pruebas rápidas
├── requirements.txt     # Librerías necesarias
├── credenciales_sheets.json # (Ignorado por git) Credenciales de Google
└── .env                 # (Ignorado por git) Claves secretas
```
