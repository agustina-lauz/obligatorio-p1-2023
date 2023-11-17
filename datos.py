
import datetime
from exceptions.tipo_valor_erroneo import TipovalorErroneo
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste


class Datos:

    @staticmethod
    def validar_cedula(cedula):
        if len(str(cedula)) == 8 and cedula.isdigit():
            return True
        return False
    # checked

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
            # Esta surgiendo un problema, ya que cuando ingnresas una cedula con numeros y letras
            # el programa tira el error " La cedula debe tener 8 digitos y no contener letras" pero en vez de volver
            # al menu, pide el nombre. Yo creo que no esta entendiendo bien la validacion de la cedula
    # checked

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
    # checked

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
    # checked

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
    # checked

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
    # checked

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

        try:
            equipo = input("Ingrese el equipo al que pertenece: ")
            if equipo.replace(" ", "").isalpha():
                return equipo
            else:
                raise ValueError
        except ValueError:
            print(TipovalorErroneo(
                "El nombre del equipo no debe contener numeros"))
    # checked

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
    # checked

    @staticmethod
    def set_nro_auto():
        try:
            nro_auto = int(input("Ingrese el numero de auto del piloto: "))
            return nro_auto
        except ValueError:
            print(TipovalorErroneo("El numero de auto no debe contener letras"))
    # checked

    @staticmethod
    def set_modelo():
        modelo = input("Ingrese el modelo del auto: ")
        return modelo
    # checked

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
    # checked

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
    # checked

    @staticmethod
    def nombre_equipo():
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        return nombre_equipo
    # checked

    @staticmethod
    def empleados_por_equipo():
        empleados_por_equipo = []
        for _ in range(12):
            try:
                cedula_empleado = Datos.set_cedula()
                empleados_por_equipo.append(cedula_empleado)

            except NoRespetaMetodoDefinido:
                print(
                    "Error: La cedula debe tener 8 digitos y no contener letras.")
                break

        return empleados_por_equipo
    # checked

    @staticmethod
    def pilotos_lesionados():

        try:
            pilotos_lesionados = []
            lesionados = input(
                "Ingrese número de auto de todos los pilotos lesionados separados por espacios. Si no existen pilotos lesionados, ingrese 0:")
            if lesionados == "0":
                return pilotos_lesionados
            else:
                lesionados = [int(i) for i in lesionados.split()
                              if i.strip().isdigit()]
                pilotos_lesionados.extend(lesionados)
            return pilotos_lesionados

        except ValueError:
            print("Se ingresaron datos inválidos. Por favor, ingrese solo números.")

    # checked

    @staticmethod
    def pilotos_abandonan():

        try:
            pilotos_abandonan = []
            abandonan = input(
                "Ingrese número de auto de todos los pilotos que abandonan la carrera. Si no existen pilotos que abandonan la carrea, ingrese 0: ")
            if abandonan == "0":
                return pilotos_abandonan
            else:
                abandonan = [int(i) for i in abandonan]
                if abandonan is not None:
                    pilotos_abandonan.extend(abandonan)
                    return pilotos_abandonan
                else:
                    raise ValorNoExiste
        except ValorNoExiste:
            print(NoRespetaMetodoDefinido(
                "No se ingresaron pilotos que abandonan la carrera."))
    # checked

    @staticmethod
    def pilotos_infraccionan():

        try:
            pilotos_infracciones = []
            infracciones = input(
                "Ingrese número de auto de todos los pilotos que tienen infracciones. \nSi el piloto tuvo más de una infracción, ingrese el número de auto tantas veces como infracciones corresponda. \nSi ningun piloto tiene infracciones, ingrese 0: ")
            if infracciones == "0":
                return pilotos_infracciones
            else:
                if infracciones is not None:
                    infracciones = [int(i) for i in infracciones]
                    pilotos_infracciones.extend(infracciones)
                    return pilotos_infracciones
                else:
                    raise ValorNoExiste
        except ValorNoExiste:
            print(ValorNoExiste(
                "Error: Los daots ingresados no son válidos."))
    # checked

    @staticmethod
    def pilotos_errores_pits():

        try:
            lista_errores_pits = []
            errores_en_pits = input(
                "Ingrese número de auto de todos los pilotos que tienen errores en pits. \nSi el piloto tuvo más de un error en pits, ingrese el número de auto tantas veces como errores corresponda. \nSi ningun piloto tiene errores en pits, ingrese 0: ")
            if errores_en_pits == "0":
                return lista_errores_pits
            else:
                errores_en_pits = [int(i) for i in errores_en_pits]
                if errores_en_pits is not None:
                    lista_errores_pits.extend(errores_en_pits)
                    return lista_errores_pits
                else:
                    raise ValorNoExiste
        except ValorNoExiste:
            print(ValorNoExiste(
                "Error: Los datos ingresados no son válidos."))
    # checked

    def mecanicos_equipo(self, equipos, nombre_equipo):
        mecanicos_por_equipo = []
        for equipo in equipos:
            if equipo.nombre == nombre_equipo:
                for mecanico in equipo.mecanicos:
                    mecanicos_por_equipo.append((nombre_equipo, mecanico))
        return mecanicos_por_equipo

    def autos_por_equipo(self, lista_de_autos, equipos, nombre_equipo):
        autos_por_equipo = []
        for auto in lista_de_autos:
            for equipo in equipos:
                if equipo.nombre == nombre_equipo and equipo.modelo_auto == auto.modelo:
                    autos_por_equipo.append(nombre_equipo, auto)
        return autos_por_equipo
