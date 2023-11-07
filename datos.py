
import datetime
from exceptions.tipo_valor_erroneo import TipovalorErroneo
from exceptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido


class Datos:
    def set_cedula():
        try:
            cedula = input("Ingrese la cedula del empleado: ")
            if len(cedula) == 8 and cedula.isdigit():
                cedula = int(cedula)
                return cedula
            else:
                if len(cedula) != 8:
                    print(NoRespetaMetodoDefinido(
                        "La cedula debe tener 8 digitos"))
                else:
                    raise ValueError
        except ValueError:
            print(TipovalorErroneo("La cedula no debe contener letras"))

    def set_nombre():
        while True:
            try:
                nombre = input("Ingrese el nombre del empleado: ")
                if nombre.replace(" ", "").isalpha():
                    return nombre
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo("El nombre no debe contener numeros"))

    def set_fecha_nacimiento():
        while True:
            try:
                fecha_nacimiento = input(
                    "Ingrese la fecha de nacimiento del empleado (dd/mm/aaaa): ")
                fecha_nacimiento = datetime.datetime.strptime(
                    fecha_nacimiento, '%d/%m/%Y')
                return fecha_nacimiento
            except:
                print(NoRespetaMetodoDefinido(
                    "la fecha no fue ingresada de manera correcta"))

    def set_nacionalidad():
        while True:
            try:
                nacionalidad = input("Ingrese la nacionalidad del empleado: ")
                if nacionalidad.replace(" ", "").isalpha():
                    return nacionalidad
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo("La nacionalidad no debe contener numeros"))

    def set_salario():
        while True:
            try:
                salario = input("Ingrese el salario del empleado: ")
                if salario.isdigit():
                    salario = float(salario)
                    return salario
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo("El salario no debe contener letras"))

    def set_cargo():
        while True:
            try:
                print(
                    "posibles cargos: \n 0. Jefe de equipo \n 1. Piloto \n 2. Mecanico")
                cargo = int(input("Ingrese el cargo del empleado: "))
                if cargo in [0, 1, 2]:
                    return cargo
                else:
                    print(NoRespetaMetodoDefinido(
                        "El cargo ingresado no es valido ya que no existe"))
            except ValueError:
                print(TipovalorErroneo("El cargo no debe contener letras"))

    def set_equipo():
        while True:
            try:
                equipo = input("Ingrese el equipo al que pertenece: ")
                if equipo.replace(" ", "").isalpha():
                    return equipo
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo(
                    "El nombre del equipo no debe contener numeros"))

    def set_score():
        while True:
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

    def set_nro_auto():
        while True:
            try:
                nro_auto = int(input("Ingrese el numero de auto del piloto: "))
                return nro_auto
            except:
                print(TipovalorErroneo("El numero de auto no debe contener letras"))

    def set_modelo():
        while True:
            try:
                modelo = input("Ingrese el modelo del auto: ")
                if modelo.isalpha():
                    return modelo
                else:
                    raise ValueError
            except:
                print(NoRespetaMetodoDefinido("el modelo no es valido"))

    def set_anio():
        while True:
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

    def set_titular():
        while True:
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

    def set_imprevistos():
        while True:
            try:
                imprevistos = input("Ingrese los imprevistos del auto: ")
                if imprevistos.replace(" ", "").isalpha():
                    return imprevistos
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo("Los imprevistos no deben contener numeros"))

    def set_lesion():
        while True:
            try:
                lesion = input("Ingrese la lesion del piloto: ")
                if lesion.replace(" ", "").isalpha():
                    return lesion
                else:
                    raise ValueError
            except ValueError:
                print(TipovalorErroneo("La lesion no debe contener numeros"))
