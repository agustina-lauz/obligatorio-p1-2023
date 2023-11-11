from entities.empleados import Empleado


class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, equipo, score, nro_auto, titular):
        super().__init__(cedula, nombre, fecha_nacimiento,
                         nacionalidad, salario, cargo, equipo)
        self._score = score
        self._nro_auto = nro_auto
        self._titular = titular
        self._lesion = None
        self._cant_infracciones = None
        self._abandono = None
        self._errores_pits = None
        self._pts_campeonato = None

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
    def pts_campeonato(self):
        return self._pts_campeonato

    @pts_campeonato.setter
    def pts_campeonato(self, pts_campeonato):
        self._pts_campeonato = pts_campeonato

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
