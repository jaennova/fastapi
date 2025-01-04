## Resumen de Variables de Entorno en FastAPI

Para profundizar en el uso de variables de entorno con FastAPI, puedes acceder a la sección correspondiente en la documentación oficial: [https://fastapi.tiangolo.com/es/tutorial/settings-and-environment-variables/](https://fastapi.tiangolo.com/es/tutorial/settings-and-environment-variables/). 

**¿Qué son las variables de entorno?**

Las variables de entorno, también conocidas como "**env vars**", son variables que viven **fuera del código** de Python, en el **sistema operativo**.  Pueden ser leídas por tu código de Python, así como por otros programas. Son útiles para:

* Manejar **configuraciones** de aplicaciones.
* Formar parte de la **instalación** de Python.

**¿Cómo se crean y usan las variables de entorno?**

Se pueden **crear y usar directamente desde la terminal**, sin necesidad de Python. 

**Ejemplo en Linux/macOS:**

```bash
# Crear la variable de entorno MY_NAME
export MY_NAME="Wade Wilson" 

# Usar la variable de entorno
echo "Hola $MY_NAME"
# Salida: Hola Wade Wilson
```

**Ejemplo en Windows:**

```powershell
# Crear la variable de entorno MY_NAME
$Env:MY_NAME = "Wade Wilson"

# Usar la variable de entorno
echo "Hola $Env:MY_NAME"
# Salida: Hola Wade Wilson
```

**¿Cómo se leen las variables de entorno en Python?**

Puedes leer variables de entorno en Python usando la función `os.getenv()`.

**Ejemplo:**

```python
import os

name = os.getenv("MY_NAME", "Mundo")
print(f"Hola {name} desde Python")
```

Si la variable de entorno `MY_NAME` no está definida, el código usará el valor por defecto "Mundo".

**Tipos y validación:**

Es importante recordar que las variables de entorno solo pueden manejar **strings de texto**. Cualquier conversión a otro tipo de dato o validación debe hacerse en el código Python.

**Variable de entorno especial: PATH**

La variable de entorno **PATH** es utilizada por los sistemas operativos para **encontrar programas ejecutables**.  Su valor es una lista de directorios separados por ":" (Linux/macOS) o ";" (Windows).

**Ejemplo en Linux/macOS:**

```
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

**Ejemplo en Windows:**

```
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32
```

Cuando ejecutas un comando en la terminal, el sistema busca el programa en cada uno de los directorios listados en la variable PATH.

**Conclusión:**

Las variables de entorno son una herramienta poderosa para manejar configuraciones y ajustes en tus aplicaciones Python.  Recuerda que la documentación oficial de FastAPI te ofrece información detallada sobre su uso y mejores prácticas. 
