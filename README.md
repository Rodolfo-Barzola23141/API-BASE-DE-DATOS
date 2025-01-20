# API de Predicción con FastAPI y SQLite

Esta  es mi API que proporciona un endpoint para realizar predicciones utilizando un modelo de regresión lineal simple. Esta API utiliza una base de datos SQLite para verificar la conexión y podría extenderse para almacenar datos. El objetivo principal es demostrar la creación de una API RESTful con FastAPI y la interacción básica con una base de datos.

## Requisitos que usé 

*   Python 3.7 o superior (Recomendado 3.9+)
*   pip (gestor de paquetes de Python)
*   Las dependencias se instalan con: `pip install -r requirements.txt`

## Instrucciones de Ejecución

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/Rodolfo-Barzola23141/API-BASE-DE-DATOS.git](https://github.com/Rodolfo-Barzola23141/API-BASE-DE-DATOS.git)
    ```

2.  Navega al directorio del proyecto:

    ```bash
    cd API-BASE-DE-DATOS
    ```

3.  Crea y activa un entorno virtual (recomendado):

    ```bash
    python3 -m venv .venv        # Crea el entorno virtual
    source .venv/bin/activate  # Activa el entorno en macOS/Linux
    .venv\Scripts\activate      # Activa el entorno en Windows
    ```

4.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    # O si no tienes el archivo requirements.txt (solo para desarrollo inicial):
    pip install fastapi uvicorn scikit-learn
    ```

5.  Ejecuta la API:

    ```bash
    uvicorn main:app --reload  # Para desarrollo (recarga automática)
    # o
    python -m uvicorn main:app --reload #en windows
    ```

## Endpoints

*   `/health` (GET): Verifica la conexión a la base de datos.
    *   Ejemplo de solicitud: `http://127.0.0.1:8000/health`
    *   Ejemplo de respuesta (éxito):
        ```json
        {"status": "success", "message": "Conexión a la base de datos exitosa."}
        ```
    *   Ejemplo de respuesta (error - si aplica):
        ```json
        {"status": "error", "message": "Error al conectar a la base de datos: <mensaje_de_error>"}
        ```

*   `/predict/{feature}` (GET): Realiza una predicción basada en la característica proporcionada.
    *   Ejemplo de solicitud: `http://127.0.0.1:8000/predict/2.5`
    *   Ejemplo de respuesta:
        ```json
        {"feature": 2.5, "prediction": 6.0}
        ```

## Documentación Interactiva

Puedes acceder a la documentación interactiva (Swagger UI) en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Y a la documentación Redoc en: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
