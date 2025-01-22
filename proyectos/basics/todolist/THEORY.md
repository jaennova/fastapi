# Conceptos Teóricos para API CRUD con FastAPI

## 1. FastAPI y CRUD
FastAPI es un framework moderno para construir APIs con Python 3.7+ basado en estándares como OpenAPI (Swagger) y JSON Schema. CRUD son las operaciones básicas (Create, Read, Update, Delete) que toda API REST debería implementar.

## 2. Conceptos Clave

### Pydantic Models
Los modelos Pydantic se utilizan para:
- Validar datos de entrada
- Serializar/deserializar datos
- Generar documentación automática
```python
from pydantic import BaseModel
from datetime import datetime

class TodoCreate(BaseModel):
    title: str
    description: str
```

### Path Operations
FastAPI utiliza "decoradores" para definir rutas y métodos HTTP:
```python
@app.post("/todos/")
@app.get("/todos/{todo_id}")
```

### Status Codes
Los códigos de estado HTTP más comunes en esta API:
- 200: Operación exitosa
- 201: Recurso creado exitosamente
- 404: Recurso no encontrado
- 422: Error de validación

### Response Model
FastAPI permite definir el modelo de respuesta esperado:
```python
@app.get("/todos/{todo_id}", response_model=Todo)
```

## 3. Documentación Relevante

### FastAPI
- [Primeros Pasos](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/)

### Python
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)