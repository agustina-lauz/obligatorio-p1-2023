
class Imprevistos:
    def __init__(self, nombre_piloto, nombre_imprevisto, dto_score):
        self.nombre_piloto = nombre_piloto
        self.nombre_imprevisto = nombre_imprevisto
        self.dto_score = dto_score

    @property   
    def nombre_piloto(self):
        return self._nombre_piloto
    
    @nombre_piloto.setter
    def nombre_piloto(self, nombre_piloto):
        self._nombre_piloto = nombre_piloto

    @property
    def nombre_imprevisto(self):
        return self._nombre_imprevisto
    
    @nombre_imprevisto.setter
    def nombre_imprevisto(self, nombre_imprevisto):
        self._nombre_imprevisto = nombre_imprevisto

    @property
    def dto_score(self):
        return self._dto_score
    
    @dto_score.setter
    def dto_score(self, dto_score):
        self._dto_score = dto_score