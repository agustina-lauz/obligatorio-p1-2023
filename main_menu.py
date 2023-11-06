# from entities.pilotos import Piloto
# from entities.auto import Auto
# from entities.equipos import Equipo
# from entities.consultas import Consultas
# from entities.empleados import Empleado


class Menu():

    def inicio(self) -> None:

       # lista_de_empleados = []
       # lista_de_autos = []
       # lista_de_equipos = []

        while True:

            print('Menu principal')
            print('Seleccione la opcion del menú:')
            print('1. Alta de empleado')
            print('2. Alta de auto')
            print('3. Alta de equipo')
            print('4. Simular carrera')
            print('5. Realizar consultas')
            print('6. Finalizar programa')

            num_seleccionado = input('Ingrese Número:')

            if num_seleccionado.isdigit():
                num_seleccionado = int(num_seleccionado)
            else:
                print('El dato ingresado no es un numero, intente nuevamente')
                continue

            if num_seleccionado == 1:

                print('Alta de empleado')

                try:
                    pass

                except ValueError:
                    print(
                        'Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            elif num_seleccionado == 2:

                print('Alta de auto')

                try:
                    pass

                except ValueError:
                    print(
                        'Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            elif num_seleccionado == 3:

                print('Alta de equipo')

                try:
                    pass

                except ValueError:
                    print(
                        'Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            elif num_seleccionado == 4:

                print('Simular carrera')

                try:
                    pass

                except ValueError:
                    print(
                        'Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            elif num_seleccionado == 5:

                print('Realizar consultas')

                try:
                    print(
                        '1. Top 10 pilotos con más puntos en el campeonato')
                    print(
                        '2. Resumen campeonato de constructores (equipos)')
                    print('3. Top 5 pilotos mejores pago')
                    print(
                        '4. Top 3 pilotos más habilidosos')
                    print(
                        '5. Retornar jefes de equipo')

                    num_seleccionado = input('Ingrese número: ')

                    if num_seleccionado.isdigit():
                        num_seleccionado = int(num_seleccionado)
                    else:
                        print(
                            'Uno o más datos ingresados son inválidos, intente nuevamente')
                        continue

                    if num_seleccionado == 1:
                        print('Top 10 pilotos con más puntos en el campeonato')

                        try:
                            pass

                        except ValueError:
                            print(
                                'Uno o más datos ingresados son inválidos, intente nuevamente')
                            continue

                    elif num_seleccionado == 2:
                        print('Resumen campeonato de constructores (equipos)')

                        try:
                            pass

                        except ValueError:
                            print(
                                'Uno o más datos ingresados son inválidos, intente nuevamente')
                            continue

                    elif num_seleccionado == 3:
                        print('Top 5 pilotos mejores pago')

                        try:
                            pass

                        except ValueError:
                            print(
                                'Uno o más datos ingresados son inválidos, intente nuevamente')
                            continue

                    elif num_seleccionado == 4:
                        print('Top 3 pilotos más habilidosos')

                        try:
                            pass

                        except ValueError:
                            print(
                                'Uno o más datos ingresados son inválidos, intente nuevamente')
                            continue

                    elif num_seleccionado == 5:
                        print('Retornar jefes de equipo')

                        try:
                            pass

                        except ValueError:
                            print(
                                'Uno o más datos ingresados son inválidos, intente nuevamente')
                            continue

                except ValueError:
                    print(
                        'El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente')
                    continue

            elif num_seleccionado == 6:

                print('Programa finalizado')
                break

            else:
                print(
                    'El dato ingresado no se corresponde con ninguna de las opciones, intente nuevamente')
                continue
