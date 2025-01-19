# FastAPI Backend Learning 🚀

Este repositorio está diseñado para aprender FastAPI de manera práctica a través de proyectos incrementales. Cada proyecto se construye consultando secciones específicas de la documentación oficial de FastAPI, combinando teoría y práctica.

## Estructura del Repositorio 📚

### 1. `setup/`
Instrucciones esenciales para comenzar:
- **Entornos virtuales**: Configuración del ambiente de desarrollo
- **Variables de entorno**: Gestión de configuraciones
- **Setup de FastAPI**: Guía inicial

### 2. `fundamentos/`
Conceptos base necesarios:
- **Tipos en Python**: Ejercicios de tipado
- **Concurrencia y async/await**: Programación asíncrona
- **Conceptos básicos de FastAPI**

### 3. `proyectos/`
Proyectos prácticos organizados por nivel de complejidad:

#### Nivel Básico

##### 1. API CRUD Básica (ToDo List)
**Temas de la documentación:**
- Primeros Pasos
- Parámetros de Path
- Request Body
- Modelos de Response
- Códigos de Estado

##### 2. Sistema de Gestión de Biblioteca
**Temas de la documentación:**
- Parámetros de Query y Validaciones
- Modelos de Parámetros Query
- Cuerpo - Múltiples Parámetros
- Body - Campos
- Modelos Anidados

##### 3. Gestor de Notas Personales
**Temas de la documentación:**
- Validaciones de Strings
- Validaciones Numéricas
- Modelos Pydantic Básicos
- Tipos de Datos Básicos
- Manejo de Fechas

##### 4. Sistema de Registro de Estudiantes
**Temas de la documentación:**
- Enumeraciones
- Validaciones Personalizadas Básicas
- Modelos de Lista
- Relaciones Simples
- Respuestas HTTP Básicas

##### 5. API de Gestión de Tareas del Hogar
**Temas de la documentación:**
- Modelos con Campos Opcionales
- Valores por Defecto
- Validaciones Condicionales
- Respuestas Personalizadas
- Manejo de Errores Básico

##### 6. Catálogo de Películas
**Temas de la documentación:**
- Búsqueda y Filtrado Básico
- Ordenamiento
- Paginación Simple
- Modelos de Respuesta Múltiple
- Validación de Parámetros de Consulta

#### Nivel Intermedio

##### 7. API de Gestión de Productos
**Temas de la documentación:**
- Ejemplos de Request
- Tipos de Datos Extra
- Parámetros de Cookie/Header
- Modelos de Cookies/Header
- Validaciones Avanzadas

##### 8. Sistema de Reservas de Restaurante
**Temas de la documentación:**
- Response Models
- Form Data
- JSON Compatible Encoder
- Manejo de Estados
- Validaciones de Tiempo

##### 9. Plataforma de Compartir Archivos
**Temas de la documentación:**
- Manejo de Archivos
- Archivos Estáticos
- Manejo de Errores
- Path Operations
- Límites de Tamaño

##### 10. Sistema de Gestión de Inventario
**Temas de la documentación:**
- Transacciones Básicas
- Modelos Relacionados
- Validaciones de Negocio
- Respuestas Personalizadas
- Manejo de Estados Complejos

##### 11. API de Gestión de Proyectos
**Temas de la documentación:**
- Dependencias Básicas
- Modelos Anidados Complejos
- Validaciones entre Campos
- Estados y Transiciones
- Filtros Avanzados

##### 12. Sistema de Encuestas
**Temas de la documentación:**
- Formularios Dinámicos
- Validaciones Grupales
- Respuestas Agregadas
- Exportación de Datos
- Manejo de Versiones

##### 13. Plataforma de Recetas
**Temas de la documentación:**
- Búsqueda Avanzada
- Tags y Categorías
- Relaciones Muchos a Muchos
- Filtros Combinados
- Ordenamiento Múltiple

##### 14. Sistema de Reservas de Vuelos
**Temas de la documentación:**
- Validaciones de Disponibilidad
- Manejo de Fechas Avanzado
- Estados Complejos
- Confirmaciones por Email
- Caché Básico

##### 15. API de Red Social Básica
**Temas de la documentación:**
- Autenticación Simple
- Relaciones entre Usuarios
- Timeline Básico
- Notificaciones
- Privacidad Básica

##### 16. Plataforma de Aprendizaje
**Temas de la documentación:**
- Progreso del Usuario
- Contenido Estructurado
- Evaluaciones
- Estadísticas Básicas
- Reportes Simples



### 4. `extras/`
Recursos complementarios:
- **Tips y trucos**: Mejores prácticas
- **Enlaces útiles**: Recursos adicionales
- **Ejemplos**: Código de referencia

## Cómo Usar este Repositorio 🛠️

### Requisitos Previos
- Python 3.10+
- Conocimientos básicos de Python
- Editor de código (VS Code recomendado)

### Configuración Inicial
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/jaennova/fastapi.git
   cd fastapi
   ```

2. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Estructura de cada Proyecto
Cada proyecto incluye:
- **README.md**: Descripción y requisitos
- **theory.md**: Conceptos teóricos
- **hints.md**: Pistas para implementación
- **tests/**: Pruebas unitarias
- **src/**: Código fuente

## Recursos 📚
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/es/)
- [Tutorial de Python](https://docs.python.org/es/3/tutorial/)
- [Roadmap Backend](https://roadmap.sh/backend)

## Progreso de Aprendizaje ✅

| Proyecto | Estado | Conceptos Clave |
|----------|---------|----------------|
| Setup Inicial | ✅ Completado | Entorno, FastAPI basics |
| ToDo List | 🟡 En Progreso | CRUD, Path params |
| Biblioteca | ⚪ Pendiente | Query params, Models |
| Productos | ⚪ Pendiente | Headers, Cookies |
| ... | ... | ... |

---

¡Explora, aprende y construye con FastAPI! 🚀
