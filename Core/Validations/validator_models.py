import re

class ValidatorModels:
    # Validar espcaios en blanco
    @staticmethod
    def not_contains_space(value, name):
        if " " not in value:
            raise ValueError(f"El valor de {name} no debe contener espacios")
        return value

    # Validar que el valor no esté vacío
    @staticmethod
    def not_empty(value, name):
        if len(value) == 0:
            raise ValueError(f"El valor de {name} no debe estar vacío")
        return value

    # Validar que el valor sea un número
    @staticmethod
    def is_number(value, name):
        if not value.isdigit():
            raise ValueError(f"El valor de {name} debe ser un número")
        return value

    # Validar que el valor sea un correo electrónico, con un regex
    @staticmethod
    def is_email(value, name):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError(f"El valor de {name} debe ser un correo electrónico")
        return value

    # Validar que el valor sea un número de teléfono, con un regex de 8 dígitos Costa Rica
    @staticmethod
    def is_phone(value, name):
        if not re.match(r"^\d{8}$", value):
            raise ValueError(
                f"El valor de {name} debe ser un número de teléfono de 8 dígitos"
            )
        return value

    # validar que la contraseña tenga al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número
    @staticmethod
    def is_password(value, name):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$", value):
            raise ValueError(
                f"El valor de {name} debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número"
            )
        return value

    # Validar que el valor sea una fecha, con un regex de formato dd/mm/yyyy
    @staticmethod
    def is_date(value, name):
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", value):
            raise ValueError(
                f"El valor de {name} debe ser una fecha con el formato dd/mm/yyyy"
            )
        return value

    # Validar que el valor sea un número decimal, con un regex
    @staticmethod
    def is_decimal(value, name):
        if not re.match(r"^\d+\.\d+$", value):
            raise ValueError(f"El valor de {name} debe ser un número decimal")
        return value

    # Validar que el valor sea un número entero positivo, con un regex
    @staticmethod
    def is_positive_integer(value, name):
        if not re.match(r"^\d+$", value):
            raise ValueError(f"El valor de {name} debe ser un número entero positivo")
        return value

    # validar un minimo de caracteres
    @staticmethod
    def min_length(value, name, length):
        if len(value) < length:
            raise ValueError(
                f"El valor de {name} debe tener al menos {length} caracteres"
            )
        return value

    # validar un maximo de caracteres
    @staticmethod
    def max_length(value, name, length):
        if len(value) > length:
            raise ValueError(
                f"El valor de {name} debe tener como máximo {length} caracteres"
            )
        return value
