from collections import defaultdict
from datos import Datos
from entities.auto import Auto
from entities.consultas import Consultas
from entities.empleados import Empleado
from entities.equipos import Equipo
from entities.pilotos import Piloto
from exceptions.valor_ya_existe import ValorYaExiste
# from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste


limites_cargo = {

    1: 2,  # pilotos titulares por equipo
    2: 1,  # pilotos reserva por equipo
    3: 8,  # mecanicos por equipo
    4: 1,  # jefes por equipo
}


class Menu:

    def __init__(self) -> None:
        self._empleados_registrados = []  # checked
        self._lista_de_autos = []  # checked
        self._equipos = []  # checked
        self.cant_empleados_equipo = defaultdict(
            lambda: defaultdict(list))
        self._cedulas_empleados = set()  # checked
        self._resultados_carrera = []  # checked

    def inicio(self) -> None:

        while True:
            print("Menu principal")
            print("Seleccione la opción del menú:")
            print("1. Alta de empleado")
            print("2. Alta de auto")
            print("3. Alta de equipo")
            print("4. Simular carrera")
            print("5. Realizar consultas")
            print("6. Finalizar programa")

            try:
                num_seleccionado = int(input("Ingrese número: "))
            except ValorNoExiste:
                print("El dato ingresado no es un número entero, intente nuevamente")
                continue

 # COMIENZA ALTA DE EMPLEADO
            if num_seleccionado == 1:
                print("Alta de empleado")

                try:
                    try:
                        cedula = Datos.set_cedula()
                        if cedula is None:
                            self.inicio()
                        if cedula in self._cedulas_empleados:
                            raise ValorYaExiste(
                                "La cédula ingresada ya existe, intente nuevamente")
                    except ValueError:
                        self.inicio()

                    nombre = Datos.set_nombre()
                    if nombre is None:
                        self.inicio()
                    fecha_nacimiento = Datos.set_fecha_nacimiento()
                    if fecha_nacimiento is None:
                        self.inicio()
                    nacionalidad = Datos.set_nacionalidad()
                    if nacionalidad is None:
                        self.inicio()
                    salario = Datos.set_salario()
                    if salario is None:
                        self.inicio()
                    cargo = Datos.set_cargo()
                    if cargo is None:
                        self.inicio()

                    if cargo in [1, 2]:
                        score = Datos.set_score()
                        nro_auto = Datos.set_nro_auto()
                        piloto = Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario,
                                        cargo, score, nro_auto)
                        if cargo == 1:
                            piloto.titular = True
                            self._cedulas_empleados.add(cedula)
                            self._empleados_registrados.append(piloto)
                            print("Piloto titular registrado correctamente")
                        else:
                            piloto.titular = False
                            self._empleados_registrados.append(piloto)
                            self._cedulas_empleados.add(cedula)
                            print("Piloto de reserva registrado correctamente")

                    elif cargo == 3:
                        score = Datos.set_score()
                        mecanico = Empleado(
                            cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
                        mecanico.score = score
                        self._empleados_registrados.append(mecanico)
                        self._cedulas_empleados.add(cedula)
                        print("Mecanico registrado correctamente")

                    elif cargo == 4:
                        jefe_equipo = Empleado(
                            cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
                        self._empleados_registrados.append(jefe_equipo)
                        self._cedulas_empleados.add(cedula)
                        print("Jefe de equipo registrado correctamente")

                except ValorNoExiste:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    self.inicio()
 # TERMINA ALTA DE EMPLEADO

 # COMIENZA ALTA DE AUTO
            elif num_seleccionado == 2:
                print("Alta de auto")

                try:
                    modelo = Datos.set_modelo()
                    if modelo is None:
                        self.inicio()
                    anio = Datos.set_anio()
                    if anio is None:
                        self.inicio()
                    score = Datos.set_score()
                    if score is None:
                        self.inicio()

                    auto = Auto(modelo, anio, score)
                    self._lista_de_autos.append(auto)
                    print("Auto registrado correctamente")

                except ValorNoExiste:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    self.inicio()
 # TERMINA ALTA DE AUTO

 # COMIENZA ALTA DE EQUIPO
            elif num_seleccionado == 3:
                print("Alta de equipo")

                try:
                    nombre_equipo = Datos.nombre_equipo()
                    modelo_auto = Datos.set_modelo()
                    auto_registrado = any(
                        auto.modelo == modelo_auto for auto in self._lista_de_autos)
                    if not auto_registrado:
                        print("El auto no está registrado.")
                        self.inicio()
                    equipo = Equipo(
                        nombre_equipo, modelo_auto)
                    empleados_equipo = Datos.empleados_por_equipo()

                    count_pilotos_titulares = 0
                    count_pilotos_reserva = 0
                    count_mecanicos = 0
                    count_jefes = 0

                    for i in empleados_equipo:
                        if i not in self._cedulas_empleados:
                            print(
                                f"La cédula {i} no se encuentra registrada en el sistema.")
                            print("No se pudo crear el equipo.")
                            self.inicio()
                        else:
                            empleado_en_equipo = False
                            for equipo_existente in self._equipos:
                                empleado_en_equipo = next(
                                    (empleado for empleado in equipo_existente.pilotos + [equipo_existente.jefe_equipo] + equipo_existente.mecanicos if empleado and getattr(empleado, 'cedula', None) == i), False)

                                if empleado_en_equipo:
                                    print(
                                        f"El empleado con cédula {i} ya pertenece a otro equipo.")
                                    print("No se pudo crear el equipo.")
                                    self.inicio()
                                elif not empleado_en_equipo:
                                    empleado_registrado = next(
                                        (empleado for empleado in self._empleados_registrados if empleado.cedula == i), None)
                                    if empleado_registrado and empleado_registrado.cargo == 1:
                                        if count_pilotos_titulares < limites_cargo[1]:
                                            equipo.pilotos.append(
                                                empleado_registrado)
                                            count_pilotos_titulares += 1
                                        else:
                                            print("Cupo de pilotos completo.")
                                            self.inicio()
                                    elif empleado_registrado and empleado_registrado.cargo == 2:
                                        if count_pilotos_reserva < limites_cargo[2]:
                                            equipo.pilotos.append(
                                                empleado_registrado)
                                            count_pilotos_reserva += 1
                                        else:
                                            print(
                                                "Cupo de pilotos reserva completo.")
                                            self.inicio()
                                    elif empleado_registrado and empleado_registrado.cargo == 3:
                                        if count_mecanicos < limites_cargo[3]:
                                            equipo.mecanicos.append(
                                                empleado_registrado)
                                            count_mecanicos += 1
                                        else:
                                            print("Cupo de mecanicos completo.")
                                            self.inicio()
                                    elif empleado_registrado and empleado_registrado.cargo == 4:
                                        if count_jefes < limites_cargo[4]:
                                            equipo.jefe_equipo = empleado_registrado
                                            count_jefes += 1
                                        else:
                                            print("Cupo de jefes completo.")
                                            self.inicio()


                    if count_pilotos_titulares + count_pilotos_reserva + count_mecanicos + count_jefes == 12:
                        self._equipos.append(equipo)
                        print("Equipo registrado correctamente")
                    else:
                        print("No se pudo crear el equipo, el equipo no tiene 12 empleados.")   #agregue, anda
                        self.inicio()
                

                except ValorNoExiste:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente")
                    self.inicio()
 # TERMINA ALTA DE EQUIPO

 # COMIENZA SIMULAR CARRERA
            elif num_seleccionado == 4:
                print("Simular carrera")

                # VALIDACIÓN DE CANTIDAD DE EMPLEADOS POR EQUIPO #
                # for equipo in self._equipos:
                #     if len(equipo.pilotos) < 3 or len(equipo.mecanicos) < 8 or equipo.jefe_equipo is None:
                #         print(NoRespetaMetodoDefinido(
                #             f"El equipo {equipo.nombre} no tiene un equipo completo de 12 empleados o no tiene jefe de equipo."))
                #         self.inicio()

                try:
                    # TOTAL DE PILOTOS DE TODOS LOS EQUIPOS #
                    total_pilotos_equipos = []
                    for equipo in self._equipos:
                        pilotos = equipo.pilotos
                        total_pilotos_equipos.extend(
                            [(equipo.nombre, piloto) for piloto in pilotos])

                    # REGISTRO DE PILOTOS LESIONADOS #
                    pilotos_lesionados = Datos.pilotos_lesionados()
                    pilotos_lesionados_con_equipo = []
                    for nro_auto in pilotos_lesionados:
                        piloto_equipo = next(
                            (piloto for piloto in total_pilotos_equipos if piloto.nro_auto == nro_auto), None)

                        if piloto_equipo:
                            pilotos_lesionados_con_equipo.append(
                                (piloto_equipo[1], piloto_equipo[0]))
                            piloto_equipo[1].lesionado = True
                        else:
                            print(ValorNoExiste(
                                f"Piloto con número de auto {nro_auto} no encontrado"))
                            self.inicio()

                    # REGISTRO DE PILOTOS QUE ABANDONAN LA CARRERA #
                        pilotos_abandonan = Datos.pilotos_abandonan()
                        pilotos_abandonan_con_equipo = []
                        for nro_auto in pilotos_abandonan:
                            piloto_equipo = next(
                                (piloto for piloto in total_pilotos_equipos if piloto.nro_auto == nro_auto), None)

                            if piloto_equipo:
                                pilotos_abandonan_con_equipo.append(
                                    (piloto_equipo[1], piloto_equipo[0]))
                                piloto_equipo[1].abandono = True
                            else:
                                print(ValorNoExiste(
                                    f"Piloto con número de auto {nro_auto} no encontrado"))
                                self.inicio()

                    # REGISTRO DE PILOTOS CON INFRACCIONES #
                    pilotos_infraccionan = Datos.pilotos_infraccionan()
                    pilotos_infraccionan_con_equipo = []
                    for nro_auto in pilotos_infraccionan:
                        piloto_equipo = next(
                            (piloto for piloto in total_pilotos_equipos if piloto.nro_auto == nro_auto), None)

                        if piloto_equipo:
                            pilotos_infraccionan_con_equipo.append(
                                (piloto_equipo[1], piloto_equipo[0]))
                            piloto_equipo[1].cantidad_penalidad_infringir_norma += 1
                        else:
                            print(ValorNoExiste(
                                f"Piloto con número de auto {nro_auto} no encontrado"))
                            self.inicio()

                    # REGISTRO PILOTOS CON ERRORES EN PITS #
                    pilotos_errores_pits = Datos.pilotos_errores_pits()
                    pilotos_errores_pits_con_equipo = []
                    for nro_auto in pilotos_errores_pits:
                        piloto_equipo = next(
                            (piloto for piloto in total_pilotos_equipos if piloto.nro_auto == nro_auto), None)

                        if piloto_equipo:
                            pilotos_errores_pits_con_equipo.append(
                                (piloto_equipo[1], piloto_equipo[0]))
                            piloto_equipo[1].cantidad_errores_en_pits += 1
                        else:
                            print(ValorNoExiste(
                                f"Piloto con número de auto {nro_auto} no encontrado"))
                            self.inicio()

                    # PILOTOS HABILITADOS PARA CORRER LA CARRERA #
                    pilotos_en_carrera_final = []
                    pilotos_por_equipo = defaultdict(int)
                    for piloto, nombre_equipo in total_pilotos_equipos:
                        if piloto.lesionado or piloto.abandono:
                            continue
                        if pilotos_por_equipo[nombre_equipo] < 2:
                            pilotos_en_carrera_final.append(
                                (piloto, nombre_equipo))
                            pilotos_por_equipo[nombre_equipo] += 1

                    # CALCULAR PUNTUACIÓN FINAL #
                    for piloto, nombre_equipo in pilotos_en_carrera_final:
                        mecanicos_por_equipo = []
                        autos_por_equipo = []

                        for equipo in self._equipos:
                            if equipo.nombre == nombre_equipo:
                                mecanicos_por_equipo = equipo.mecanicos
                                break

                        for auto in self._lista_de_autos:
                            if piloto.nro_auto == auto.nro_auto:
                                autos_por_equipo = auto.score
                                break

                        if piloto.abandono:   #agregue
                            score_final = 0
                        else:
                            score_mecanicos = sum(
                                mecanico.score for mecanico in mecanicos_por_equipo)
                            score_auto = autos_por_equipo
                            score_final = score_mecanicos + score_auto + piloto.score - 5 * \
                                piloto.cantidad_errores_en_pits - 8 * piloto.cantidad_penalidad_infringir_norma


                        # self._puntos_pilotos[piloto.cedula] += score_final
                        # self._resultados_carrera.append(
                        #     (nombre_equipo, piloto.nombre, score_final))

                    resultados_carrera_ordenados = sorted(
                        self._resultados_carrera, key=lambda x: x[1], reverse=True)
                    self._resultados_carrera.append(
                        resultados_carrera_ordenados)
                    
                    # for resultado in self._resultados_carrera:
                    #     piloto = next((p for p in self._empleados_registrados if p.nombre == resultado[1]), None)
                    #     if piloto:
                    #         piloto.ptos_campeonato += resultado[3]

                    puntaje_a_asignar = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

                    for i, (nombre_equipo, nombre_piloto, score_final) in enumerate(self._resultados_carrera):
                        if i < len(puntaje_a_asignar):
                            self._resultados_carrera[i] = (
                                nombre_equipo, nombre_piloto, score_final, puntaje_a_asignar[i])

                    for equipo in self._equipos:
                        for resultado in self._resultados_carrera:
                            if resultado.nombre_piloto == equipo[4].nombre:
                                equipo[4].ptos_campeonato = resultado.puntaje_a_asignar

                    # for equipo in self._equipos:
                    #      for resultado in self._resultados_carrera:
                    #          if resultado[1] == equipo.jefe_equipo.nombre:
                    #              equipo.jefe_equipo.ptos_campeonato = resultado[3]

                    # for piloto in self._empleados_registrados:
                    #     piloto.abandono=False
                    #     piloto.lesionado=False
                    #     piloto.cantidad_errores_en_pits=0
                    #     piloto.cantidad_penalidad_infringir_norma=0

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    self.inicio()
 # TERMINA SIMULAR CARRERA

 # COMIENZA REALIZAR CONSULTAS
            elif num_seleccionado == 5:
                print("Realizar consultas")

                try:
                    print("1. Top 10 pilotos con más puntos en el campeonato")
                    print("2. Resumen campeonato de constructores (equipos)")
                    print("3. Top 5 pilotos mejores pago")
                    print("4. Top 3 pilotos más habilidosos")
                    print("5. Retornar jefes de equipo")

                    num_seleccionado = input("Ingrese número: ")

                    if num_seleccionado.isdigit():
                        num_seleccionado = int(num_seleccionado)
                    else:
                        print(
                            "Uno o más datos ingresados son inválidos, intente nuevamente")

                    if num_seleccionado == 1:
                        print("Top 10 pilotos con más puntos en el campeonato:")

                        try:
                            total_pilotos = []
                            for equipo in self._equipos:
                                for empleado in equipo.piloto:
                                    if empleado.ptos_campeonato != 0:
                                        total_pilotos.append(equipo.nombre,
                                                             empleado.nombre, empleado.ptos_campeonato)

                            listado_consultas = Consultas()
                            top_diez_pilotos = listado_consultas.top_diez_pilotos(
                                total_pilotos)
                            if top_diez_pilotos is None:
                                print("No hay pilotos registrados en el sistema.")
                                self.inicio()
                            else:
                                for piloto in top_diez_pilotos:
                                    print(
                                        f"Piloto: {piloto[0]}, Score: {piloto[1]} ")

                        except ValorNoExiste:
                            print(
                                "No se pudo ejecutar su solicitud. Intente nuevamente.")

                    elif num_seleccionado == 2:
                        print("Resumen campeonato de constructores (equipos): ")

                        try:

                            total_pilotos = []
                            for equipo in self._equipos:
                                for empleado in equipo.piloto:
                                    if empleado.ptos_campeonato != 0:
                                        total_pilotos.append(equipo.nombre,
                                                             empleado.nombre, empleado.ptos_campeonato)

                            lista_consultas = Consultas()
                            resultados_resumen = lista_consultas.resumen_campeonato(
                                total_pilotos)
                            for resultado in resultados_resumen:
                                print(
                                    f"Equipo: {resultado[0]}, Puntaje: {resultado[1]}")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente.")
                            continue

                    elif num_seleccionado == 3:
                        print("Top 5 pilotos mejores pagados: ")

                        try:

                            total_pilotos = []
                            for equipo in self._equipos:
                                for empleado in equipo.piloto:
                                    total_pilotos.append(equipo.nombre,
                                                         empleado.nombre, empleado.salario)

                            lista_consultas = Consultas()
                            top_cinco_pilotos = lista_consultas.top_cinco_pilotos_mejores_pagos(
                                total_pilotos)
                            if top_cinco_pilotos is None:
                                print("No hay pilotos registrados en el sistema.")
                                self.inicio()
                            else:
                                for piloto in top_cinco_pilotos:
                                    print(
                                        f"Piloto: {piloto[0]}, Salario: {piloto[1]} ")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 4:
                        print("Top 3 pilotos más habilidosos")

                        try:
                            total_pilotos = []
                            for equipo in self._equipos:
                                for empleado in equipo.piloto:
                                    if empleado.ptos_campeonato != 0:
                                        total_pilotos.append(equipo.nombre,
                                                             empleado.nombre, empleado.score)

                            listado_consultas = Consultas()
                            top_tres_pilotos = listado_consultas.top_diez_pilotos(
                                total_pilotos)
                            if top_tres_pilotos is None:
                                print("No hay pilotos registrados en el sistema.")
                                self.inicio()
                            else:
                                for piloto in top_tres_pilotos:
                                    print(
                                        f"Piloto: {piloto[0]}, Score: {piloto[1]} ")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 5:
                        print("Retornar jefes de equipo")

                        try:

                            total_jefes_equipo = []
                            for equipo in self._equipos:
                                for empleado in equipo.jefe_equipo:
                                    if empleado.ptos_campeonato != 0:
                                        total_jefes_equipo.append(
                                            empleado.nombre, equipo.nombre)

                            lista_consultas = Consultas()
                            jefes_equipo = lista_consultas.retornar_jefes_equipo(
                                total_jefes_equipo)
                            for jefe in jefes_equipo:
                                print(
                                    f"Jefe: {jefe[0]}, Equipo: {jefe[1]} ")
                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                except ValueError:
                    print(
                        "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente."
                    )
                    self.inicio()
#  # TERMINA REALIZAR CONSULTAS

#  # COMIENZA FINALIZAR PROGRAMA
            elif num_seleccionado == 6:
                print("El programa ha finalizado correctamente")

                self._empleados_registrados.clear()
                self._lista_de_autos.clear()
                self._equipos.clear()
                self.cant_empleados_equipo.clear()
                self._cedulas_empleados.clear()
                self._resultados_carrera.clear()
                # self._asignaciones_auto_piloto.clear()
                break
 # TERMINA FINALIZAR PROGRAMA
            else:
                print(
                    "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                )
                self.inicio()


if __name__ == "__main__":
    menu = Menu()
    menu.inicio()
