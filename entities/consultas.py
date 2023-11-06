from entities.equipos import Equipo
from entities.empleados import Empleado
from entities.auto import Auto
from entities.pilotos import Piloto

 
 
class Consultas:
 
    def top_diez_pilotos(self, equipo):
        # Top 10 pilotos con más puntos en el campeonato puntaje
        pass
 
    def resumen_campeonato(self, equipo):
        # Resumen campeonato de constructores (equipos): El puntaje de un equipo
        #     corresponde a la suma de puntos que tiene cada uno de sus pilotos.
        pass
 
    def top_cinco_pilotos_mejores_pagos(self, equipo):
        # Top 5 pilotos mejores pago
        pass
 
    def top_tres_pilotos_mas_habilidosos(self, equipo):
        # Top 3 pilotos más habilidosos representada x el score personal de cada piloto
        pass
 
    def retornar_jefes_equipo(self, equipo):
        # Retornar jefes de equipo: Se debe retornar el jefe del equipo y el equipo que
        #    lidera, ordenados por nombre del jefe de manera ascendente.
        pass