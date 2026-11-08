from datetime import date
from clientes import Cliente
from servicios import Servicio

"""Clase que representa una reservación de un servicio."""

class Reservacion:
    def __init__(self, cliente, servicio, fecha, duracion):

# Comprobamos que la duración sea un valor numérico y no un booleano.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")

# Verificamos que la duración sea mayor que cero.
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

# Comprobamos que el cliente y el servicio sean objetos de las clases correspondientes.
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ValueError("El cliente y el servicio deben ser instancias de las clases Cliente y Servicio, respectivamente.")

# Verificamos que la fecha recibida sea un objeto de tipo date.
        if not isinstance(fecha, date):
            raise ValueError("La fecha debe ser una instancia de la clase date.")

 # Guardamos los datos de la reservación.
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.duracion = duracion
        self.estado = "pendiente" # Toda reservación comienza con estado pendiente.

    def calcular_costo_total(self):
        return self.servicio.calcular_costo(self.duracion)

    def cambiar_estado(self, nuevo_estado):

# Comprobamos que el nuevo estado pertenezca a los estados permitidos.
        if nuevo_estado not in ["pendiente", "confirmada", "cancelada"]:
            raise ValueError("El estado debe ser 'pendiente', 'confirmada' o 'cancelada'.")

# Impedimos modificar una reservación que ya fue cancelada.
        if self.estado == "cancelada":
            raise ValueError("No se puede cambiar el estado de una reservación cancelada.")

# Impedimos regresar una reservación confirmada al estado pendiente.
        if self.estado == "confirmada" and nuevo_estado == "pendiente":
            raise ValueError("No se puede cambiar el estado de una reservación confirmada a pendiente.")

# Evitamos asignar nuevamente el mismo estado.
        if self.estado== nuevo_estado:
            raise ValueError("El nuevo estado es el mismo que el estado actual.")
        
        self.estado = nuevo_estado  # Actualizamos el estado de la reservación.


