
import datetime
from exceptions.tipo_valor_erroneo import TipovalorErroneo
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido
from exceptions.valor_no_existe import ValorNoExiste

todas_las_cedulas = set()


class Datos:

    @staticmethod
    def validar_cedula(cedula):
        cedula_str = str(cedula)
        if len(cedula_str) == 8 and cedula_str.isdigit():
            return True
        return False
    # checked

    @staticmethod
    def set_cedula():

        try:
            cedula = int(input("Ingrese la cedula del empleado: "))
            Datos.validar_cedula(cedula)
            return cedula

        except NoRespetaMetodoDefinido:
            print(NoRespetaMetodoDefinido(
                "La cedula debe tener 8 digitos y no contener letras"))
            return None
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

        empleados_por_equipo = None
        try:
            cedula_empleado = Datos.set_cedula()

            if cedula_empleado is not None:
                empleados_por_equipo = cedula_empleado

            else:
                raise ValorNoExiste(
                    "La cedula ingresada no esta registrada")

            return empleados_por_equipo

        except ValueError:
            print(TipovalorErroneo(
                "La cedula no debe contener letras"))
        # checked

    @staticmethod
    def pilotos_lesionados():

        try:
            numeros_auto_lesionados = input(
                "Ingrese los números de auto de los pilotos lesionados separados por coma (si está vacío, presione Enter): ")

            autos_con_lesiones = []
            if numeros_auto_lesionados:
                numeros_auto_lesionados = [
                    int(num.strip()) for num in numeros_auto_lesionados.split(',')]
                autos_con_lesiones.extend(numeros_auto_lesionados)
                return autos_con_lesiones
            else:
                return []

        except ValueError:
            print("Se ingresaron datos inválidos. Por favor, ingrese solo números.")
            return []
    # checked

    @staticmethod
    def pilotos_abandonan():

        try:
            numeros_auto_abandonados = input(
                "Ingrese los números de auto de los pilotos que abandonaron la carrera separados por coma (si está vacío, presione Enter): ")

            autos_abandonados = []
            if numeros_auto_abandonados:
                numeros_auto_abandonados = [
                    int(num.strip()) for num in numeros_auto_abandonados.split(',')]
                autos_abandonados.extend(numeros_auto_abandonados)
                return autos_abandonados
            else:
                return []

        except ValueError:
            print("Se ingresaron datos inválidos. Por favor, ingrese solo números.")
            return []
    # checked

    @staticmethod
    def pilotos_infraccionan():

        try:
            numeros_auto_infracciones = input(
                "Ingrese los números de auto de los pilotos que cometieron infracciones separados por coma (si está vacío, presione Enter): ")
            autos_infracciones = []
            if numeros_auto_infracciones:
                numeros_auto_infracciones = [
                    int(num.strip()) for num in numeros_auto_infracciones.split(',')]
                autos_infracciones.extend(numeros_auto_infracciones)
                return autos_infracciones
            else:
                return []

        except ValueError:
            print("Se ingresaron datos inválidos. Por favor, ingrese solo números.")
            return []

    # checked

    @staticmethod
    def pilotos_errores_pits():

        try:
            numeros_auto_errores_pits = input(
                "Ingrese los números de auto de los pilotos que cometieron errores en pits separados por coma (si está vacío, presione Enter): ")
            lista_errores_pits = []
            if numeros_auto_errores_pits:
                numeros_auto_errores_pits = [
                    int(num.strip()) for num in numeros_auto_errores_pits.split(',')]
                lista_errores_pits.extend(numeros_auto_errores_pits)
                return lista_errores_pits
            else:
                return []

        except ValueError:
            print("Se ingresaron datos inválidos. Por favor, ingrese solo números.")
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
