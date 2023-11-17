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
        self._jefes_y_equipos = []  # checked

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

                    lista_empleados = []
                    for _ in range(12):
                        empleado_equipo = Datos.empleados_por_equipo()
                        lista_empleados.append(empleado_equipo)

                    print("Longitud de lista_empleados antes de la verificación:", len(
                        lista_empleados))

                    count_pilotos_titulares = 0
                    count_pilotos_reserva = 0
                    count_mecanicos = 0
                    count_jefes = 0
                    print(lista_empleados)

                    if len(lista_empleados) < 12:
                        print(
                            "No se pudo crear el equipo, el equipo no tiene 12 empleados.")
                        self.inicio()

                    for cedula in lista_empleados:
                        print(f"Cédula a verificar: {cedula}")
                        if cedula not in self._cedulas_empleados:
                            print(
                                f"La cédula {cedula} no se encuentra registrada en el sistema.")
                            print("No se pudo crear el equipo.")
                            self.inicio()
                        else:
                            empleado_en_equipo = next(
                                (empleado for equipo_existente in self._equipos
                                 for empleado in equipo_existente.pilotos + [equipo_existente.jefe_equipo] + equipo_existente.mecanicos
                                 if empleado and getattr(empleado, 'cedula', None) == cedula), None)

                            if empleado_en_equipo:
                                print(
                                    f"El empleado con cédula {cedula} ya pertenece a otro equipo.")
                                print("No se pudo crear el equipo.")
                                self.inicio()
                            elif empleado_en_equipo is None:
                                empleado_registrado = next(
                                    (empleado for empleado in self._empleados_registrados if empleado.cedula == cedula), None)

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
                                        self._jefes_y_equipos.append(
                                            (empleado_registrado.nombre, equipo.nombre))
                                    else:
                                        print("Cupo de jefes completo.")
                                        self.inicio()

                    if count_pilotos_titulares + count_pilotos_reserva + count_mecanicos + count_jefes == 12:
                        self._equipos.append(equipo)
                        print("Equipo registrado correctamente")
                    else:
                        print(
                            "No se pudo crear el equipo, el equipo no tiene 12 empleados.")
                        self.inicio()

                except ValorNoExiste:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente")
                    self.inicio()
 # TERMINA ALTA DE EQUIPO

 # COMIENZA SIMULAR CARRERA
            elif num_seleccionado == 4:
                print("Simular carrera")

                try:
                    # # TOTAL DE PILOTOS DE TODOS LOS EQUIPOS #
                    total_pilotos_equipos = []
                    for equipo in self._equipos:
                        nombre_equipo = equipo.nombre
                        pilotos = equipo.pilotos

                        pilotos_equipo = [(nombre_equipo, piloto.nro_auto)
                                          for piloto in pilotos]

                        total_pilotos_equipos.extend(pilotos_equipo)

                    print("Total de pilotos de todos los equipos:",
                          len(total_pilotos_equipos))

                    # REGISTRO DE PILOTOS LESIONADOS #
                    pilotos_lesionados = Datos.pilotos_lesionados()
                    if pilotos_lesionados:
                        for empleado in self._empleados_registrados:
                            if isinstance(empleado, Piloto) and empleado.nro_auto in pilotos_lesionados:
                                empleado.lesion = True
                    else:
                        print(ValorNoExiste(
                            "No se registraron pilotos lesionados."))

                    for equipo in self._equipos:
                        pilotos_titulares = [
                            piloto for piloto in equipo.pilotos if piloto.cargo == 1]

                        if len(pilotos_titulares) != 2:
                            print(
                                f"El equipo {equipo.nombre} no tiene los dos pilotos titulares.")

                        for piloto_titular in pilotos_titulares:
                            if piloto_titular.lesion:

                                piloto_reserva = next(
                                    (piloto for piloto in equipo.pilotos if piloto.cargo == 2), None)
                                if piloto_reserva:
                                    equipo.pilotos.remove(piloto_titular)
                                    equipo.pilotos.append(piloto_reserva)
                                    print(
                                        f"El piloto titular {piloto_titular.nombre} del equipo {equipo.nombre} está lesionado. Correrá el piloto de reserva {piloto_reserva.nombre}.")
                                else:

                                    print(
                                        f"El piloto titular {piloto_titular.nombre} del equipo {equipo.nombre} está lesionado y no hay piloto de reserva. El equipo no puede participar.")

                    # REGISTRO DE PILOTOS QUE ABANDONAN LA CARRERA #
                    numeros_auto_abandonados = Datos.pilotos_abandonan()
                    if numeros_auto_abandonados:
                        for empleado in self._empleados_registrados:
                            if isinstance(empleado, Piloto) and empleado.nro_auto in numeros_auto_abandonados:
                                empleado.abandono = True

                    else:
                        print(ValorNoExiste(
                            "No se registraron pilotos que abandonaron la carrera."))

                    # REGISTRO DE PILOTOS CON INFRACCIONES #
                    pilotos_infraccionan = Datos.pilotos_infraccionan()
                    if pilotos_infraccionan:
                        for empleado in self._empleados_registrados:
                            if isinstance(empleado, Piloto) and empleado.nro_auto in pilotos_infraccionan:
                                empleado.cant_infracciones += 1
                    else:
                        print(ValorNoExiste(
                            "No se registraron pilotos que infringieron normas."))

                    # REGISTRO PILOTOS CON ERRORES EN PITS #
                    pilotos_errores_pits = Datos.pilotos_errores_pits()
                    if pilotos_errores_pits:
                        for empleado in self._empleados_registrados:
                            if isinstance(empleado, Piloto) and empleado.nro_auto in pilotos_errores_pits:
                                empleado.errores_pits += 1
                    else:
                        print(ValorNoExiste(
                            "No se registraron pilotos con errores en pits."))

                    # PILOTOS HABILITADOS PARA CORRER LA CARRERA #
                    pilotos_en_carrera_final = []
                    for piloto in self._empleados_registrados:
                        if isinstance(piloto, Piloto) and not piloto.lesion and not piloto.abandono:
                            pilotos_en_carrera_final.append(piloto.cedula)

                    print("Cant. pilotos habilitados para correr la carrera: ", len(
                        pilotos_en_carrera_final))

                    # CALCULAR PUNTUACIÓN FINAL #

                    for piloto_actual in pilotos_en_carrera_final:
                        nombre_equipo = next(
                            (equipo.nombre for equipo in self._equipos if piloto_actual in [p.cedula for p in equipo.pilotos]), None)

                        print("Nombre equipo:", nombre_equipo)

                        for equipo in self._equipos:
                            if nombre_equipo == equipo.nombre:
                                score_mecanicos_equipo = 0
                                for equipo in self._equipos:
                                    if nombre_equipo == equipo.nombre:
                                        # Obtener la suma de los scores de los mecánicos asociados al equipo
                                        score_mecanicos_equipo = sum(
                                            mecanico.score for mecanico in equipo.mecanicos)
                                        print("Score mecánicos equipo:",
                                              score_mecanicos_equipo)

                                score_auto = next(
                                    (auto.score for auto in self._lista_de_autos if equipo.modelo_auto == auto.modelo), None)
                                print("Score auto:", score_auto)

                                score_piloto = next(
                                    (p.score for p in self._empleados_registrados if p.cedula == piloto_actual), None)
                                print("Score pilotos:", score_piloto)

                        cant_errores_pits = next(
                            (piloto.errores_pits for piloto in self._empleados_registrados if piloto.cedula == piloto), None)
                        print("Cant. errores pits:", cant_errores_pits)

                        cant_infracciones = next(
                            (piloto.cant_infracciones for piloto in self._empleados_registrados if piloto.cedula == piloto), None)
                        print("Cant. infracciones:", cant_infracciones)

                        score_total = score_mecanicos_equipo + score_auto + score_piloto - \
                            5 * (cant_errores_pits or 0) - \
                            8 * (cant_infracciones or 0)

                        print("Score total:", score_total)

                        self._resultados_carrera.append(
                            (nombre_equipo, piloto_actual, score_total))
                        print("Resultados carrera:", self._resultados_carrera)

                    resultados_carrera_ordenados = sorted(
                        self._resultados_carrera, key=lambda x: x[2], reverse=True)
                    print("Resultados carrera ordenados:",
                          resultados_carrera_ordenados)

                    puntaje_a_asignar = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

                    for i, (nombre_equipo, cedula_piloto, score_final) in enumerate(resultados_carrera_ordenados):
                        if i < len(puntaje_a_asignar):
                            resultados_carrera_ordenados[i] = (
                                nombre_equipo, cedula_piloto, score_final, puntaje_a_asignar[i])

                    self._resultados_carrera = resultados_carrera_ordenados
                    print("Resultados carrera ordenados con puntaje:",
                          self._resultados_carrera)

                    for i, (nombre_equipo, nombre_piloto, score_final, puntaje) in enumerate(self._resultados_carrera):
                        for empleado in self._empleados_registrados:
                            if isinstance(empleado, Piloto) and empleado.cedula == nombre_piloto:
                                empleado.ptos_campeonato += puntaje
                                print("Piloto:", empleado.cedula,
                                      "Puntos campeonato:", empleado.ptos_campeonato)

                    for piloto in self._empleados_registrados:
                        piloto.abandono = False
                        piloto.lesion = False
                        piloto.errores_pits = 0
                        piloto.cant_infracciones = 0

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
                            for empleado in self._empleados_registrados:
                                if isinstance(empleado, Piloto) and empleado.ptos_campeonato != 0:
                                    total_pilotos.append(
                                        (empleado.cedula, empleado.ptos_campeonato))

                            total_pilotos_ordenados = sorted(
                                total_pilotos, key=lambda x: x[1], reverse=True)

                            print("Top 10 pilotos en el campeonato:")
                            for nombre, puntos in total_pilotos_ordenados[:10]:
                                print(f"{nombre}: {puntos} puntos")

                        except ValorNoExiste:
                            print(
                                "No se pudo ejecutar su solicitud. Intente nuevamente.")

                    elif num_seleccionado == 2:
                        print("Resumen campeonato de constructores(equipos): ")

                        try:

                            total_pilotos = []
                            for equipo in self._equipos:
                                for empleado in equipo.pilotos:
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
                            for empleado in self._empleados_registrados:
                                if isinstance(empleado, Piloto):
                                    total_pilotos.append(
                                        (empleado.cedula, empleado.salario))

                            total_pilotos_ordenados = sorted(
                                total_pilotos, key=lambda x: x[1], reverse=True)

                            print("Top 5 pilotos mejores pagados:")
                            for nombre, salario in total_pilotos_ordenados[:5]:
                                print(f"{nombre}: USD {salario} ")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 4:
                        print("Top 3 pilotos más habilidosos")

                        try:
                            total_pilotos = []
                            for empleado in self._empleados_registrados:
                                if isinstance(empleado, Piloto):
                                    total_pilotos.append(
                                        (empleado.cedula, empleado.score))

                            total_pilotos_ordenados = sorted(
                                total_pilotos, key=lambda x: x[1], reverse=True)

                            print("Top 5 pilotos mejores pagados:")
                            for nombre, score in total_pilotos_ordenados[:3]:
                                print(f"{nombre}:  {score} ptos. ")

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 5:
                        print("Retornar jefes de equipo")

                        try:

                            print("Jefes de equipo:")
                            for jefe in self._jefes_y_equipos:
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
