
import datetime
from exeptions.tipo_valor_erroneo import TipovalorErroneo
from exeptions.no_respeta_metodo_definido import NoRespetaMetodoDefinido


class Datos:

    def set_cedula(self, cedula):
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
            
    def set_nombre(self, nombre):
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre.isalpha():
            return nombre
        else:
            raise TipovalorErroneo("El nombre no debe contener numeros")

    def set_fecha_nacimiento(self, fecha_nacimiento):
        fecha_nacimiento = input(
            "Ingrese la fecha de nacimiento del empleado (dd/mm/aaaa): ")
        try:
            fecha_nacimiento = datetime.datetime.strptime(
                fecha_nacimiento, '%d/%m/%Y')
            return fecha_nacimiento
        except:
            raise NoRespetaMetodoDefinido( "la fecha no fue ingresada de manera correcta")
            

    def set_nacionalidad(self, nacionalidad):
        nacionalidad = input("Ingrese la nacionalidad del empleado: ")
        if nacionalidad.isalpha():
            return nacionalidad
        else:
            raise TipovalorErroneo("La nacionalidad no debe contener numeros")

    def set_salario(self, salario):
        salario = input("Ingrese el salario del empleado: ")
        if salario.isdigit():
            salario = float(salario)
            return salario
        else:
            raise TipovalorErroneo("El salario no debe contener letras")

    def set_cargo(self, cargo):
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
                 raise NoRespetaMetodoDefinido("El cargo no es valido, no existe")
            

    def set_equipo(self, equipo):
        equipo = input("Ingrese el equipo al que pertenece: ")
        if equipo.isalpha():
            return equipo
        else:
            raise TipovalorErroneo("El  nombre del equipo no debe contener numeros")

    def set_score(self, score):
        score = input("Ingrese el score del empleado: ")
        if score.isdigit() and score in range(1, 100):
            score = int(score)
            return score
        else:
            if score is not int:
                raise TipovalorErroneo("El score no debe contener letras")
            else:
                if score is not range(1, 100):
                 raise NoRespetaMetodoDefinido("El score no es valido, no esta dento del rango")
        

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
            raise TipovalorErroneo("El modelo del auto no deberia contener numeros")

    def set_anio(self, anio):
        anio = input("Ingrese el año del auto: ")
        if anio.isdigit():
            anio = int(anio)
            return anio
        else:
            raise TipovalorErroneo("El año del auto no deberia contener letras")
