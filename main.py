def calcular_horas_trabajadas(hora_entrada, hora_salida):
    if hora_salida < hora_entrada:
        return (24 - hora_entrada) + hora_salida
    else:
        return hora_salida - hora_entrada
# ejemplo de la funcion, ponele que entro alas 18 y salio alas 00, ni apalo laburo 18 horas, entonces la funcion reconoce que es mayor y a 24 le resta 18, dando 6, las 6 horas que laburo

# TODO: añadir error handler y sentencias TRY EXCEPT FINALLY

# Estructura empleados = {id_empleado: [id_trabajo, turno, nombre, apellido, dni, telefono, edad]}
empleados = {1: [1, "mañana", "Juan", "Perez", "12345678", "555-1234", 30],
             2: [2, "tarde", "Maria", "Gomez", "87654321", "555-5678", 40],
             3: [1, "mañana", "Carlos", "Lopez", "11223344", "555-8765", 25],
             4: [2, "tarde", "Ana", "Martinez", "44332211", "555-4321", 35]}


# Estructura tipo_trabajos = {(id_trabajo, turno): [puesto, sueldo_hora, area]}
# Actualmente tenemos id 1: obrero, id 2: gerente
tipo_trabajos = {(1, "mañana"): ["Obrero", 1000, "Produccion"],
                 (1, "tarde"): ["Obrero", 1200, "Produccion"],
                 (2, "mañana"): ["Gerente", 3000, "Administracion"],
                 (2, "tarde"): ["Gerente", 3000, "Administracion"]}

# Estructura liquidaciones = {id_liquidacion: [id_empleado, sueldo_bruto, horas_extra, deducciones, periodo]}
liquidaciones = {}

# Estructura jornada = {(fecha, id_empleado): [horario_entrada, horario_salida]}
jornada = {("10/10/2025", 1): [8, 17],
           ("11/10/2025", 2): [8, 18],
           ("12/10/2025", 3): [8, 16],
           ("13/10/2025", 4): [9, 17]}

# Estructura montos_diarios = {id_empleado: {periodo: [[dia, monto, horas_trabajadas, horas_extra], [dia, monto, horas_trabajadas, horas_extra]]}}
# El periodo tiene el formato MM/AAAA
montos_diarios = {}

contador_empleado = 5
id_liquidacion = 1

mensaje = """Que operacion quiere realizar: 
1 = Agregar Empleado
2 = Eliminar empleado
3 = mostrar empleados
4 = modificar empleado
5 = Agregar jornada
6 = Mostrar jornadas
7 = Modificar horarios jornada
8 = Eliminar Jornada
9 = Agregar tipo trabajos
10 = Mostrar tipos de trabajos
11 = Modificar Tipo trabajo
12 = Eliminar tipo trabajo 
13 = Calcular monto del dia
14 = Calcular liquidacion de empleado (#Mostrar liquidaciones)
15 = Mostrar liquidaciones
16 = salir: """

operacion = input(mensaje)

while operacion not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15", "16"]:
    print("Opcion incorrecta, seleccione una opcion valida!")
    operacion = input(mensaje)
    
while operacion != "16":
    if operacion == "1":
        bandera = True
        while bandera:
            while True:
                id_input = input("Ingrese el id del puesto: 1 = Obrero, 2 = Gerente: ")
                if id_input in ["1","2"]:
                    id_trabajo = int(id_input)
                    break
                print("El ID debe ser 1 o 2")
            
            while True:
                turno = input("Ingrese el turno del empleado: ")
                if turno.lower() in ["mañana", "tarde"]:
                    break
                print("el Turno debe ser mañana o tarde")
            
            while True:
                nombre = input("Ingrese el nombre del empleado: ")
                if nombre.strip():
                    break
                print("El nombre no puede estar vacio")
            # el .strip genera stripers, na mentira verifica que el sting no este vacio, ejemplo: ponen " " entonces el .strip elimina los espacios y el if lo toma como False si esta vacio y como True si esta con algo
            while True:
                apellido = input("Ingrese el apellido del empleado: ")
                if apellido.strip():
                    break
                print("El apellido no puede estar vacio")
            
            while True:
                dni = input("Ingrese el DNI del empleado: ")
                if dni.isdigit() and len(dni) == 8:
                    dni_existe = False
                    for empleado_id, datos_empleado in empleados.items():
                        if datos_empleado[4] == dni: 
                            dni_existe = True
                            break
                    if dni_existe:
                        print("Ya existe un empleado con ese DNI")
                    else:
                        break
                else:
                    print("El DNI debe ser de 8 digitos numericos")

#El .isdigit verifica si lo puesto contiene solo numeros y el == 8 verifica que no tenga ni mas ni menos que 8, si no se cumplen esas 2 te corta todo ala mierda
            
            while True:
                telefono = input("Ingrese el telefono del empleado: ")
                if telefono.strip():
                    break
                print("El numero de telefono no puede estar vacio")
            
            while True:
                edad_input = input("Ingrese la edad del empleado: ")
                if edad_input.isdigit() and 18 <= int(edad_input) <= 65:
                    edad = int(edad_input)
                    break
                print("La edad debe ser un numero entre 18 y 65")

            empleados[contador_empleado] = [id_trabajo, turno, nombre, apellido, dni, telefono, edad]
            contador_empleado += 1
            
            while True:
                continuar = input("Desea ingresar otro empleado: 1 = Si, 2 = No: ")
                if continuar in ["1","2"]:
                    break
                print("Opcion debe ser 1 o 2")
            if continuar == "2":
                bandera = False
    
    elif operacion == "2":
        while True:
            id_input = input("Ingrese el ID del empleado que quiere eliminar: ")
            if id_input.isdigit():
                empleado_a_eliminar = int(id_input)
                break
            print("El ID debe ser un numero")
        
        if empleado_a_eliminar not in empleados:
            print("El ID no existe")
        else:
            while True:
                confirmacion = input(f"Esta seguro de eliminar el empleado {empleados[empleado_a_eliminar]}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            if confirmacion == "1":
                empleados.pop(empleado_a_eliminar)
    
    elif operacion == "3":
        if not empleados:
            print("No hay empleados registrados")
        else:
            for id, datos in empleados.items():
                id_trabajo, turno, nombre, apellido, dni, telefono, edad = datos
                print(f"ID: {id}, nombre: {nombre}, apellido: {apellido}, DNI: {dni}, telefono: {telefono}, ID trabajo: {id_trabajo}, edad: {edad}, turno: {turno}.")
    
    elif operacion == "4":
        while True:
            id_input = input("Ingrese el ID del empleado que quiere modificar: ")
            if id_input.isdigit():
                id_empleado_modificar = int(id_input)
                break
            print("El ID debe ser un numero")
        
        if id_empleado_modificar not in empleados:
            print("El ID no existe")
            operacion = input(mensaje)
            continue

        empleado = empleados[id_empleado_modificar]
        etiquetas = ["id_trabajo", "turno", "nombre", "apellido", "dni", "telefono", "edad"]

        for i in range(len(empleado)):
            while True:
                modificar = input(f"Desea modificar {etiquetas[i]} de {empleado[2]}, {empleado[3]}? 1 = Si, 2 = No: ")
                if modificar in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            if modificar != "1":
                continue
            
            while True:
                nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                if etiquetas[i] == "id_trabajo":
                    if nuevo_valor in ["1","2"]:
                        empleado[i] = int(nuevo_valor)
                        break
                    print("La ID trabajo debe ser 1 o 2")
                elif etiquetas[i] == "turno":
                    if nuevo_valor in ["mañana","tarde"]:
                        empleado[i] = nuevo_valor
                        break
                    print("El turno debe ser mañana o tarde")
                elif etiquetas[i] == "edad":
                    if nuevo_valor.isdigit() and 18 <= int(nuevo_valor) <= 65:
                        empleado[i] = int(nuevo_valor)
                        break
                    print("la Edad debe ser un numero entre 18 y 65")
                elif etiquetas[i] == "dni":
                    if nuevo_valor.isdigit() and len(nuevo_valor) == 8:
                        dni_existe = False
                        for emp_id, datos_emp in empleados.items():
                            if emp_id != id_empleado_modificar and datos_emp[4] == nuevo_valor:
                                dni_existe = True
                                break
                        if dni_existe:
                            print("Ya existe un empleado con ese DNI")
                        else:
                            empleado[i] = nuevo_valor
                            break
                    else:
                        print("El DNI debe ser 8 digitos")        
                else:
                    if nuevo_valor.strip():
                        empleado[i] = nuevo_valor
                        break
                    print("El campo no puede estar vacio")

    elif operacion == "5":
        while True:
            fecha = input("Ingrese la fecha de la jornada (DD/MM/AAAA): ")
            if fecha.strip():
                break
            print("La fecha no puede estar vacia")
        
        while True:
            id_input = input("Ingrese el ID del empleado: ")
            if id_input.isdigit():
                id_empleado = int(id_input)
                break
            print("La ID debe ser numero")
        
        if id_empleado not in empleados:
            print("El empleado no existe")
            operacion = input(mensaje)
            continue
        
        while True:
            entrada_input = input("Ingrese la hora de entrada (formato 24hs): ")
            if entrada_input.isdigit() and 00 <= int(entrada_input) <= 23:
                horario_entrada = int(entrada_input)
                break
            print("La hora debe ser entre 00 y 23")
        
        while True:
            salida_input = input("Ingrese la hora de salida (formato 24hs): ")
            if salida_input.isdigit() and 00 <= int(salida_input) <= 23:
                horario_salida = int(salida_input)
                break
            print("La hora debe ser entre 00 y 23")
        
        jornada[(fecha, id_empleado)] = [horario_entrada, horario_salida]
        print("Jornada agregada correctamente")
    
    elif operacion == "6":
        if not jornada:
            print("No hay jornadas registradas")
        else:
            for id_jornada, datos_jornada in jornada.items():
                fecha, id_empleado = id_jornada
                horario_entrada, horario_salida = datos_jornada
                print(f"Fecha: {fecha}, ID Empleado: {id_empleado}, Hora Entrada: {horario_entrada}, Hora Salida: {horario_salida}.")
    
    elif operacion == "7":
        while True:
            fecha_modificar = input("Ingrese la fecha de la jornada que quiere modificar (DD/MM/AAAA): ")
            if fecha_modificar.strip():
                break
            print("La fecha no puede estar vacia")
        
        while True:
            id_input = input("Ingrese el ID del empleado de la jornada que quiere modificar: ")
            if id_input.isdigit():
                id_empleado_modificar = int(id_input)
                break
            print("La ID debe ser numero")

        if (fecha_modificar, id_empleado_modificar) not in jornada:
            print("Jornada no encontrada")
            operacion = input(mensaje)
            continue

        datos_jornada = jornada[(fecha_modificar, id_empleado_modificar)]
        etiquetas = ["Horario de entrada", "Horario de Salida"]
        
        for i in range(len(datos_jornada)):
            while True:
                modificar = input(f"Desea modificar {etiquetas[i]}? 1 = Si, 2 = No: ")
                if modificar in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            if modificar != "1":
                continue
            
            while True:
                nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                if nuevo_valor.isdigit() and 00 <= int(nuevo_valor) <= 23:
                    datos_jornada[i] = int(nuevo_valor)
                    break
                print("La hora debe ser entre 00 y 23")

    elif operacion == "8":
        while True:
            fecha_eliminar = input("Ingrese la fecha de la jornada que quiere eliminar (DD/MM/AAAA): ")
            if fecha_eliminar.strip():
                break
            print("La fecha no puede estar vacia")
        
        while True:
            id_input = input("Ingrese el ID del empleado de la jornada que quiere eliminar: ")
            if id_input.isdigit():
                id_empleado_eliminar = int(id_input)
                break
            print("La ID debe ser numero")

        if (fecha_eliminar, id_empleado_eliminar) not in jornada:
            print("La jornada no existe")
        else:
            while True:
                confirmacion = input(f"Esta seguro de eliminar la jornada del empleado con ID {id_empleado_eliminar} en la fecha {fecha_eliminar}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            if confirmacion == "1":
                jornada.pop((fecha_eliminar, id_empleado_eliminar))
                print("Jornada eliminada correctamente")

    elif operacion == "9":
        while True:
            id_input = input("Ingrese el ID del puesto: ")
            if id_input.isdigit():
                id_trabajo = int(id_input)
                break
            print("La ID debe ser numero")
        
        while True:
            turno_trabajo = input("Ingrese el turno del puesto (Mañana o Tarde): ").lower()
            if turno_trabajo in ["mañana","tarde"]:
                break
            print("Turno debe ser mañana o tarde")
        
        if (id_trabajo, turno_trabajo) in tipo_trabajos:
            print("Ya hay un puesto con esa ID y turno")
            operacion = input(mensaje)
            continue

        while True:
            puesto = input("Ingrese el nombre del puesto: ")
            if puesto.strip():
                break
            print("Puesto no puede estar vacio")
        
        while True:
            sueldo_input = input("Ingrese el sueldo por hora del puesto: ")
            if sueldo_input.isdigit() and int(sueldo_input) > 0:
                sueldo_hora = int(sueldo_input)
                break
            print("Sueldo debe ser numero positivo")
        
        while True:
            area = input("Ingrese el area del puesto: ")
            if area.strip():
                break
            print("Area no puede estar vacia")

        tipo_trabajos[(id_trabajo, turno_trabajo)] = [puesto, sueldo_hora, area]
        print("Tipo de trabajo agregado correctamente")

    elif operacion == "10":
        if not tipo_trabajos:
            print("No hay tipos de trabajos registrados")
        else:
            for id_tipo_trabajo, datos_tipo_trabajo in tipo_trabajos.items():
                id_puesto, turno = id_tipo_trabajo
                puesto, sueldo_hora, area = datos_tipo_trabajo
                print(f"ID Puesto: {id_puesto}, Turno: {turno}, Puesto: {puesto}, Sueldo por hora: {sueldo_hora}, Area: {area}.")

    elif operacion == "11":
        while True:
            id_input = input("Ingrese el ID del puesto que quiere modificar: ")
            if id_input.isdigit():
                id_puesto_modificar = int(id_input)
                break
            print("ID debe ser numero")
        
        while True:
            turno_modificar = input("Ingrese el turno del puesto que quiere modificar (Mañana o Tarde): ").lower()
            if turno_modificar in ["mañana","tarde"]:
                break
            print("Turno debe ser mañana o tarde")

        if (id_puesto_modificar, turno_modificar) not in tipo_trabajos:
            print("Tipo de trabajo no existe")
            operacion = input(mensaje)
            continue

        datos_tipo_trabajo = tipo_trabajos[(id_puesto_modificar, turno_modificar)]
        etiquetas = ["puesto", "sueldo_hora", "area"]

        for i in range(len(datos_tipo_trabajo)):
            while True:
                modificar = input(f"Desea modificar {etiquetas[i]}? 1 = Si, 2 = No: ")
                if modificar in ["1","2"]:
                    break
                print("Opcion debe ser 1 o 2")
            if modificar != "1":
                continue
            
            while True:
                nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                if etiquetas[i] == "sueldo_hora":
                    if nuevo_valor.isdigit() and int(nuevo_valor) > 0:
                        datos_tipo_trabajo[i] = int(nuevo_valor)
                        break
                    print("Sueldo debe ser numero positivo")
                else:
                    if nuevo_valor.strip():
                        datos_tipo_trabajo[i] = nuevo_valor
                        break
                    print("El campo no puede estar vacio")

    elif operacion == "12":
        while True:
            id_input = input("Ingrese el ID del puesto que quiere eliminar: ")
            if id_input.isdigit():
                id_puesto_eliminar = int(id_input)
                break
            print("ID debe ser numero")
        
        while True:
            turno_eliminar = input("Ingrese el turno del puesto que quiere eliminar (Mañana o Tarde): ").lower()
            if turno_eliminar in ["mañana","tarde"]:
                break
            print("Turno debe ser mañana o tarde")

        if (id_puesto_eliminar, turno_eliminar) not in tipo_trabajos:
            print("El tipo de trabajo no existe")
        else:
            while True:
                confirmacion = input(f"Esta seguro de eliminar el tipo de trabajo con ID {id_puesto_eliminar} y turno {turno_eliminar}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("Opcion debe ser 1 o 2")
            if confirmacion == "1":
                tipo_trabajos.pop((id_puesto_eliminar, turno_eliminar))
                print("Tipo de trabajo eliminado correctamente")

    elif operacion == "13":
        while True:
            fecha_calcular = input("Ingrese la fecha que quiere calcular: ")
            if fecha_calcular.strip():
                break
            print("Fecha no puede estar vacia")
        
        while True:
            id_input = input("Ingrese el ID del empleado que quiere calcular: ")
            if id_input.isdigit():
                id_empleado_calcular = int(id_input)
                break
            print("ID debe ser numerico")

        if id_empleado_calcular not in empleados:
            print("El empleado no existe")
            operacion = input(mensaje)
            continue

        clave_jornada = (fecha_calcular, id_empleado_calcular)
        if clave_jornada not in jornada:
            print("No existe jornada para esa fecha y empleado")
            operacion = input(mensaje)
            continue

        id_trabajo_empleado = empleados[id_empleado_calcular][0]
        turno_empleado = empleados[id_empleado_calcular][1]
        clave_trabajo = (id_trabajo_empleado, turno_empleado)
        
        if clave_trabajo not in tipo_trabajos:
            print("No existe configuracion de salario para ese puesto y turno")
            operacion = input(mensaje)
            continue

        datos_jornada = jornada[clave_jornada]
        horario_entrada = datos_jornada[0]
        horario_salida = datos_jornada[1]
        
        horas_trabajadas = calcular_horas_trabajadas(horario_entrada, horario_salida)
        horas_extra = 0

        if horas_trabajadas > 8:
            horas_extra = horas_trabajadas - 8
            horas_normales = 8
        else:
            horas_normales = horas_trabajadas

        sueldo_hora = tipo_trabajos[clave_trabajo][1]
        monto_dia = horas_normales * sueldo_hora + horas_extra * (sueldo_hora * 1.5)
        
        nombre_empleado = empleados[id_empleado_calcular][2]
        apellido_empleado = empleados[id_empleado_calcular][3]
        print(f"Empleado: {nombre_empleado} {apellido_empleado}")
        print(f"Horas trabajadas: {horas_trabajadas} (Normales: {horas_normales}, Extra: {horas_extra})")
        print(f"Sueldo por hora: ${sueldo_hora}")
        print(f"Monto del dia: ${monto_dia:.2f}")
        
        if montos_diarios[id_empleado_calcular][fecha_calcular[3:]]:
            montos_diarios[id_empleado_calcular][fecha_calcular[3:]].append([[fecha_calcular, monto_dia, horas_trabajadas, horas_extra]])
        else:
            montos_diarios[id_empleado_calcular][fecha_calcular[3:]] = [[fecha_calcular, monto_dia, horas_trabajadas, horas_extra]]

    elif operacion == "14":
        empleado_liquidar = input("Ingrese el ID del empleado a liquidar: ")
        periodo_liquidar = input("Ingrese el periodo a liquidar (MM/YYYY): ")
        
        montos = montos_diarios[empleado_liquidar][periodo_liquidar]
        
        total = 0
        
        for monto in montos:
            total += monto[1]
        horas_extra = monto[2]
        jubilacion = total * 0.11
        total -= jubilacion
        pensiones = total * 0.03
        obra_social =total * 0.03
        bruto = total
        neto = total - jubilacion - pensiones - obra_social
        print("Sueldo bruto: ", bruto, "\n Deduccion pension: ", pensiones, "\n Deducion obra social: ", obra_social ,  "\n Total: ", total)

        liquidaciones[id_liquidacion] = [empleado_liquidar, bruto, horas_extra, jubilacion + pensiones + obra_social, periodo_liquidar]
        id_liquidacion += 1
        
    elif operacion == "15":
        if not liquidaciones:
            print("No hay liquidaciones registradas")
        else:
            for clave, datos in liquidaciones.items():
                empleado, bruto, horas_extra, deducciones, periodo = datos
                print(f"ID Liquidacion: {clave}, Empleado: {empleado}, Sueldo Bruto: {bruto}, Horas Extra: {horas_extra}, Deducciones: {deducciones}, Periodo: {periodo}.")
        
    operacion = input(mensaje)