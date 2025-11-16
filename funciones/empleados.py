from estructuras import empleados

contador_empleado = 21

def agregar_empleado():
    global contador_empleado
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

def eliminar_empleado():
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

def mostrar_empleados():
    if not empleados:
        print("No hay empleados registrados")
    else:
        for id, datos in empleados.items():
            id_trabajo, turno, nombre, apellido, dni, telefono, edad = datos
            print(f"ID: {id}, nombre: {nombre}, apellido: {apellido}, DNI: {dni}, telefono: {telefono}, ID trabajo: {id_trabajo}, edad: {edad}, turno: {turno}.")

def modificar_empleado():
    while True:
        id_input = input("Ingrese el ID del empleado que quiere modificar: ")
        if id_input.isdigit():
            id_empleado_modificar = int(id_input)
            break
        print("El ID debe ser un numero")
    
    if id_empleado_modificar not in empleados:
        print("El ID no existe")
        return

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
