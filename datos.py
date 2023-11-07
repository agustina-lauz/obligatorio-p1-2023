
import datetime
from exeptions.tipo_valor_erroneo import TipovalorErroneo
from exeptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido


class Datos:

    def set_cedula():
        cedula = input("Ingrese la cedula del empleado: ")
        if len(str(cedula)) == 8 and cedula.isdigit():
            cedula = int(cedula)
            return cedula
        else:
            if len(str(cedula)) != 8:
                raise NoRespetaMetodoDefinido("La cedula debe tener 8 digitos")
            else:
                if cedula is not int:
                    raise TipovalorErroneo("La cedula no debe contener letras")

    def set_nombre():
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre.isalpha():
            return nombre
        else:
            raise TipovalorErroneo("El nombre no debe contener numeros")

    def set_fecha_nacimiento():
        fecha_nacimiento = input(
            "Ingrese la fecha de nacimiento del empleado (dd/mm/aaaa): ")
        try:
            fecha_nacimiento = datetime.datetime.strptime(
                fecha_nacimiento, '%d/%m/%Y')
            return fecha_nacimiento
        except:
            raise NoRespetaMetodoDefinido(
                "la fecha no fue ingresada de manera correcta")

    def set_nacionalidad():
        nacionalidad = input("Ingrese la nacionalidad del empleado: ")
        if nacionalidad.isalpha():
            return nacionalidad
        else:
            raise TipovalorErroneo("La nacionalidad no debe contener numeros")

    def set_salario():
        salario = input("Ingrese el salario del empleado: ")
        if salario.isdigit():
            salario = float(salario)
            return salario
        else:
            raise TipovalorErroneo("El salario no debe contener letras")

    def set_cargo():
        print("posibles cargos: \n 0. Jefe de equipo \n 1. Piloto \n 2. Mecanico")
        cargo = input("Ingrese el cargo del empleado: ")
        if cargo.isdigit() and cargo in ["0", "1", "2"]:
            cargo = int(cargo)
            return cargo
        else:
            if cargo is not int:
                raise TipovalorErroneo("El cargo no debe contener letras")
            else:
                if cargo is not ["0", "1", "2"]:
                    raise NoRespetaMetodoDefinido(
                        "El cargo no es valido, no existe")

    def set_equipo():
        equipo = input("Ingrese el equipo al que pertenece: ")
        if equipo.isalpha():
            return equipo
        else:
            raise TipovalorErroneo(
                "El  nombre del equipo no debe contener numeros")

    def set_score():
        try:
            score = int(input("Ingrese el score del empleado: "))
            if 1 <= score <= 100:
                return score
            else:
                raise NoRespetaMetodoDefinido(
                    "El score no es valido, no está dentro del rango 1-100")
        except:
            raise TipovalorErroneo("El score debe ser un número entero")

    def set_nro_auto():
        try:
            nro_auto = int(input("Ingrese el numero de auto del piloto: "))
            return nro_auto

        except:
            raise TipovalorErroneo("El numero de auto no debe contener letras")

    def set_modelo():
        modelo = input("Ingrese el modelo del auto: ")
        if modelo is str:
            return modelo
        else:
            raise NoRespetaMetodoDefinido("el modelo no es valido")

    def set_anio():
        try:
            anio = int(input("Ingrese el año del auto : "))
            if 1990 <= anio <= 2024:
                return anio
            else:
                raise NoRespetaMetodoDefinido(
                    "El año no es valido, no está dentro del rango aceptado.")
        except:
            raise TipovalorErroneo("El año debe ser un número entero")

    def set_titular():
        try:
            titular = int(input(
                "Ingrese 1 si el piloto es titular o 2 si es de reserva: "))

            if titular == 1:
                return True
            elif titular == 2:
                return False
            else:
                raise NoRespetaMetodoDefinido(
                    "El valor ingresado no es valido, debe ser 1 o 2")
        except:
            raise TipovalorErroneo(
                "El nombre del titular no debe contener numeros")

    def set_imprevistos():
        imprevistos = input("Ingrese los imprevistos del auto: ")
        if imprevistos.isalpha():
            return imprevistos
        else:
            raise TipovalorErroneo("Los imprevistos no deben contener numeros")

    def set_lesion():
        lesion = input("Ingrese la lesion del piloto: ")
        if lesion.isalpha():
            return lesion
        else:
            raise TipovalorErroneo("La lesion no debe contener numeros")
