# obligatorio-p1-2023
# Simulación de carreras del Campeonato de F1
Este programa esta diseñado para realizar la simulacion de carreras del campeonato de F1,
brindando la posibilidad de crear pilotos, mecanicos, jefes de equipos y autos para lograr formar el equipo
y asi poder correr la carrera.

## Requisitos:
para ejecutar dicho programa, es nesesario tener:
1. Python 3.X (se recomienda la version 3.11)
2. Visual Studio Code

## Pasos para descargar el programa:
Instrucciones para descargar el programa mediante la consola:
1. Ingrese a Github, y luego al respectivo repositorio.
2. Ve a donde dice "code", precione HTTPS, y copie el enlace que aparece debajo.
3. Abra Visual Studio Code.
4. Precione los 3 puntitos que se encuentran alado de "run", y abra una nueva terminal.
5. En la terminal, escriba : 'git clone 'seguido del enlace copiado en el paso 2.
6. Luego de estos pasos, la copia del proyecto se encontrara en tu computador, listo para comenzar a ejecutarlo.

## Uso
Para asegurarse de que el programa funcione sin pequeños percanses,
recomendamos abrir los archivos para que carguen del todo.
Para luego poder continuar con la ejecucion:
1. Vaya a la carpeta que dice "main_menu.py".
2. Luego dentro de esta, precione el simbolito de reproduccion (play) que aparece arriba a la derecha.
3. Una vez precionado, Visual Studio abrira una terminal.
4. En dicha terminal aparecerar opciones e informacion para completar.
5. Responda en la misma terminal, y el programa seguira corriendo solo.


## Estructura de archivos
El programa se encuentra en una carpeta llamada Obligatorio-P1-2023.
La misma esta conformada por dos archivos sueltos: 
1. 'datos.py'
En el cual se encuentran las funciones y exeption sobre las caracteristicas y datos importantes a solicitar.

2.'main_menu.py'
En esta carpeta es donde se encuentra el sector de prueba del programa, el cual corre todos los archivos fromando la simulacion de la carrera.

Y por dos carpetas:
1. **Entities: ** en esta carpeta se encuentran las respectivas clases que hay que usar para ejecutar el programa 
('auto.py', 'consultas.py', 'empleados.py', 'equipos.py', 'pilotos.py').

2. **Exeptions: ** en esta carpeta se encuentran los archivos correspondientes a los posibles errores a encontrar al ejecutar el programa ('no_respeta_metodo_definido.py', 'tipo_valor_erroneo.py', 'valor_no_existe.py', 'valor_ya_existe.py').

## Modelo UML
### Clase Empleado
- Atributos:
  - Cedula
  - Nombre
  - Fecha de nacimiento
  - Nacionalidad
  - Salario
  - Cargo
  - (Opcional) Score

### Clase Piloto (Herencia de Empleado)
- Atributos adicionales:
  - NroAuto

### Clase Equipo
- Atributos:
  - NombreEquipo
  - ModeloAuto

### Clase Auto
- Atributos:
  - Modelo
  - Año
  - Score

### Clase Datos
- Métodos:
  - validar_cedula(cedula)
  - set_cedula()
  - set_nombre()
  - set_fecha_nacimiento()
  - set_nacionalidad()
  - set_cargo()
  - set_score()
  - set_nro_auto()
  - set_modelo()
  - set_anio()
  - set_titular()
  - nombre_equipo()
  - empleados_por_equipo()
  - mecanicos_equipo(equipos, nombre_equipo)
  - autos_por_equipo(lista_de_autos, equipos, nombre_equipo)
### Relaciones
- La clase Piloto hereda de la clase Empleado (Relación de herencia).
- La clase Equipo está compuesta por 12 instancias de la clase Empleado y 1 instancia de la clase Auto (Relación de composición).

## Problemas conocidos
Hasta ahora, el programa no cuenta con problemas conocidos.
Sin embargo, se espera en unos años, al lograr implementar este programa en la vida real, el que puedan surgir problemas desconocidos.

## Contacto
alauz1@correo.um.edu.uy
fpaguirre@correo.um.edu.uy

## Agradecimiento
Agradecemos al equipo por el desarrollo del proyecto, ya que fue un desafio. Tambien agradecemos al profesor quien nos impulso a ir a mas.
