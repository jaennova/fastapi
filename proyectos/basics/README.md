# Proyectos Básicos con FastAPI 🚀

Esta sección contiene una colección de proyectos básicos para aprender FastAPI de manera práctica. Cada proyecto está diseñado para cubrir conceptos específicos de la documentación oficial.

## Proyectos Incluidos 📚

### 1. API CRUD Básica (ToDo List)
- **Descripción**: API básica para gestionar tareas (ToDo List)
- **Conceptos**: Primeros Pasos, Parámetros de Path, Request Body, Modelos de Response, Códigos de Estado
- **Carpeta**: `01_todo_api/`

### 2. Sistema de Gestión de Biblioteca
- **Descripción**: API para gestionar libros y préstamos
- **Conceptos**: Parámetros de Query, Modelos de Parámetros Query, Cuerpo - Múltiples Parámetros
- **Carpeta**: `02_library_system/`

### 3. Gestor de Notas Personales
- **Descripción**: API para crear y gestionar notas personales
- **Conceptos**: Validaciones de Strings, Validaciones Numéricas, Modelos Pydantic Básicos
- **Carpeta**: `03_notes_manager/`

### 4. Sistema de Registro de Estudiantes
- **Descripción**: API para gestionar registros de estudiantes
- **Conceptos**: Enumeraciones, Validaciones Personalizadas Básicas, Modelos de Lista
- **Carpeta**: `04_student_registry/`

### 5. API de Gestión de Tareas del Hogar
- **Descripción**: API para organizar tareas domésticas
- **Conceptos**: Modelos con Campos Opcionales, Valores por Defecto, Validaciones Condicionales
- **Carpeta**: `05_home_tasks/`

### 6. Catálogo de Películas
- **Descripción**: API para gestionar un catálogo de películas
- **Conceptos**: Búsqueda y Filtrado Básico, Ordenamiento, Paginación Simple
- **Carpeta**: `06_movie_catalog/`

## Configuración del Entorno 🛠️

### Requisitos Previos
- Python 3.10+
- Editor de código (VS Code recomendado)
- Git instalado

### Pasos de Configuración

1. **Clonar el Repositorio**
```bash
git clone https://github.com/tuusuario/fastapi-learning.git
cd fastapi-learning/projects/basic
```

2. **Crear y Activar Entorno Virtual**
```bash
# En Linux/macOS
python -m venv .venv
source .venv/bin/activate

# En Windows
python -m venv .venv
.venv\Scripts\activate
```

3. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

## Estructura de cada Proyecto 📁

Cada proyecto sigue esta estructura común:
```
proyecto/
├── README.md         # Descripción específica del proyecto
├── theory.md         # Conceptos teóricos necesarios
├── hints.md          # Pistas para implementación
├── src/              # Código fuente
│   ├── main.py      # Punto de entrada
│   ├── models/      # Modelos Pydantic
│   └── routers/     # Rutas de la API
└── tests/           # Pruebas unitarias
```

## Ejecutar los Proyectos 🚀

1. **Navegar al Proyecto**
```bash
cd [nombre_proyecto]
```

2. **Ejecutar el Servidor**
```bash
uvicorn src.main:app --reload
```

3. **Acceder a la API**
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- Documentación alternativa: http://localhost:8000/redoc

## Pruebas ✅

Cada proyecto incluye pruebas unitarias. Para ejecutarlas:
```bash
pytest
```

## Documentación 📚

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/es/)
- [Tutorial de Python](https://docs.python.org/es/3/tutorial/)
- [Guía de Pydantic](https://docs.pydantic.dev/)

## Consejos para el Aprendizaje 💡

1. Lee el README.md específico de cada proyecto antes de comenzar
2. Revisa theory.md para entender los conceptos
3. Implementa la solución por tu cuenta
4. Usa hints.md si te atascas
5. Verifica tu implementación con las pruebas
6. Consulta la documentación oficial para profundizar

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias:
1. Haz fork del repositorio
2. Crea una rama para tus cambios
3. Envía un pull request

---

¡Feliz aprendizaje con FastAPI! 🎉
