

class Equipo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mecanicos = []
        self._jefe_equipo = None
        self._auto = None
        self._pilotos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

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
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, auto):
        self._auto = auto

    @property
    def pilotos(self):
        return self._pilotos

    @pilotos.setter
    def pilotos(self, pilotos):
        self._pilotos = pilotos
