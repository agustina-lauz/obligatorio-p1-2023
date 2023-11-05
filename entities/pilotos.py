from entities.empleados import Empleado


class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, equipo, score, nro_auto, titular, imprevistos, lesion=False):
        super().__init__(cedula, nombre, fecha_nacimiento,
                         nacionalidad, salario, cargo, equipo)
        self._score = score
        self._nro_auto = nro_auto
        self._pts_campeonato = None
        self._titular = titular
        self._lesion = lesion
        self._imprevistos = imprevistos

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
    def imprevistos(self):
        return self._imprevistos

    @imprevistos.setter
    def imprevistos(self, imprevistos):
        self._imprevistos = imprevistos
