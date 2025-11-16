from estructuras import tipo_trabajos

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
