# 🚀 Guía de Configuración: ElectroBot (Chatbot de Ventas)

¡Felicidades! Ya tienes el núcleo de tu chatbot creado en Python.
Esta versión funciona actualmente en **Modo Simulador de Terminal** con una base de datos local (CSV), pero está listo para conectarse al mundo real.

## 📋 1. Probar el Bot AHORA (Sin claves)
Como tu bot tiene un "Modo de Respaldo", puedes probarlo ya mismo.
1. Abre tu terminal en esta carpeta.
2. Ejecuta: `python main_simulador.py`
3. Escribe: "Hola", o "Busco una lavadora".
4. Verás cómo responde usando la base de datos local `data/inventario.csv`.

---

## 🧠 2. Conectar la Inteligencia Artificial (Gemini) - ¡GRATIS!
Para que el bot hable fluido y no sea robótico, necesitas la clave de Google.
1. Ve a: [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en **"Create API Key"**.
4. Copia esa clave larga (empieza por `AIza...`).
5. En esta carpeta, crea un archivo llamado `.env` y pega esto:
   ```
   GEMINI_API_KEY=Pega_Tu_Clave_Aqui
   ```

---

## 📱 3. Conectar WhatsApp (Cuando estés listo para probar en el celular)
Para esto necesitas registrarte como desarrollador en Meta.
1. Ve a [Meta for Developers](https://developers.facebook.com/).
2. Crea una app tipo "Business".
3. Busca el producto "WhatsApp" y actívalo.
4. En la sección **API Setup**, verás un "Test Number" (Número de prueba) y un "Temporary Access Token".
5. Necesitarás configurar un Webhook (esto requiere un servidor real o `ngrok`).
   * *Te recomendaría dominar primero la versión de terminal antes de meterte aquí, ya que Meta es estricto.*

---

## 📊 4. Conectar Google Sheets (Base de Datos Real)
Actualmente el bot lee `data/inventario.csv`. Para usar Sheets:
1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un proyecto nuevo y habilita la **Google Sheets API** y **Google Drive API**.
3. Crea una "Service Account" y descarga el archivo JSON de credenciales.
4. Comparte tu hoja de cálculo con el email raro que sale en ese JSON (`algo@tu-proyecto.iam.gserviceaccount.com`).
5. En Python, solo tendrías que cambiar el archivo `src/inventario.py` para usar `gspread` en lugar de `csv`.

---

## 📦 Estructura de Archivos
- `main_simulador.py`: El punto de entrada para probar en tu PC.
- `src/cerebro.py`: La lógica que decide qué contestar (usa IA o reglas).
- `src/inventario.py`: El encargado de buscar precios y stock.
- `data/inventario.csv`: Tu base de datos de prueba. ¡Edítalo para cambiar precios!
