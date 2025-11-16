from estructuras import empleados, jornadas

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
    
    jornadas[(fecha, id_empleado)] = [horario_entrada, horario_salida]
    print("Jornada agregada correctamente")

def mostrar_jornadas():
    if not jornadas:
        print("No hay jornadas registradas")
    else:
        for id_jornada, datos_jornada in jornadas.items():
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

    if (fecha_modificar, id_empleado_modificar) not in jornadas:
        print("Jornada no encontrada")
        return

    datos_jornada = jornadas[(fecha_modificar, id_empleado_modificar)]
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

    if (fecha_eliminar, id_empleado_eliminar) not in jornadas:
        print("La jornada no existe")
    else:
        while True:
            confirmacion = input(f"Esta seguro de eliminar la jornada del empleado con ID {id_empleado_eliminar} en la fecha {fecha_eliminar}, 1 = Si, 2 = No: ")
            if confirmacion in ["1","2"]:
                break
            print("La opcion debe ser 1 o 2")
        if confirmacion == "1":
            jornadas.pop((fecha_eliminar, id_empleado_eliminar))
            print("Jornada eliminada correctamente")
