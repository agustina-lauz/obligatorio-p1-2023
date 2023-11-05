

class Auto:
    def __init__(self, numero, modelo, anio, score):
        self._numero = numero
        self._modelo = modelo
        self._anio = anio
        self._score = score

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f'Numero: {self._numero}, Modelo: {self._modelo}, Año: {self._anio}, Score: {self._score}'

    def __repr__(self):
        return str(self)
