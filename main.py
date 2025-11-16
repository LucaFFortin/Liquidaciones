from estructuras import empleados, tipo_trabajos, jornada, montos_diarios, liquidaciones
from funciones.empleados import agregar_empleado, modificar_empleado, mostrar_empleados, eliminar_empleado

contador_empleado = 21
id_liquidacion = 21

def calcular_horas_trabajadas(hora_entrada, hora_salida):
    if hora_salida < hora_entrada:
        return (24 - hora_entrada) + hora_salida
    else:
        return hora_salida - hora_entrada

def agregar_jornada():
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
        return
    
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

def mostrar_jornadas():
    if not jornada:
        print("No hay jornadas registradas")
    else:
        for id_jornada, datos_jornada in jornada.items():
            fecha, id_empleado = id_jornada
            horario_entrada, horario_salida = datos_jornada
            print(f"Fecha: {fecha}, ID Empleado: {id_empleado}, Hora Entrada: {horario_entrada}, Hora Salida: {horario_salida}.")

def modificar_jornada():
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
        return

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

def eliminar_jornada():
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

def agregar_tipo_trabajo():
    while True:
        id_input = input("Ingrese el ID del puesto: ")
        if id_input.isdigit():
            id_trabajo = int(id_input)
            break
        print("La ID debe ser numero")
    
    while True:
        turno_trabajo = input("Ingrese el turno del puesto (Manana o Tarde): ").lower()
        if turno_trabajo in ["manana","tarde"]:
            break
        print("Turno debe ser manana o tarde")
    
    if (id_trabajo, turno_trabajo) in tipo_trabajos:
        print("Ya hay un puesto con esa ID y turno")
        return

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

def mostrar_tipos_trabajos():
    if not tipo_trabajos:
        print("No hay tipos de trabajos registrados")
    else:
        for id_tipo_trabajo, datos_tipo_trabajo in tipo_trabajos.items():
            id_puesto, turno = id_tipo_trabajo
            puesto, sueldo_hora, area = datos_tipo_trabajo
            print(f"ID Puesto: {id_puesto}, Turno: {turno}, Puesto: {puesto}, Sueldo por hora: {sueldo_hora}, Area: {area}.")

def modificar_tipo_trabajo():
    while True:
        id_input = input("Ingrese el ID del puesto que quiere modificar: ")
        if id_input.isdigit():
            id_puesto_modificar = int(id_input)
            break
        print("ID debe ser numero")
    
    while True:
        turno_modificar = input("Ingrese el turno del puesto que quiere modificar (Manana o Tarde): ").lower()
        if turno_modificar in ["manana","tarde"]:
            break
        print("Turno debe ser manana o tarde")

    if (id_puesto_modificar, turno_modificar) not in tipo_trabajos:
        print("Tipo de trabajo no existe")
        return

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

def eliminar_tipo_trabajo():
    while True:
        id_input = input("Ingrese el ID del puesto que quiere eliminar: ")
        if id_input.isdigit():
            id_puesto_eliminar = int(id_input)
            break
        print("ID debe ser numero")
    
    while True:
        turno_eliminar = input("Ingrese el turno del puesto que quiere eliminar (Manana o Tarde): ").lower()
        if turno_eliminar in ["manana","tarde"]:
            break
        print("Turno debe ser manana o tarde")

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

def calcular_monto():
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
        return

    clave_jornada = (fecha_calcular, id_empleado_calcular)
    if clave_jornada not in jornada:
        print("No existe jornada para esa fecha y empleado")
        return

    id_trabajo_empleado = empleados[id_empleado_calcular][0]
    turno_empleado = empleados[id_empleado_calcular][1]
    clave_trabajo = (id_trabajo_empleado, turno_empleado)
    
    if clave_trabajo not in tipo_trabajos:
        print("No existe configuracion de salario para ese puesto y turno")
        return

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
    
    periodo = fecha_calcular[3:]
    if id_empleado_calcular not in montos_diarios:
        montos_diarios[id_empleado_calcular] = {}
    if periodo not in montos_diarios[id_empleado_calcular]:
        montos_diarios[id_empleado_calcular][periodo] = []
    
    for monto in montos_diarios[id_empleado_calcular][periodo]:
        if monto[0] == fecha_calcular:
            print("Ya existe un monto registrado para ese dia y empleado")
            break
    else:
        montos_diarios[id_empleado_calcular][periodo].append([fecha_calcular, monto_dia, horas_trabajadas, horas_extra])

def mostrar_montos():
    if not montos_diarios:
        print("No hay montos diarios registrados")
    else:
        for id_empleado, datos_monto in montos_diarios.items():
            nombre, apellido = empleados[id_empleado][2], empleados[id_empleado][3]
            print(f"Empleado: {nombre} {apellido}")
            for periodo, datos_periodo in datos_monto.items():
                print(f"Periodo: {periodo}")
                for datos in datos_periodo:
                    dia, monto, horas_trabajadas, horas_extra = datos
                    print(f"Dia: {dia}, monto: {monto}, horas trabajadas: {horas_trabajadas}, horas extra: {horas_extra}")

def actualizar_monto():
    empleado_actualizar = int(input("Ingrese el ID del empleado a actualizar el monto: "))
    periodo_actualizar = input("Ingrese el periodo a actualizar (MM/YYYY): ")
    fecha_actualizar = input("Ingrese la fecha a actualizar (DD/MM/YYYY): ")
    
    montos = montos_diarios[empleado_actualizar][periodo_actualizar]
    
    for i in range(len(montos)):
        if montos[i][0] == fecha_actualizar:
            nuevo_monto_input = input("Ingrese el nuevo monto: ")
            if nuevo_monto_input.replace('.','',1).isdigit():
                nuevo_monto = float(nuevo_monto_input)
                montos[i][1] = nuevo_monto
                print("Monto actualizado correctamente")
            else:
                print("El monto debe ser un numero")
            break
    else:
        print("No se encontro la fecha especificada")

def eliminar_monto():
    empleado_eliminar = int(input("Ingrese el ID del empleado a eliminar el monto: "))
    periodo_eliminar = input("Ingrese el periodo a eliminar (MM/YYYY): ")
    fecha_eliminar = input("Ingrese la fecha a eliminar (DD/MM/YYYY): ")
    
    montos = montos_diarios[empleado_eliminar][periodo_eliminar]
    
    for i in range(len(montos)):
        if montos[i][0] == fecha_eliminar:
            montos.pop(i)
            print("Monto eliminado correctamente")
            break
    else:
        print("No se encontro la fecha especificada")

def calcular_liquidacion():
    global id_liquidacion
    empleado_liquidar = int(input("Ingrese el ID del empleado a liquidar: "))
    periodo_liquidar = input("Ingrese el periodo a liquidar (MM/YYYY): ")
    
    if empleado_liquidar not in montos_diarios or periodo_liquidar not in montos_diarios[empleado_liquidar]:
        print("No hay montos registrados para ese empleado y periodo")
        return
    
    montos = montos_diarios[empleado_liquidar][periodo_liquidar]
    
    total = 0
    horas_extra_total = 0
    
    for monto in montos:
        total += monto[1]
        horas_extra_total += monto[3]
    
    jubilacion = total * 0.11
    pensiones = total * 0.03
    obra_social = total * 0.03
    bruto = total
    neto = total - jubilacion - pensiones - obra_social
    
    print("Sueldo bruto: ", bruto, "\n Deduccion pension: ", pensiones, "\n Deducion obra social: ", obra_social, "\n Total: ", neto)

    liquidaciones[id_liquidacion] = [empleado_liquidar, bruto, horas_extra_total, jubilacion + pensiones + obra_social, periodo_liquidar]
    id_liquidacion += 1

def mostrar_liquidaciones():
    if not liquidaciones:
        print("No hay liquidaciones registradas")
    else:
        for clave, datos in liquidaciones.items():
            empleado, bruto, horas_extra, deducciones, periodo = datos
            print(f"ID Liquidacion: {clave}, Empleado: {empleado}, Sueldo Bruto: {bruto}, Horas Extra: {horas_extra}, Deducciones: {deducciones}, Periodo: {periodo}.")

def eliminar_liquidacion():
    while True:
        id_input = input("Ingrese el ID de la liquidacion que quiere eliminar: ")
        if id_input.isdigit():
            id_liquidacion_eliminar = int(id_input)
            break
        print("El ID debe ser un numero")
    
    if id_liquidacion_eliminar not in liquidaciones:
        print("La liquidacion no existe")
    else:
        while True:
            confirmacion = input(f"Esta seguro de eliminar la liquidacion con ID {id_liquidacion_eliminar}, 1 = Si, 2 = No: ")
            if confirmacion in ["1","2"]:
                break
            print("La opcion debe ser 1 o 2")
        if confirmacion == "1":
            liquidaciones.pop(id_liquidacion_eliminar)
            print("Liquidacion eliminada correctamente")

def main():
    mensaje = """Que operacion quiere realizar: 
Empleado:           1 = Agregar Empleado, 2 = Eliminar empleado, 3 = mostrar empleados, 4 = modificar empleado.
Jornadas:           5 = Agregar jornada, 6 = Mostrar jornadas, 7 = Modificar horarios jornada, 8 = Eliminar Jornada.
Cargos laborales:   9 = Agregar tipo trabajos, 10 = Mostrar tipos de trabajos, 11 = Modificar Tipo trabajo, 12 = Eliminar tipo trabajo.
Montos diarios:     13 = Calcular monto, 14 = Mostrar montos, 15 = Actualizar monto, 16 = Eliminar monto.
Liquidaciones:      17 = Calcular liquidacion de empleado, 18 = Mostrar liquidaciones, 19 = eliminar liquidacion.
Para salir de la aplicacion = Ingrese "20".
------------------------------
Ingrese la operacion a realizar: """

    operacion = input(mensaje)

    while operacion not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Opcion incorrecta, seleccione una opcion valida!")
        operacion = input(mensaje)
        
    while operacion != "20":
        if operacion == "1":
            agregar_empleado()
        elif operacion == "2":
            eliminar_empleado()
        elif operacion == "3":
            mostrar_empleados()
        elif operacion == "4":
            modificar_empleado()
        elif operacion == "5":
            agregar_jornada()
        elif operacion == "6":
            mostrar_jornadas()
        elif operacion == "7":
            modificar_jornada()
        elif operacion == "8":
            eliminar_jornada()
        elif operacion == "9":
            agregar_tipo_trabajo()
        elif operacion == "10":
            mostrar_tipos_trabajos()
        elif operacion == "11":
            modificar_tipo_trabajo()
        elif operacion == "12":
            eliminar_tipo_trabajo()
        elif operacion == "13":
            calcular_monto()
        elif operacion == "14":
            mostrar_montos()
        elif operacion == "15":
            actualizar_monto()
        elif operacion == "16":
            eliminar_monto()
        elif operacion == "17":
            calcular_liquidacion()
        elif operacion == "18":
            mostrar_liquidaciones()
        elif operacion == "19":
            eliminar_liquidacion()

        operacion = input(mensaje)
        
if __name__ == "__main__":
    main()
