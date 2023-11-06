
import datetime


class Datos:

    def set_cedula(self, cedula):
        cedula = input("Ingrese la cedula del empleado: ")
        if len(str(cedula)) == 8 and cedula.isdigit():
            cedula = int(cedula)
            return cedula
        else:
            raise ValueError

    def set_nombre(self, nombre):
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre.isalpha():
            return nombre
        else:
            raise ValueError

    def set_fecha_nacimiento(self, fecha_nacimiento):
        fecha_nacimiento = input(
            "Ingrese la fecha de nacimiento del empleado (dd/mm/aaaa): ")
        try:
            fecha_nacimiento = datetime.datetime.strptime(
                fecha_nacimiento, '%d/%m/%Y')
            return fecha_nacimiento
        except ValueError():
            pass

    def set_nacionalidad(self, nacionalidad):
        nacionalidad = input("Ingrese la nacionalidad del empleado: ")
        if nacionalidad.isalpha():
            return nacionalidad
        else:
            raise ValueError

    def set_salario(self, salario):
        salario = input("Ingrese el salario del empleado: ")
        if salario.isdigit():
            salario = float(salario)
            return salario
        else:
            raise ValueError

    def set_cargo(self, cargo):
        cargo = input("Ingrese el cargo del empleado: ")
        if cargo.isdigit():
            cargo = int(cargo)
            return cargo
        else:
            raise ValueError

    def set_equipo(self, equipo):
        equipo = input("Ingrese el equipo del empleado: ")
        if equipo.isalpha():
            return equipo
        else:
            raise ValueError

    def set_score(self, score):
        score = input("Ingrese el score del empleado: ")
        if score.isdigit():
            score = int(score)
            return score
        else:
            raise ValueError

    def set_nro_auto(self, nro_auto):
        nro_auto = input("Ingrese el numero de auto del piloto: ")
        if nro_auto.isdigit():
            nro_auto = int(nro_auto)
            return nro_auto
        else:
            raise ValueError

    def set_modelo(self, modelo):
        modelo = input("Ingrese el modelo del auto: ")
        if modelo.isalpha():
            return modelo
        else:
            raise ValueError

    def set_anio(self, anio):
        anio = input("Ingrese el año del auto: ")
        if anio.isdigit():
            anio = int(anio)
            return anio
        else:
            raise ValueError
