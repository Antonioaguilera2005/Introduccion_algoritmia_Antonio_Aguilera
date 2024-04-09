def calcular_horas_extra(salario_mensual_bruto, horas_extra):
    salario_semanal = salario_mensual_bruto / 4.33  # Aproximación de semanas en un mes
    salario_hora_normal = salario_semanal / 35  # 35 horas trabajadas por semana
    if horas_extra <= 35:  # Sin horas extra
        return 0
    elif horas_extra <= 43:  # Horas extra entre 36 y 43
        horas_extra_normales = horas_extra - 35
        salario_extra = horas_extra_normales * salario_hora_normal * 1.25
    else:  # Horas extra a partir de la 44
        horas_extra_normales = 8  # 43 - 35 = 8 horas ya incluidas
        horas_extra_extra = horas_extra - 43
        salario_extra = horas_extra_normales * salario_hora_normal * 1.25 + horas_extra_extra * salario_hora_normal * 1.5
    
    return round(salario_extra, 2)  # Redondear a 2 decimales

# Ejemplo de uso
horas_extra = 50
salario_extra = calcular_horas_extra(3000, horas_extra)  # Salario mensual bruto: 3000, Horas extra: 50
print("Salario por horas extra:", salario_extra)
