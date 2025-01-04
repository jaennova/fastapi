# Configuración Básica para Iniciar un Proyecto con FastAPI

FastAPI es un framework moderno y rápido para construir APIs con Python, basado en las mejores características de Python 3.6+ y herramientas estándar como Pydantic y Starlette.

En esta guía, aprenderás cómo configurar un proyecto básico con FastAPI, desde la instalación hasta la ejecución de un servidor de desarrollo.

## Requisitos Previos
- Python 3.7 o superior instalado en tu sistema.
- Un entorno virtual configurado (consulta [Configuración de un Entorno Virtual](#)).

## Instalación de FastAPI y Uvicorn
FastAPI requiere un servidor ASGI para ejecutarse. Uno de los más comunes es Uvicorn. Para instalarlos, ejecuta:

```bash
pip install fastapi uvicorn
```

## Crear la Estructura del Proyecto
Organiza tu proyecto de manera clara desde el inicio. Aquí tienes una estructura básica recomendada:

```
mi_proyecto/
├── app/
│   ├── main.py       # Punto de entrada de la aplicación
│   ├── routers/      # Rutas separadas por módulos (opcional)
│   ├── models/       # Modelos Pydantic o de base de datos (opcional)
│   └── __init__.py   # Indica que es un paquete Python
├── venv/             # Entorno virtual
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación del proyecto
```

### Crear el Archivo `main.py`
El archivo `main.py` es el punto de entrada principal para tu aplicación FastAPI. Crea un archivo `main.py` con el siguiente contenido básico:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}
```

## Ejecutar el Servidor de Desarrollo
Con el archivo `main.py` configurado, puedes ejecutar tu aplicación usando Uvicorn:

```bash
uvicorn app.main:app --reload
```

- `app.main` se refiere a la ruta del archivo y la instancia de la aplicación.
- `--reload` habilita la recarga automática del servidor al realizar cambios en el código.

Visita `http://127.0.0.1:8000` en tu navegador para ver tu API en acción.

## Documentación Automática
FastAPI genera automáticamente documentación interactiva para tus APIs:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Crear un Archivo `requirements.txt`
Para compartir las dependencias de tu proyecto, genera un archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Otros desarrolladores pueden instalar estas dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Buenas Prácticas
- **Usa entornos virtuales:** Mantén las dependencias aisladas por proyecto.
- **Estructura modular:** Divide tu aplicación en routers, modelos, y controladores para facilitar el mantenimiento.
- **Escribe pruebas:** Usa herramientas como `pytest` para probar tu aplicación.

---

Con esta configuración básica, estás listo para comenzar a desarrollar aplicaciones con FastAPI. En futuras secciones, exploraremos temas más avanzados como modelos, validaciones, seguridad, y bases de datos.
