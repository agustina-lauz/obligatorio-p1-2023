

class Equipo:
    def __init__(self, nombre, modelo_auto):
        self._nombre = nombre
        self._modelo_auto = modelo_auto
        self._mecanicos = []
        self._jefe_equipo = None
        self._pilotos = []
        self._puntuacion = 0

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def modelo_auto(self):
        return self._modelo_auto

    @modelo_auto.setter
    def modelo_auto(self, modelo_auto):
        self._modelo_auto = modelo_auto

    @property
    def mecanicos(self):
        return self._mecanicos

    @mecanicos.setter
    def mecanicos(self, mecanicos):
        self._mecanicos = mecanicos

    @property
    def jefe_equipo(self):
        return self._jefe_equipo

    @jefe_equipo.setter
    def jefe_equipo(self, jefe_equipo):
        self._jefe_equipo = jefe_equipo

    @property
    def pilotos(self):
        return self._pilotos

    @pilotos.setter
    def pilotos(self, pilotos):
        self._pilotos = pilotos
