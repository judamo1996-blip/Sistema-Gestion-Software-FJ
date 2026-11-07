from entidades import Entidad


class Cliente(Entidad):
    """Clase que representa a un cliente con su información personal."""

    def __init__(self, nombre, apellido, correo, telefono):

        # Validar que todos los datos sean cadenas de texto
        if not all(isinstance(dato, str) for dato in
                   (nombre, apellido, correo, telefono)):
            raise ValueError("Todos los datos deben ser textos.")

        # Eliminar espacios al principio y al final
        nombre = nombre.strip()
        apellido = apellido.strip()
        correo = correo.strip()
        telefono = telefono.strip()

        # Validar campos obligatorios
        if not all((nombre, apellido, correo, telefono)):
            raise ValueError("Todos los campos son obligatorios.")

        # Validar correo electrónico
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo electrónico inválido.")

        # Validar teléfono
        if not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("Número de teléfono inválido.")

        # Encapsular los atributos
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_informacion(self):
        """Devuelve la información del cliente."""
        return (
            f"Cliente: {self.__nombre} {self.__apellido}, "
            f"Correo: {self.__correo}, "
            f"Teléfono: {self.__telefono}"
        )
