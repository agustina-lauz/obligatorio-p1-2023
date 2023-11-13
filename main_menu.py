from collections import defaultdict
from datos import Datos
from entities.auto import Auto
from entities.empleados import Empleado
# from entities.equipos import Equipo
from entities.pilotos import Piloto
from exceptions.valor_ya_existe import ValorYaExiste
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste
from entities.consultas import Consultas 



limites_cargo = {
    0: 1,  # jefes por equipo
    1: 3,  # pilotos por equipo
    2: 8  # mecanicos por equipo
}


class Menu:

    def __init__(self) -> None:
        self._jefe_equipo = None
        self._lista_de_mecanicos = []
        self._lista_de_pilotos_titulares = []
        self._piloto_reserva = None
        self._equipo_completo = []
        self._lista_de_autos = []
        self._equipos = []
        self.cant_empleados_equipo = defaultdict(
            lambda: defaultdict(list))
        self.cedulas_empleados = set()
        self._asignaciones_auto_piloto = {}

    def inicio(self) -> None:

        while True:
            print("Menu principal")
            print("Seleccione la opcion del menú:")
            print("1. Alta de empleado")
            print("2. Alta de auto")
            print("3. Alta de equipo")
            print("4. Simular carrera")
            print("5. Realizar consultas")
            print("6. Finalizar programa")

            num_seleccionado = input("Ingrese Número:")

            if num_seleccionado.isdigit():
                num_seleccionado = int(num_seleccionado)
            else:
                print("El dato ingresado no es un numero, intente nuevamente")
                continue

 # COMIENZA ALTA DE EMPLEADO
            if num_seleccionado == 1:
                print("Alta de empleado")

                try:
                    nombre = Datos.set_nombre()
                    if nombre is None:
                        self.inicio()

                    try:
                        cedula = Datos.set_cedula()
                        if cedula is None:
                            self.inicio()
                        if cedula in self.cedulas_empleados:
                            print(ValorYaExiste(
                                "La cédula ingresada ya existe, intente nuevamente"))
                            raise ValorYaExiste(
                                "La cédula ingresada ya existe, intente nuevamente")

                    except ValorYaExiste:
                        self.inicio()

                    fecha_nacimiento = Datos.set_fecha_nacimiento()
                    if fecha_nacimiento is None:
                        self.inicio()
                    nacionalidad = Datos.set_nacionalidad()
                    if nacionalidad is None:
                        self.inicio()
                    equipo = Datos.set_equipo()
                    if equipo is None:
                        self.inicio()
                    salario = Datos.set_salario()
                    if salario is None:
                        self.inicio()
                    cargo = Datos.set_cargo()
                    if cargo is None:
                        self.inicio()

                    try:
                        if len(self.cant_empleados_equipo[equipo][cargo]) >= limites_cargo[cargo]:
                            raise ValorYaExiste(
                                "El cupo de empleados para ese cargo y equipo se encuentra completo")

                    except ValorYaExiste:
                        print(ValorYaExiste(
                            "El cupo de empleados para ese cargo se encuentra completo"))
                        self.inicio()

                    if cargo == 0:
                        agregar_jefe = None
                        if agregar_jefe is not None:
                            print("Este equipo tiene el cupo de jefes completo")
                        else:
                            jefe_equipo = Empleado(
                                cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
                            self.cant_empleados_equipo[equipo][cargo].append(
                                jefe_equipo)
                            self.cedulas_empleados.add(cedula)
                            self._equipo_completo.append(jefe_equipo)

                    elif cargo == 1:
                        score = Datos.set_score()
                        if score is None:
                            self.inicio()
                        nro_auto = Datos.set_nro_auto()
                        if nro_auto is None:
                            self.inicio()
                        titular = Datos.set_titular()
                        if titular is None:
                            self.inicio()
                        piloto = Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario,
                                        cargo, equipo, score, nro_auto, titular)
                        try:
                            if len(self._lista_de_pilotos_titulares) >= 2 and titular:
                                print(ValorYaExiste(
                                    "El cupo de pilotos titulares se encuentra completo"))
                                self.inicio()
                            elif len(self._lista_de_pilotos_titulares) <= 2 and titular:
                                self._lista_de_pilotos_titulares.append(piloto)
                                self.cant_empleados_equipo[equipo][cargo].append(
                                    piloto)
                                self.cedulas_empleados.add(cedula)
                                self._equipo_completo.append(piloto)

                            else:
                                if self._piloto_reserva is not None:
                                    print(ValorYaExiste(
                                        "El cupo de pilotos reserva se encuentra completo"))
                                    self.inicio()
                                else:
                                    self._piloto_reserva = piloto
                                    self.cant_empleados_equipo[equipo][cargo].append(
                                        piloto)
                                    self.cedulas_empleados.add(cedula)
                                    self._equipo_completo.append(piloto)

                        except ValorYaExiste:
                            print(ValorYaExiste(
                                "El cupo de pilotos en el equipo se encuentra completo"))
                            self.inicio()

                    elif cargo == 2:
                        score = Datos.set_score()
                        if score is None:
                            self.inicio()
                        mecanico = Empleado(
                            cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
                        mecanico.score = score

                        self.cant_empleados_equipo[equipo][cargo].append(
                            mecanico)
                        self.cedulas_empleados.add(cedula)
                        self._equipo_completo.append(mecanico)
                        self._lista_de_mecanicos.append(mecanico)

                except ValueError:
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
                    numero = Datos.set_nro_auto()
                    if numero is None:
                        self.inicio()
                    anio = Datos.set_anio()
                    if anio is None:
                        self.inicio()
                    score = Datos.set_score()
                    if score is None:
                        self.inicio()

                    auto = Auto(numero, modelo, anio, score)
                    self._lista_de_autos.append(auto)

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    self.inicio()

 # TERMINA ALTA DE AUTO

 # COMIENZA ALTA DE EQUIPO
            elif num_seleccionado == 3:
                print("Alta de equipo")

                try:
                    nombre_equipo = input("Ingrese el nombre del equipo: ")
                    modelo_auto = input("Ingrese el modelo del auto: ")

                    auto_registrado = any(
                        auto.modelo == modelo_auto for auto in self._lista_de_autos)
                    if not auto_registrado:
                        print("El auto no está registrado.")
                        self.inicio()

                    empleados = []
                    for _ in range(12):
                        cedula_colaborador = int(
                            input("Ingrese la cédula del empleado: "))

                        empleado_encontrado = next(
                            (empleado for empleado in self._equipo_completo if empleado.cedula == cedula_colaborador), None)

                        if empleado_encontrado is None:
                            print("La cédula no está registrada en el sistema.")
                            self.inicio()
                        elif empleado_encontrado.equipo != nombre_equipo:
                            print(
                                "El empleado no pertenece al equipo que estás intentando crear.")
                            self.inicio()
                        else:
                            empleados.append(empleado_encontrado)

                        nuevo_equipo = {
                            'nombre': nombre_equipo, 'modelo_auto': modelo_auto, 'empleados': empleados}
                        self._equipos.append(nuevo_equipo)

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente")
                    self.inicio()

 # TERMINA ALTA DE EQUIPO

 # COMIENZA SIMULAR CARRERA
            elif num_seleccionado == 4:
                print("Simular carrera")

                if len(self._equipo_completo) < 12:
                    print(NoRespetaMetodoDefinido(
                        "No se puede simular una carrera sin un equipo completo."))
                    self.inicio()
                else:
                    continue
                
                try:
                    pilotos_ordenados = sorted(
                        self._lista_de_pilotos_titulares, key=lambda piloto: piloto.score, reverse=True)
                    if self._piloto_reserva is not None:
                        pilotos_ordenados.extend(self._piloto_reserva)
                        pilotos_ordenados = sorted(
                            pilotos_ordenados, key=lambda piloto: piloto.score, reverse=True)

                    pilotos_lesionados = Datos.pilotos_lesionados()
                    for pilotos in pilotos_ordenados:
                        if pilotos.cedula == pilotos_lesionados.cedula:
                            pilotos.lesion = True
                        else:
                            print(ValorNoExiste("Piloto no encontrado"))
                            self.inicio()


                    pilotos_abandonan = Datos.pilotos_abandonan()
                    for pilotos in pilotos_ordenados:
                        if pilotos.cedula == pilotos_abandonan.cedula:
                            pilotos.abandono = True
                            pilotos.score_final = 0
                        else:
                            print(ValorNoExiste("Piloto no encontrado"))
                            self.inicio()



                    pilotos_infraccionan = Datos.pilotos_infraccionan()
                    for piloto in pilotos_ordenados:
                        if piloto.cedula == pilotos_infraccionan[0]:
                            piloto.cant_infracciones = pilotos_infraccionan[1]
                        else:
                            self.inicio()

                    pilotos_errores_pits = Datos.pilotos_errores_pits()
                    for piloto in pilotos_ordenados:
                        if piloto.cedula == pilotos_errores_pits[0]:
                            piloto.errores_pits = pilotos_errores_pits[1]
                        else:
                            self.inicio()

                    pilotos_en_carrera = []
                    for piloto in pilotos_ordenados:
                        if not piloto.lesion and not piloto.abandono:
                            pilotos_en_carrera.append(piloto)
                        else:
                            self.inicio() 

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

                        continue

                    if num_seleccionado == 1:
                        print("Top 10 pilotos con más puntos en el campeonato")

                        top_diez_pilotos = Consultas.top_diez_pilotos(pilotos_en_carrera)
                        if top_diez_pilotos is None:
                            print("No hay pilotos registrados en el sistema.")
                            self.inicio()

                    elif num_seleccionado == 2:
                        print("Resumen campeonato de constructores (equipos)")

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 3:
                        print("Top 5 pilotos mejores pagados")

                        top_cinco_pilotos_mejores_pagos = Consultas.top_cinco_pilotos_mejores_pagos( self._equipo_completo)
                        if top_cinco_pilotos_mejores_pagos is None: 
                            print("No hay pilotos registrados en el sistema.")
                            self.inicio()

                    elif num_seleccionado == 4:
                        print("Top 3 pilotos más habilidosos")

                        top_tres_pilotos_mas_habilidosos = Consultas.top_tres_pilotos_mas_habilidosos(pilotos_en_carrera)
                        if top_tres_pilotos_mas_habilidosos is None:
                            print("No hay pilotos registrados en el sistema.")
                            self.inicio()

                    elif num_seleccionado == 5:
                        print("Retornar jefes de equipo")

                        retornar_jefes_equipo = Consultas.retornar_jefes_equipo(self._equipo_completo)
                        if retornar_jefes_equipo is None:
                            print("No hay jefes de equipo registrados en el sistema.")
                            self.inicio()          

                except ValueError:
                    print(
                        "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                    )
                    self.inicio() 
 # TERMINA REALIZAR CONSULTAS

 # COMIENZA FINALIZAR PROGRAMA
            elif num_seleccionado == 6:
                print("El programa ha finalizado correctamente")

                self._jefe_equipo = None
                self._lista_de_mecanicos.clear()
                self._lista_de_pilotos_titulares.clear()
                self._piloto_reserva = None
                self._equipo_completo.clear()
                self._lista_de_autos.clear()
                self._equipos.clear()
                self.cant_empleados_equipo.clear()
                self.cedulas_empleados.clear()
                self._asignaciones_auto_piloto.clear()
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
