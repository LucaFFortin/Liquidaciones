from estructuras import montos_diarios, liquidaciones

id_liquidacion = 21

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
