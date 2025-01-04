## Resumen de Entornos Virtuales en FastAPI

Para profundizar en el uso de entornos virtuales con FastAPI, puedes acceder a la sección correspondiente en la documentación oficial: [https://fastapi.tiangolo.com/es/tutorial/virtual-environments/](https://fastapi.tiangolo.com/es/tutorial/virtual-environments/). Este resumen te ayudará a comprender los puntos clave de la página.

**¿Por qué usar entornos virtuales?**

Los entornos virtuales son cruciales para evitar conflictos entre las dependencias de diferentes proyectos de Python. Permiten aislar los paquetes instalados para cada proyecto, asegurando que las diferentes versiones de un mismo paquete no interfieran entre sí. 

Imagina que tienes dos proyectos de API construidos con FastAPI, cada uno destinado a resolver problemas distintos. Llamemos a estos proyectos `"API de Recomendaciones de Películas"` y `"API de Procesamiento de Imágenes"`.

`API de Recomendaciones de Películas`: Esta API utiliza la versión 1.0 de la biblioteca Pandas para manipular datos de usuarios y películas.

`API de Procesamiento de Imágenes`: Esta API, por su parte, requiere la versión 2.0 de la misma biblioteca Pandas para aprovechar nuevas funcionalidades de optimización de imágenes.

 Si instalas ambos proyectos en el entorno global de Python, uno de ellos no funcionará correctamente. Además, podrías afectar el funcionamiento de programas del sistema que dependen de versiones específicas de Python.

**¿Cómo funcionan los entornos virtuales?**

Un entorno virtual es simplemente un directorio (generalmente llamado ".venv") que contiene una copia independiente del intérprete de Python y los paquetes instalados. Al activar un entorno virtual, modificas la variable de entorno `PATH` para que el sistema busque primero los programas en el directorio del entorno virtual. Esto asegura que al ejecutar `python` o `pip`, se utilicen las versiones del entorno virtual activo.

**Creando y usando un entorno virtual:**

1. **Crear un proyecto:** Crea un directorio para tu proyecto.
2. **Crear un entorno virtual:** Utiliza el módulo `venv` de Python para crear el entorno virtual dentro del directorio de tu proyecto:
```bash
 python -m venv .venv
 ```
3. **Activar el entorno virtual:** Ejecuta el script de activación dentro del directorio del entorno virtual:
```bash
 source .venv/bin/activate # (Linux/macOS)
 source .venv/Scripts/activate # (Windows)
```
4. **Instalar paquetes:** Una vez activado el entorno, puedes instalar los paquetes necesarios con `pip install`:
```bash
pip install fastapi[standard]
```

5. **Ejecutar tu programa:** Con el entorno virtual activado, ejecuta tu programa con 
```bash
python main.py
```
6. **Desactivar el entorno virtual:** Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con 
```bash
deactivate
```

**Alternativas:**

Existen herramientas que facilitan la gestión de entornos virtuales y dependencias. Una de ellas es **uv**, que se encarga de instalar Python, crear el entorno virtual, instalar paquetes y gestionar las dependencias del proyecto.

Para una mejor comprensión del funcionamiento interno de los entornos virtuales, se recomienda leer la sección completa de la documentación de FastAPI. 

**Recuerda:** los entornos virtuales son una buena práctica para cualquier proyecto de Python, no solo para FastAPI. Te ayudarán a mantener tus proyectos organizados y evitar conflictos entre dependencias. 
