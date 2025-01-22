# API CRUD Básica: Lista de Tareas (ToDo List)

## Descripción del Problema
Necesitas desarrollar una API REST básica utilizando FastAPI para gestionar una lista de tareas (ToDo List). Esta API permitirá crear, leer, actualizar y eliminar tareas, implementando las operaciones CRUD fundamentales.

## Requerimientos Funcionales
1. Crear una nueva tarea con título y descripción
2. Obtener una lista de todas las tareas
3. Obtener una tarea específica por su ID
4. Actualizar una tarea existente
5. Eliminar una tarea

## Estructura de Datos
Cada tarea (ToDo) debe contener:
- ID (generado automáticamente)
- Título
- Descripción
- Estado de completado (boolean)
- Fecha de creación

## Endpoints Requeridos

### 1. Crear Tarea (POST)
- Ruta: `/todos/`
- Cuerpo de la petición: título y descripción
- Respuesta: tarea creada con todos sus campos

### 2. Obtener Todas las Tareas (GET)
- Ruta: `/todos/`
- Respuesta: lista de todas las tareas

### 3. Obtener Tarea por ID (GET)
- Ruta: `/todos/{todo_id}`
- Respuesta: tarea específica o error 404 si no existe

### 4. Actualizar Tarea (PUT)
- Ruta: `/todos/{todo_id}`
- Cuerpo de la petición: campos a actualizar
- Respuesta: tarea actualizada o error 404

### 5. Eliminar Tarea (DELETE)
- Ruta: `/todos/{todo_id}`
- Respuesta: confirmación de eliminación o error 404

## Ejemplos de Uso

### Crear una Tarea
```http
POST /todos/
{
    "title": "Completar proyecto FastAPI",
    "description": "Desarrollar una API CRUD básica usando FastAPI"
}
```

### Respuesta Exitosa
```json
{
    "id": 1,
    "title": "Completar proyecto FastAPI",
    "description": "Desarrollar una API CRUD básica usando FastAPI",
    "completed": false,
    "created_at": "2025-01-19T10:00:00"
}
```

## Preparar el entorno

Crear el entorno virtual

```bash
python -m venv .envtodolist
.envtodolist\Scripts\Activate # para windows
```

instalar las dependencias para el proyecto
```bash
pip install fastapi uvicorn
```

levantar el servidor del proyecto

```bash
uvicorn todo_api:app --reload
```