from collections import defaultdict
from datos import Datos
from entities.auto import Auto
from entities.consultas import Consultas
from entities.empleados import Empleado
from entities.equipos import Equipo
from entities.pilotos import Piloto
from exceptions.valor_ya_existe import ValorYaExiste
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste


limites_cargo = {

    1: 2,  # pilotos titulares por equipo
    2: 1,  # pilotos reserva por equipo
    3: 8,  # mecanicos por equipo
    4: 1,  # jefes por equipo
}


class Menu:

    def __init__(self) -> None:
        self._jefe_equipo = []  # checked
        self._lista_de_mecanicos = []  # checked
        self._lista_de_pilotos_titulares = []  # checked
        self._piloto_reserva = []  # checked
        self._lista_de_autos = []  # checked
        self._equipos = []  # checked
        self.cant_empleados_equipo = defaultdict(
            lambda: defaultdict(list))
        self._cedulas_empleados = set()  # checked
        self._pilotos_en_carrera = []
        # self._asignaciones_auto_piloto = {}

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
                            print(ValorYaExiste(
                                "La cédula ingresada ya existe, intente nuevamente"))
                            raise ValorYaExiste(
                                "La cédula ingresada ya existe, intente nuevamente")
                    except ValorYaExiste:
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
                            self._lista_de_pilotos_titulares.append(piloto)
                            self._cedulas_empleados.add(cedula)
                            print("Piloto titular registrado correctamente")
                        else:
                            piloto.titular = False
                            self._piloto_reserva.append(piloto)
                            self._cedulas_empleados.add(cedula)
                            print("Piloto de reserva registrado correctamente")

                    elif cargo == 3:
                        score = Datos.set_score()
                        mecanico = Empleado(
                            cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
                        mecanico.score = score
                        self._lista_de_mecanicos.append(mecanico)
                        self._cedulas_empleados.add(cedula)
                        print("Mecanico registrado correctamente")

                    elif cargo == 4:
                        jefe_equipo = Empleado(
                            cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
                        self._jefe_equipo.append(jefe_equipo)
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

                #aca en alta de equipo esta habiendo un problema al validar las cedulas
                #de los empleados, ya que ingresas cedulas que no estan registradas y las toma bien

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
                    empleados = Datos.empleados_por_equipo()
                    #creo que el problema esta por aca ya que
                    #no se esta tomando la lista de _cedulas_empleados al momento
                    #de validar y ver que empleados se pueden agrear o no

                    count_pilotos_titulares = 0
                    count_pilotos_reserva = 0
                    count_mecanicos = 0
                    count_jefes = 0

                    for cedula_colaborador in empleados:
                        if cedula_colaborador in self._cedulas_empleados:
                            print(
                                f"La cédula {cedula_colaborador} ya está registrada.")
                            print("No se pudo crear el equipo.")
                            self.inicio()

                        empleado_encontrado = None
                        for equipo_existente in self._equipos:
                            empleado_encontrado = next(
                                (empleado for empleado in equipo_existente.pilotos + [equipo_existente.jefe_equipo] + equipo_existente.mecanicos if empleado.cedula == cedula_colaborador), None)
                            if empleado_encontrado:
                                break

                        if empleado_encontrado is None:
                            print(
                                f"La cédula {cedula_colaborador} no está registrada en el sistema.")
                            print("No se pudo crear el equipo.")
                            self.inicio()
                        elif empleado_encontrado.equipo is not None:
                            print(
                                f"El empleado con cédula {cedula_colaborador} ya pertenece a otro equipo.")
                            print("No se pudo crear el equipo.")
                            self.inicio()

                        if empleado_encontrado.cargo == 1:
                            if count_pilotos_titulares < limites_cargo[1]:
                                equipo.pilotos.append(empleado_encontrado)
                                count_pilotos_titulares += 1
                            else:
                                print("Cupo de pilotos completo.")
                                self.inicio()
                        elif empleado_encontrado.cargo == 2:
                            if count_pilotos_reserva < limites_cargo[2]:
                                equipo.pilotos.append(empleado_encontrado)
                                count_pilotos_reserva += 1
                            else:
                                print("Cupo de pilotos reserva completo.")
                                self.inicio()
                        elif empleado_encontrado.cargo == 3:
                            if count_mecanicos < limites_cargo[3]:
                                equipo.mecanicos.append(empleado_encontrado)
                                count_mecanicos += 1
                            else:
                                print("Cupo de mecanicos completo.")
                                self.inicio()
                        elif empleado_encontrado.cargo == 4:
                            if count_jefes < limites_cargo[4]:
                                equipo.jefe_equipo = empleado_encontrado
                                count_jefes += 1
                            else:
                                print("Cupo de jefes completo.")
                                self.inicio()

                    self._equipos.append(equipo)
                    print("Equipo registrado correctamente")

                except ValorNoExiste:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente")
                    self.inicio()

 # TERMINA ALTA DE EQUIPO

 # COMIENZA SIMULAR CARRERA
            elif num_seleccionado == 4:
                print("Simular carrera")

                #TENEMOS QUE TENER EN CUENTA QUE SI EL USUARIO PONE ENTER O ESPACIO A ALGUA DE ESTAS LSITAS
                # ES PORQUE EN ESA LESION/ABANDON/INFRACCION... NO HAY PILOTOS
                #POR LO TANTO SE DEVUELVE LA LISTA VACIA

                # for equipo in self._equipos:
                #     if len(equipo.pilotos) < 3 or len(equipo.mecanicos) < 8 or equipo['jefe_equipo'] is None:
                #         print(NoRespetaMetodoDefinido(
                #             f"El equipo {equipo['nombre']} no tiene un equipo completo de 12 empleados o no tiene jefe de equipo."))
                #         self.inicio()

                # try:
                #     pilotos_ordenados = sorted(
                #         self._lista_de_pilotos_titulares, key=lambda piloto: piloto.score, reverse=True)
                #     if self._piloto_reserva is not None:
                #         pilotos_ordenados.extend(self._piloto_reserva)
                #         pilotos_ordenados = sorted(
                #             pilotos_ordenados, key=lambda piloto: piloto.score, reverse=True)

                #     pilotos_lesionados = Datos.pilotos_lesionados()
                #     for pilotos in pilotos_ordenados:
                #         if pilotos.cedula == pilotos_lesionados[0]:
                #             pilotos.lesion = True
                #         else:
                #             print(ValorNoExiste("Piloto no encontrado"))
                #             self.inicio()

                #     pilotos_abandonan = Datos.pilotos_abandonan()
                #     for pilotos in pilotos_ordenados:
                #         if pilotos.cedula == pilotos_abandonan[0]:
                #             pilotos.abandono = True
                #             pilotos.score_final = 0
                #         else:
                #             print(ValorNoExiste("Piloto no encontrado"))
                #             self.inicio()

                #     pilotos_infraccionan = Datos.pilotos_infraccionan()
                #     for piloto in pilotos_ordenados:
                #         if piloto.cedula == pilotos_infraccionan[0]:
                #             piloto.cant_infracciones = pilotos_infraccionan[1]
                #         else:
                #             self.inicio()

                #     pilotos_errores_pits = Datos.pilotos_errores_pits()
                #     for piloto in pilotos_ordenados:
                #         if piloto.cedula == pilotos_errores_pits[0]:
                #             piloto.errores_pits = pilotos_errores_pits[1]
                #         else:
                #             self.inicio()

                #     pilotos_en_carrera = []
                #     for piloto in pilotos_ordenados:
                #         if not piloto.lesion and not piloto.abandono:
                #             pilotos_en_carrera.append(piloto)
                #         else:
                #             self.inicio()

                # except ValueError:
                #     print(
                #         "Uno o más datos ingresados son inválidos, intente nuevamente"
                #     )
                #     self.inicio()
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

                        continue

                    if num_seleccionado == 1:
                        print("Top 10 pilotos con más puntos en el campeonato:")

                        listado_consultas = Consultas()
                        top_diez_pilotos = listado_consultas.top_diez_pilotos(
                            self._pilotos_en_carrera)
                        if top_diez_pilotos is None:
                            print("No hay pilotos registrados en el sistema.")
                            self.inicio()

                    elif num_seleccionado == 2:
                        print("Resumen campeonato de constructores (equipos): ")

                        try:
                            lista_consultas = Consultas()
                            resultados_resumen = lista_consultas.resumen_campeonato()
                            for resultado in resultados_resumen:
                                print(
                                    f"Equipo: {resultado[0]}, Puntaje: {resultado[1]}")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 3:
                        print("Top 5 pilotos mejores pagados: ")

                        try:
                            total_pilotos = []
                            total_pilotos.extend(
                                self._lista_de_pilotos_titulares)
                            total_pilotos.extend(self._piloto_reserva)

                            lista_consultas = Consultas()
                            top_cinco_pilotos = lista_consultas.top_cinco_pilotos_mejores_pagos()
                            for i, piloto in enumerate(top_cinco_pilotos, start=1):
                                print(
                                    f"{i}. {piloto.nombre} - Salario: {piloto.salario}")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 4:
                        print("Top 3 pilotos más habilidosos")

                        try:
                            total_pilotos = []
                            total_pilotos.extend(
                                self._lista_de_pilotos_titulares)
                            total_pilotos.extend(self._piloto_reserva)

                            lista_consultas = Consultas()
                            pilotos = lista_consultas.top_tres_pilotos_mas_habilidosos()
                            for i, piloto in enumerate(pilotos, start=1):
                                print(
                                    f"{i}. {piloto.nombre} - Score: {piloto.score}")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 5:
                        print("Retornar jefes de equipo")

                        try:

                            lista_consultas = Consultas()
                            jefes_equipo = lista_consultas.retornar_jefes_equipo()
                            for jefe in jefes_equipo:
                                print(
                                    f"Equipo: {jefe.equipo.nombre}, Jefe: {jefe.nombre}")
                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                except ValueError:
                    print(
                        "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                    )
                    self.inicio()
#  # TERMINA REALIZAR CONSULTAS

#  # COMIENZA FINALIZAR PROGRAMA
            elif num_seleccionado == 6:
                print("El programa ha finalizado correctamente")

                self._jefe_equipo = None
                self._lista_de_mecanicos.clear()
                self._lista_de_pilotos_titulares.clear()
                self._piloto_reserva = None
                self._lista_de_autos.clear()
                self._equipos.clear()
                self.cant_empleados_equipo.clear()
                self._cedulas_empleados.clear()
                # self._asignaciones_auto_piloto.clear()
                break

            else:
                print(
                    "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                )
                self.inicio()
 # TERMINA FINALIZAR PROGRAMA


if __name__ == "__main__":
    menu = Menu()
    menu.inicio()
