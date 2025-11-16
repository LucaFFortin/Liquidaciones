from funciones.empleados import agregar_empleado, modificar_empleado, mostrar_empleados, eliminar_empleado
from funciones.jornadas import agregar_jornada, modificar_jornada, mostrar_jornadas, eliminar_jornada
from funciones.tipo_trabajos import agregar_tipo_trabajo, modificar_tipo_trabajo, mostrar_tipos_trabajos, eliminar_tipo_trabajo

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
