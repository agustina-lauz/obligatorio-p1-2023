from entities.pilotos import Piloto
from datos import Datos
from entities.auto import Auto
# from entities.equipos import Equipo
# from entities.consultas import Consultas
from entities.empleados import Empleado


class Menu:
    def inicio(self) -> None:
        jefe_equipo = None
        lista_de_mecanicos = []
        lista_de_pilotos_titulares = []
        piloto_reserva = None
        equipo_completo = []
        lista_de_autos = []
        # lista_de_equipos = []

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

            if num_seleccionado == 1:
                print("Alta de empleado")

                cedulas_existentes = [
                    empleado.cedula for empleado in equipo_completo]

                for _ in range(12):

                    try:
                        nombre = Datos.set_nombre()

                        while True:
                            cedula = Datos.set_cedula()
                            if cedula is None:  # Check if an error occurred
                                self.inicio() 
                            if cedula in cedulas_existentes:  # Verificar si la cédula ya existe
                                print(
                                    "La cédula ingresada ya existe, intente nuevamente")
                                continue
                            else:
                                cedulas_existentes.append(cedula)
                                break

                        fecha_nacimiento = Datos.set_fecha_nacimiento()
                        nacionalidad = Datos.set_nacionalidad()
                        equipo = Datos.set_equipo()
                        salario = Datos.set_salario()
                        cargo = Datos.set_cargo()

                        if cargo == 0:
                            agregar_jefe = None
                            if agregar_jefe is not None:
                                print("Este equipo tiene el cupo de jefes completo")
                            else:
                                jefe_equipo = Empleado(
                                    nombre, cedula, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
                                agregar_jefe = jefe_equipo
                                equipo_completo.append(jefe_equipo)

                        elif cargo == 1:
                            score = Datos.set_score()
                            nro_auto = Datos.set_nro_auto()
                            titular = Datos.set_titular()
                            imprevistos = Datos.set_imprevistos()
                            lesion = Datos.set_lesion()
                            piloto = Piloto(nombre, cedula, fecha_nacimiento, nacionalidad, salario,
                                            cargo, equipo, score, nro_auto, titular, imprevistos, lesion)

                            if titular and len(lista_de_pilotos_titulares) <= 2:
                                lista_de_pilotos_titulares.append(piloto)
                                equipo_completo.append(piloto)
                            elif not titular and piloto_reserva is None:
                                piloto_reserva = piloto
                                equipo_completo.append(piloto_reserva)
                            else:
                                print(
                                    "Este equipo tiene el cupo de pilotos completo")

                        elif cargo == 2:
                            score = Datos.set_score()
                            mecanico = Empleado(
                                nombre, cedula, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
                            mecanico._score = score

                            if len(lista_de_mecanicos) <= 8:
                                lista_de_mecanicos.append(mecanico)
                                equipo_completo.append(mecanico)
                            else:
                                print(
                                    "Este equipo tiene el cupo de mecanicos completo")

                    except ValueError:
                        print(
                            "Uno o más datos ingresados son inválidos, intente nuevamente"
                        )
                        continue

            elif num_seleccionado == 2:
                print("Alta de auto")

                try:
                    modelo = Datos.set_modelo()
                    numero = Datos.set_nro_auto()
                    anio = Datos.set_anio()
                    score = Datos.set_score()

                    auto = Auto(modelo, numero, anio, score)
                    lista_de_autos.append(auto)

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    continue

            elif num_seleccionado == 3:
                print("Alta de equipo")

                try:
                    pass

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    continue

            elif num_seleccionado == 4:
                print("Simular carrera")

                try:
                    pass

                except ValueError:
                    print(
                        "Uno o más datos ingresados son inválidos, intente nuevamente"
                    )
                    continue

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

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")

                            continue

                    elif num_seleccionado == 2:
                        print("Resumen campeonato de constructores (equipos)")

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 3:
                        print("Top 5 pilotos mejores pago")

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 4:
                        print("Top 3 pilotos más habilidosos")

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente")
                            continue

                    elif num_seleccionado == 5:
                        print("Retornar jefes de equipo")

                        try:
                            pass

                        except ValueError:
                            print(
                                "Uno o más datos ingresados son inválidos, intente nuevamente"
                            )
                            continue

                except ValueError:
                    print(
                        "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                    )
                    continue

            elif num_seleccionado == 6:
                print("Programa finalizado")
                break

            else:
                print(
                    "El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente"
                )
                continue


if __name__ == "__main__":
    menu = Menu()
    menu.inicio()
