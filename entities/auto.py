

class Auto:
    def __init__(self, modelo, anio, score):
        self._modelo = modelo
        self._anio = anio
        self._score = score

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
