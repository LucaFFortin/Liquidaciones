from estructuras import empleados, montos_diarios, jornadas, tipo_trabajos
from funciones.auxiliares import calcular_horas_trabajadas

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
    if clave_jornada not in jornadas:
        print("No existe jornada para esa fecha y empleado")
        return

    id_trabajo_empleado = empleados[id_empleado_calcular][0]
    turno_empleado = empleados[id_empleado_calcular][1]
    clave_trabajo = (id_trabajo_empleado, turno_empleado)
    
    if clave_trabajo not in tipo_trabajos:
        print("No existe configuracion de salario para ese puesto y turno")
        return

    datos_jornada = jornadas[clave_jornada]
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
