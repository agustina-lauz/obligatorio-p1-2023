from entities.equipos import Equipo
from entities.empleados import Empleado
from entities.auto import Auto
from entities.pilotos import Piloto

 
 
class Consultas:
 
    def top_diez_pilotos(pilotos_en_carrera):
        try:
            pilotos_ordenados = sorted(
                pilotos_en_carrera, key=lambda piloto: piloto.score_final, reverse=True)

            for i, piloto in enumerate(pilotos_ordenados[:10], start=1):
                print(
                    f"{i}. {piloto.nombre} - {piloto.score_final} pts")

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
        

    def resumen_campeonato(self, equipo):
        # Resumen campeonato de constructores (equipos): El puntaje de un equipo
        #     corresponde a la suma de puntos que tiene cada uno de sus pilotos.
        pass
 
 
    def top_cinco_pilotos_mejores_pagos(_equipo_completo):
        try:
            pilotos_ordenados = sorted(
                _equipo_completo, key=lambda piloto: piloto.salario, reverse=True)

            for i, piloto in enumerate(pilotos_ordenados[:5], start=1):
                print(
                    f"{i}. {piloto.nombre} - Salario: {piloto.salario}")

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
            
 
    def top_tres_pilotos_mas_habilidosos(pilotos_en_carrera):
        try:
            pilotos_ordenados = sorted(
                pilotos_en_carrera, key=lambda piloto: piloto.score, reverse=True)

            for i, piloto in enumerate(pilotos_ordenados[:3], start=1):
                print(
                    f"{i}. {piloto.nombre} - {piloto.scorel} pts")

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
            
 
    def retornar_jefes_equipo(self, equipo):
        try:

            jefes_de_equipo = [
                empleado for empleado in self._equipo_completo if empleado.cargo == 0]

            if jefes_de_equipo:
                for jefe_equipo in jefes_de_equipo:
                    equipo_asignado = next(
                        (equipo['nombre'] for equipo in self._equipos if jefe_equipo in equipo['empleados']), None)
                    if equipo_asignado is not None:
                        print(
                            f"Jefe de equipo: {jefe_equipo.nombre}, Equipo: {equipo_asignado}")
                    else:
                        print(
                            f"Jefe de equipo: {jefe_equipo.nombre}, Sin equipo asignado")
            else:
                print("No hay jefes de equipo en el sistema.")

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
                           
        # Retornar jefes de equipo: Se debe retornar el jefe del equipo y el equipo que
        #    lidera, ordenados por nombre del jefe de manera ascendente.