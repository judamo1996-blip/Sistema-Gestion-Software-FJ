from abc import ABC, abstractmethod


class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

"""1. creamos un primer servicio de reserva de sala para eventos"""

class ReservaSala(Servicio):
   
    def __init__(self, sala,tarifa):

        # Validamos que la tarifa sea un número y no un valor booleano.

        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ValueError("La tarifa debe ser un valor numérico.")

        if not isinstance(sala, str):
            raise ValueError("El nombre de la sala debe ser una cadena de texto.")

        if tarifa <= 0:
             # Comprobamos que la tarifa sea mayor que cero.

            raise ValueError("La tarifa debe ser mayor a cero.")

        if not sala.strip():
            # Comprobamos que el nombre de la sala no esté vacío.

            raise ValueError("El nombre de la sala no puede estar vacío.")
        
        # Guardamos los datos de la sala y su tarifa.
        self.sala = sala.strip()
        self.tarifa = tarifa

    def calcular_costo(self, duracion):
        # Validamos que la duración sea un valor numérico.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")
        
        if duracion <= 0:
            # Evitamos que la duración sea cero o negativa.
            raise ValueError("La duración debe ser mayor a cero.")
        
        # Calculamos el costo multiplicando la tarifa por las horas reservadas.
        return self.tarifa * duracion
    
    def describir_servicio(self):
        # Retornamos una descripción del servicio y su tarifa por hora.
        return f"Reserva de sala: {self.sala}, tarifa por hora: ${self.tarifa}"


"""2. creamos un segundo servicio de alquiler de equipo para eventos"""

class AlquilerEquipo(Servicio): 
    
    def __init__(self, equipo, tarifa):

        # Validamos que la tarifa sea numérica y no sea un booleano.
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ValueError("La tarifa debe ser un valor numérico.")

        # Comprobamos que el nombre del equipo sea texto.
        if not isinstance(equipo, str):
            raise ValueError("El nombre del equipo debe ser una cadena de texto.")

        # Validamos que la tarifa sea mayor a cero.
        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor a cero.")

        # Comprobamos que el nombre del equipo no esté vacío.
        if not equipo.strip():
            raise ValueError("El nombre del equipo no puede estar vacío.")

        # Guardamos los datos del equipo y su tarifa.
        self.equipo = equipo.strip()
        self.tarifa = tarifa

    def calcular_costo(self, duracion):

        # Validamos que la duración sea numérica.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")

        # Evitamos duraciones iguales o inferiores a cero.
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

        # Calculamos el costo según la tarifa y el tiempo de alquiler.
        return self.tarifa * duracion

    def describir_servicio(self):
        # Retornamos la descripción del equipo y su tarifa por hora.
        return f"Alquiler de equipo: {self.equipo}, tarifa por hora: ${self.tarifa}"

"""3. creamos un tercer servicio de asesoria especializada para eventos"""

class AsesoriaEspecializada(Servicio):
    

    def __init__(self, asesor, tarifa):

        # Validamos que la tarifa sea numérica y no sea un booleano.
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ValueError("La tarifa debe ser un valor numérico.")

        # Comprobamos que el nombre del asesor sea texto.
        if not isinstance(asesor, str):
            raise ValueError("El nombre del asesor debe ser una cadena de texto.")

        # Validamos que la tarifa sea mayor a cero.
        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor a cero.")

        # Comprobamos que el nombre del asesor no esté vacío.
        if not asesor.strip():
            raise ValueError("El nombre del asesor no puede estar vacío.")

        # Guardamos el nombre del asesor y su tarifa.
        self.asesor = asesor.strip()
        self.tarifa = tarifa

    def calcular_costo(self, duracion):

        # Validamos que la duración sea numérica.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")

        # Evitamos duraciones iguales o inferiores a cero.
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

        # Calculamos el costo según la tarifa y las horas de asesoría.
        return self.tarifa * duracion

    def describir_servicio(self):
        # Retornamos la descripción de la asesoría y su tarifa por hora.
        return f"Asesoría especializada: {self.asesor}, tarifa por hora: ${self.tarifa}"