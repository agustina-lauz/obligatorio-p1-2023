from exceptions.valor_no_existe import ValorNoExiste


class Consultas:

    def top_diez_pilotos(self, pilotos):

        try:
            pilotos_ordenados = sorted(
                pilotos, key=lambda piloto: piloto.ptos_campeonato, reverse=True)
            top_diez = []
            for i, piloto in enumerate(pilotos_ordenados[:10], start=1):
                top_diez.append(
                    f"{i}. {piloto.nombre} - {piloto.ptos_campeonato} pts")
            return top_diez

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def resumen_campeonato(self, equipos):

        try:
            resumen = []

            for equipo in equipos:
                score_campeonato = sum(
                    empleado.ptos_campeonato for empleado in equipo)
                resumen.append(
                    f"{equipo.nombre} - {score_campeonato} pts")

            resumen_ordenado = sorted(
                resumen, key=lambda x: x[1], reverse=True)

            return resumen_ordenado

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def top_cinco_pilotos_mejores_pagos(self, pilotos):

        try:
            pilotos_ordenados = sorted(
                pilotos, key=lambda piloto: piloto.salario, reverse=True)
            top_cinco = []
            for i, piloto in enumerate(pilotos_ordenados[:5], start=1):
                top_cinco.append(
                    f"{i}. {piloto.nombre} - USD {piloto.salario}")
            return top_cinco

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def top_tres_pilotos_mas_habilidosos(self, pilotos):

        try:

            pilotos_ordenados = sorted(
                pilotos, key=lambda piloto: piloto.score, reverse=True)
            top_tres = []
            for i, piloto in enumerate(pilotos_ordenados[:3], start=1):
                top_tres.append(
                    f"{i}. {piloto.nombre} - {piloto.score} pts")
            return top_tres

        except ValorNoExiste:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def retornar_jefes_equipo(self, jefes_equipo):

        try:

            jefes_ordenados = sorted(
                jefes_equipo, key=lambda jefes: jefes.nombre, reverse=False)
            jefes_equipos = []
            for jefe_equipo in jefes_ordenados:
                jefes_equipos.append(
                    f"{jefe_equipo.nombre} - {jefe_equipo.equipo}")
            return jefes_equipos

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
