from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional

class Contact(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=8, max_length=8)
    website: Optional[HttpUrl] = Field(None, max_length=100)


# Tipos de datos
# str: Cadena de texto
# int: Número entero
# float: Número decimal
# bool: Valor booleano
# datetime.datetime: Fecha y hora
# datetime.date: Fecha
# datetime.time: Hora
# list: Lista
# dict: Diccionario
# set: Conjunto
# decimal.Decimal: Número decimal

# Aleatorios
# random.random(): Número aleatorio entre 0 y 1

# valores nulos
# None: Valor nulo en Python
# Optional[T]: Valor nulo o de tipo T
# Optional[datetime.date]: Valor nulo o de tipo datetime.date

# Validaciones Numéricas
# validacion gt  greater than, valores mayores a #
# validacion ge  greater than or equal, valores mayores o iguales a #
# validacion lt  less than, valores menores a #
# validacion le  less than or equal, valores menores o iguales a #

# Validaciones de Cadenas
# validacion min_length  longitud mínima de la cadena
# validacion max_length  longitud máxima de la cadena
# validacion pattern  expresión regular que debe cumplir la cadena

# Validaciones de Listas
# validacion min_items  cantidad mínima de elementos en la lista
# validacion max_items  cantidad máxima de elementos en la lista
# validacion unique_items  todos los elementos de la lista deben ser únicos

# Validaciones de Fechas
# validacion gt  greater than, fechas mayores a #
# validacion ge  greater than or equal, fechas mayores o iguales a #
