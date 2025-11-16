def calcular_horas_trabajadas(hora_entrada, hora_salida):
    if hora_salida < hora_entrada:
        return (24 - hora_entrada) + hora_salida
    else:
        return hora_salida - hora_entrada