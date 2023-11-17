from entities.empleados import Empleado


class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, score, nro_auto):
        super().__init__(cedula, nombre, fecha_nacimiento,
                         nacionalidad, salario, cargo)
        self._score = score
        self._nro_auto = nro_auto
        self._titular = True
        self._lesion = False
        self._cant_infracciones = 0
        self._abandono = False
        self._errores_pits = 0
        self._ptos_campeonato = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def nro_auto(self):
        return self._nro_auto

    @nro_auto.setter
    def nro_auto(self, nro_auto):
        self._nro_auto = nro_auto

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def lesion(self):
        return self._lesion

    @lesion.setter
    def lesion(self, lesion):
        self._lesion = lesion

    @property
    def cant_infracciones(self):
        return self._cant_infracciones

    @cant_infracciones.setter
    def imprevistos(self, cant_infracciones):
        self._cant_infracciones = cant_infracciones

    @property
    def abandono(self):
        return self._abandono

    @abandono.setter
    def abandono(self, abandono):
        self._abandono = abandono

    @property
    def errores_pits(self):
        return self._errores_pits

    @errores_pits.setter
    def errores_pits(self, errores_pits):
        self._errores_pits = errores_pits

    @property
    def ptos_campeonato(self):
        return self._ptos_campeonato

    @ptos_campeonato.setter
    def ptos_campeonato(self, ptos_campeonato):
        self._ptos_campeonato = ptos_campeonato
