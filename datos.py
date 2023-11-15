
import datetime
from exceptions.tipo_valor_erroneo import TipovalorErroneo
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste


class Datos:

    @staticmethod
    def validar_cedula(cedula):
        return len(cedula) == 8 and cedula.isdigit()

    @staticmethod
    def set_cedula():
        try:
            cedula = input("Ingrese la cedula del empleado: ")

            if Datos.validar_cedula(cedula):
                cedula = int(cedula)
                return cedula
            else:
                raise NoRespetaMetodoDefinido
            
        except NoRespetaMetodoDefinido:
           print(NoRespetaMetodoDefinido(
                    "La cedula debe tener 8 digitos y no contener letras"))
           #Esta surgiendo un problema, ya que cuando ingnresas una cedula con numeros y letras
           # el programa tira el error " La cedula debe tener 8 digitos y no contener letras" pero en vez de volver
           #al menu, pide el nombre. Yo creo que no esta entendiendo bien la validacion de la cedula
           
    @staticmethod
    def set_nombre():
        try:
            nombre = input("Ingrese el nombre del empleado: ")
            if nombre.replace(" ", "").isalpha():
                return nombre
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo("El nombre no debe contener numeros"))

    @staticmethod
    def set_fecha_nacimiento():
        try:
            fecha_nacimiento = input(
                "Ingrese la fecha de nacimiento del empleado (dd/mm/aaaa): ")
            if fecha_nacimiento is not None:
                fecha_nacimiento = datetime.datetime.strptime(
                    fecha_nacimiento, '%d/%m/%Y')
                return fecha_nacimiento
            else:
                raise ValueError
        except ValueError:
            print(NoRespetaMetodoDefinido(
                "la fecha no fue ingresada de manera correcta"))

    @staticmethod
    def set_nacionalidad():
        try:
            nacionalidad = input("Ingrese la nacionalidad del empleado: ")
            if nacionalidad.replace(" ", "").isalpha():
                return nacionalidad
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo("La nacionalidad no debe contener numeros"))

    @staticmethod
    def set_salario():
        try:
            salario = input("Ingrese el salario del empleado: ")
            if salario.isdigit():
                salario = float(salario)
                return salario
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo("El salario no debe contener letras"))

    @staticmethod
    def set_cargo():
        try:
            print(
                "posibles cargos: \n 1. Piloto titular \n 2. Piloto de reserva \n 3. Mecanico \n 4. Jefe de equipo")
            cargo = int(input("Ingrese el cargo del empleado: "))
            if cargo in [1, 2, 3, 4]:
                return cargo
            else:
                print(NoRespetaMetodoDefinido(
                    "El cargo ingresado no es valido ya que no existe"))
        except ValueError:
            print(TipovalorErroneo("El cargo no debe contener letras"))

    @staticmethod
    def set_equipo():
        try:
            equipo = input("Ingrese el equipo al que pertenece: ")
            if equipo.replace(" ", "").isalpha():
                return equipo
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo(
                "El nombre del equipo no debe contener numeros"))

    @staticmethod
    def set_score():
        try:
            score = int(input("Ingrese el score correspondiente: "))
            if 1 <= score <= 100:
                return score
            elif score < 1 or score > 100:
                print(NoRespetaMetodoDefinido(
                    "El score no es valido, no está dentro del rango 1-100"))
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo(
                "El score debe ser un número entero y no puede contener letras"))

    @staticmethod
    def set_nro_auto():
        while True:
            try:
                nro_auto = int(input("Ingrese el numero de auto del piloto: "))
                return nro_auto
            except ValueError:
                print(TipovalorErroneo("El numero de auto no debe contener letras"))

    @staticmethod
    def set_modelo():
        modelo = input("Ingrese el modelo del auto: ")
        return modelo

    @staticmethod
    def set_anio():
        try:
            anio = int(input("Ingrese el año del auto : "))
            if 1990 <= anio <= 2024:
                return anio
            elif anio < 1990 or anio > 2024:
                print(NoRespetaMetodoDefinido(
                    "El año no es valido, no está dentro del rango aceptado."))
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo(
                "El año debe ser un número entero y no debe contener letras"))

    @staticmethod
    def set_titular():
        try:
            titular = int(
                input("Ingrese 1 si el piloto es titular o 2 si es de reserva: "))
            if titular == 1:
                return True
            elif titular == 2:
                return False
            elif titular != 1 or titular != 2:
                print(NoRespetaMetodoDefinido(
                    "El valor ingresado no es valido, debe ser 1 o 2"))
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo(
                "El valor del titular no debe contener letras"))

    @staticmethod
    def nombre_equipo():
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        return nombre_equipo

    @staticmethod
    def empleados_por_equipo():
        empleados_por_equipo = []
        for _ in range(12):
            try:
                cedula_empleado = int(input(
                    "Ingrese la cedula del empleado: "))

                if not cedula_empleado:
                    print(ValorNoExiste(" No se ingreso cedula de empleado"))
                    break

                empleados_por_equipo.append(cedula_empleado)
            except ValueError:
                print(ValorNoExiste(
                    "Error: Ingrese una cédula válida (número entero)."))
                continue

        return empleados_por_equipo

    @staticmethod
    def pilotos_lesionados():
        while True:
            try:
                pilotos_lesionados = []
                lesionados = input(
                    "Ingrese la cedula de el piloto lesionado: ")
                print(
                    "si existen mas pilotos lesionados ingrese su cedula, sino ingrese 0")
                lesionados = [int(i) for i in lesionados]
                if lesionados is not None:
                    pilotos_lesionados.extend(lesionados)
                    return pilotos_lesionados
                elif lesionados == 0:
                    break
                else:
                    raise ValorNoExiste
            except ValorNoExiste:
                print(NoRespetaMetodoDefinido(
                    "No se ingresaron pilotos lesionados"))

    @staticmethod
    def pilotos_abandonan():
        while True:
            try:
                pilotos_abandonan = []
                abandonan = input(
                    "Ingrese la cedula de el piloto que abandono la carrera: ")
                print(
                    "si existen mas pilotos que abandonaron ingrese su cedula, sino ingrese 0")
                abandonan = [int(i) for i in abandonan]
                if abandonan is not None:
                    pilotos_abandonan.extend(abandonan)
                    return pilotos_abandonan
                elif abandonan == 0:
                    break
                else:
                    raise ValorNoExiste
            except ValorNoExiste:
                print(NoRespetaMetodoDefinido(
                    "No se ingresaron pilotos que abandonan"))

    @staticmethod
    def pilotos_infraccionan():
        lista_infracciones = []

        while True:
            try:
                cedula_infracciones = int(input(
                    "Ingrese cédula del piloto que tiene infracciones (o ingrese una cédula vacía para salir): "))

                if not cedula_infracciones:
                    print(ValorNoExiste(" No se ingreso cedula de piloto"))
                    break
                else:
                    cantidad_infracciones = int(
                        input("Ingrese la cantidad de infracciones: "))
                    if cantidad_infracciones is None:
                        raise ValorNoExiste
            except ValorNoExiste:
                print(ValorNoExiste(
                    "Error: Ingrese una cédula y cantidad válidas (números enteros)."))
                continue

            lista_infracciones.append(
                (cedula_infracciones, cantidad_infracciones))

        return lista_infracciones

    @staticmethod
    def pilotos_errores_pits():

        lista_errores_pits = []

        while True:
            try:
                cedula_errores_pits = input(
                    "Ingrese cédula del piloto con errores en pits (o ingrese una cédula vacía para salir): ")

                if not cedula_errores_pits:
                    print(ValorNoExiste(" No se ingreso cedula de piloto"))
                    break

                else:
                    cantidad_errores_pits = int(
                        input("Ingrese la cantidad de errores en pits: "))
                    if cantidad_errores_pits is None:
                        raise ValorNoExiste
            except ValorNoExiste:
                print(ValorNoExiste(
                    "Error: Ingrese una cantidad válida (número entero)."))
                continue

            lista_errores_pits.append(
                (cedula_errores_pits, cantidad_errores_pits))

        return lista_errores_pits
