def precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos

# Ejemplo de uso
precio_final = precio_con_impuestos(100, 21)  # Precio sin impuestos: 100, IVA: 21%
print("Precio con impuestos:", precio_final)


def calcular_intereses(capital, tasa_interes, tiempo_meses):
    intereses = (capital * tasa_interes / 100) * tiempo_meses
    return intereses

# Ejemplo de uso
intereses_generados = calcular_intereses(1000, 5, 12)  # Capital: 1000, Tasa de interés: 5%, Tiempo en meses: 12
print("Intereses generados:", intereses_generados)
