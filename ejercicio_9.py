def media_aritmetica(a, b, c):
    return (a + b + c) / 3

# Ejemplo de uso
media = media_aritmetica(10, 20, 30)  # Números: 10, 20, 30
print("Media aritmética:", media)



def media_ponderada(a, b, c, coef_a, coef_b, coef_c):
    numerador = a * coef_a + b * coef_b + c * coef_c
    denominador = coef_a + coef_b + coef_c
    return numerador / denominador

# Ejemplo de uso
media_ponderada = media_ponderada(10, 20, 30, 0.2, 0.3, 0.5)  # Números: 10, 20, 30; Coeficientes: 0.2, 0.3, 0.5
print("Media ponderada:", media_ponderada)
