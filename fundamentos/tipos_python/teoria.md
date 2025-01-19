## Tipos en Python con FastAPI

Este documento resume el contenido sobre los tipos en Python y su uso con FastAPI, basado en la información de las fuentes proporcionadas, **incluyendo ejemplos de código para una mejor comprensión**.

**Introducción a los Tipos en Python**

Python admite "anotaciones de tipos", una sintaxis especial que permite declarar el tipo de una variable. Esto mejora el soporte de editores y herramientas, facilitando la detección de errores y el autocompletado. **FastAPI se basa completamente en estas anotaciones de tipos**.

**Motivación**

Las anotaciones de tipos ayudan a recordar los métodos disponibles para un tipo de dato. 

**Ejemplo sin tipos:**

```python
def get_full_name(first_name, last_name):
  full_name = first_name.title() + " " + last_name.title()
  return full_name

print(get_full_name("john", "doe"))
```

Al escribir este código, el editor no puede ofrecer sugerencias útiles para el método que convierte la primera letra a mayúscula.

**Ejemplo con tipos:**

```python
def get_full_name(first_name: str, last_name: str):
  full_name = first_name.title() + " " + last_name.title()
  return full_name

print(get_full_name("john", "doe"))
```

En este caso, al escribir `first_name.` y presionar Ctrl+Espacio, el editor mostrará una lista de métodos disponibles para el tipo `str`, incluyendo `title()`.

También permiten la detección temprana de errores al realizar operaciones incompatibles con el tipo de dato.

**Ejemplo sin tipos:**

```python
def get_name_with_age(name, age):
  name_with_age = name + " is this old: " + age
  return name_with_age
```

Este código no genera un error al escribirlo, pero fallará al ejecutarlo porque no se puede concatenar una cadena con un entero.

**Ejemplo con tipos:**

```python
def get_name_with_age(name: str, age: int):
  name_with_age = name + " is this old: " + age
  return name_with_age
```

En este caso, el editor marcará un error en la línea que intenta concatenar la cadena con el entero `age`, permitiendo corregirlo antes de la ejecución.

**Declaración de Tipos**

Las anotaciones de tipos se declaran principalmente como parámetros de función. Se pueden usar tipos simples como `str`, `int`, `float`, `bool` y `bytes`.

**Ejemplo:**

```python
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
  return item_a, item_b, item_c, item_d, item_e
```

También se pueden utilizar tipos genéricos como `list`, `tuple`, `set` y `dict` que contienen otros valores, usando el módulo `typing` para especificar los tipos internos.

**Ejemplos:**

* **Lista:** `list[str]` o `List[str]` (Python 3.8+) indica una lista de cadenas.
* **Tupla:** `tuple[int, int, str]` o `Tuple[int, int, str]` (Python 3.8+) indica una tupla con dos enteros y una cadena.
* **Conjunto:** `set[bytes]` o `Set[bytes]` (Python 3.8+) indica un conjunto de bytes.
* **Diccionario:** `dict[str, float]` o `Dict[str, float]` (Python 3.8+) indica un diccionario con claves de tipo cadena y valores de tipo flotante.

**Tipos especiales:**

* **Union:** Permite declarar que una variable puede ser de varios tipos.

  **Ejemplos:**

  * `Union[int, str]` (Python 3.6+) 
  * `int | str` (Python 3.10+)

* **Optional:**  Indica que un valor puede ser de un tipo o `None`.

  **Ejemplos:**

  * `Optional[str]` (Python 3.6+) 
  * `str | None` (Python 3.10+)

* **Clases:** Se puede usar una clase como tipo para indicar que una variable es una instancia de esa clase.

  **Ejemplo:**

  ```python
  class Person:
    def __init__(self, name: str):
      self.name = name
  
  def get_person_name(one_person: Person):
    return one_person.name
  ```

**Modelos Pydantic**

Pydantic es una librería que permite la validación de datos. Se definen modelos de datos como clases con atributos tipados. Pydantic valida los valores, los convierte al tipo correcto y proporciona un objeto con los datos validados. **FastAPI se basa en Pydantic para la validación de datos**.

**Ejemplo:**

```python
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str = "John Doe"
  signup_ts: datetime | None = None
  friends: list[int] = []

external_data = {
  "id": "123",
  "signup_ts": "2017-06-01 12:22",
  "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user) # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=
print(user.id) # > 123
```

**Anotaciones de Tipos con Metadata**

Python permite agregar metadata a las anotaciones de tipos usando `Annotated`.

**Ejemplos:**

* `Annotated[str, "this is just metadata"]` (Python 3.9+)
* `from typing_extensions import Annotated` y luego `Annotated[str, "this is just metadata"]` (Python 3.8+)

Esto no afecta el comportamiento de Python, pero **permite a FastAPI obtener información adicional para la gestión de la aplicación**.

**Beneficios de las Anotaciones de Tipos en FastAPI**

FastAPI utiliza las anotaciones de tipos para:

* Brindar soporte de editor y verificación de tipos.
* Definir requisitos para parámetros de solicitud, como parámetros de ruta, consulta, encabezados y cuerpo.
* Convertir los datos de la solicitud al tipo requerido.
* Validar los datos de la solicitud, generando errores automáticos para el cliente si los datos son inválidos.
* Documentar la API utilizando OpenAPI, que se utiliza para generar interfaces de documentación interactivas.
