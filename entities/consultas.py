from exceptions.valor_no_existe import ValorNoExiste

class Consultas:

    def top_diez_pilotos(self, pilotos_en_carrera):
        try:
            pilotos_ordenados = sorted(
                pilotos_en_carrera, key=lambda piloto: piloto.score_final, reverse=True)
            if len(pilotos_ordenados) < 10:
                raise ValorNoExiste("La lista tiene menos de 10 pilotos, no esta completa para realizar la funcion")
            else:
                top_diez = []
                for i, piloto in enumerate(pilotos_ordenados[:10], start=1):
                    top_diez.append(
                        f"{i}. {piloto.nombre} - {piloto.score_final} pts")

            return top_diez

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
            
            #agregue la funcion para que imprima: "la lista no esta completa para realizar la funcion" 
            #per dudo de q si hay menos pilotos igual se realize....? no entiendo la letra, No aclara

    def resumen_campeonato(self):

        try:
            resumen = []

            # for equipo in equipos:
            #     puntaje_equipo = sum(
            #         piloto.score_final for piloto in equipo.pilotos)
            #     resumen.append((equipo.nombre, puntaje_equipo))

            resumen_ordenado = sorted(
                resumen, key=lambda x: x[1], reverse=True)

            return resumen_ordenado
        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def top_cinco_pilotos_mejores_pagos(self):

        try:
            mejores_pagos = []

            for equipo in self._equipos:
                mejores_pagos.extend(equipo.pilotos)

            pilotos_ordenados = sorted(
                mejores_pagos, key=lambda piloto: piloto.salario, reverse=True)
            if len(pilotos_ordenados) < 5:
                raise ValorNoExiste("La lista tiene menos de 5 pilotos, no esta completa para realizar la funcion")
            else:
                top_cinco_pilotos = pilotos_ordenados[:5]

                return top_cinco_pilotos

        except ValorNoExiste:
            print("Uno o más datos ingresados son inválidos, intente nuevamente")

    def top_tres_pilotos_mas_habilidosos(self):

        try:
            total_pilotos = []

            pilotos_ordenados = sorted(
                total_pilotos, key=lambda piloto: piloto.score, reverse=True)
            
            if len(pilotos_ordenados) < 3:
                raise ValorNoExiste("La lista tiene menos de 3 pilotos, no esta completa para realizar la funcion")
            else: 
                top_tres = []
                for i, piloto in enumerate(pilotos_ordenados[:3], start=1):
                    top_tres.append((piloto.nombre, piloto.score))

                return top_tres

        except ValorNoExiste:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")

    def retornar_jefes_equipo(self):

        try:
            jefes_con_equipos = []

            for equipo in self.equipos:
                jefe_equipo = equipo.jefe_equipo
                if jefe_equipo is not None:
                    jefes_con_equipos.append(
                        (jefe_equipo, equipo))

            jefes_con_equipos.sort(key=lambda x: x[0].nombre)

            return jefes_con_equipos

        except ValueError:
            print(
                "Uno o más datos ingresados son inválidos, intente nuevamente")
