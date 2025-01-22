## Hints Generales
- Comienza creando los modelos Pydantic antes de implementar los endpoints
- Utiliza una lista en memoria como almacenamiento temporal de las tareas
- Implementa una función auxiliar para buscar tareas por ID
- Considera usar `HTTPException` para manejar errores comunes

## Hints Específicos por Función

### Crear Tarea (POST /todos/)
- Usa `datetime.datetime.now()` para la fecha de creación
- Genera IDs únicos incrementales empezando desde 1
- Documentación útil: https://fastapi.tiangolo.com/tutorial/body/

### Obtener Todas las Tareas (GET /todos/)
- Devuelve la lista completa de tareas
- Considera implementar paginación más adelante
- Documentación útil: https://fastapi.tiangolo.com/tutorial/response-model/

### Obtener Tarea por ID (GET /todos/{todo_id})
- Usa `HTTPException` si el ID no existe
- Valida que el ID sea positivo
- Documentación útil: https://fastapi.tiangolo.com/tutorial/path-params/

### Actualizar Tarea (PUT /todos/{todo_id})
- Verifica la existencia de la tarea antes de actualizar
- Mantén la fecha de creación original
- Documentación útil: https://fastapi.tiangolo.com/tutorial/body-updates/

### Eliminar Tarea (DELETE /todos/{todo_id})
- Devuelve un mensaje de éxito tras la eliminación
- Usa el código de estado apropiado
- Documentación útil: https://fastapi.tiangolo.com/tutorial/response-status-code/