

class Empleado:
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo):
        self._cedula = cedula
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario
        self._cargo = cargo
        self._score = 0
        self._ptos_campeonato = 0

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def ptos_campeonato(self):
        return self._ptos_campeonato

    @ptos_campeonato.setter
    def ptos_campeonato(self, ptos_campeonato):
        self._ptos_campeonato = ptos_campeonato
