# ============================================
# PROGRAMA:
# Clasificación de sesiones de clientes
# Curso: Fundamentos de Programación
#Grupo: (213022A_2201)
# ============================================

# Matriz de sesiones de clientes
# Formato:
# [ID Cliente, Duración en segundos, Cantidad de clics]

sesiones = [
    [101, 200, 10],
    [102, 40, 2],
    [103, 120, 5],
    [104, 300, 15],
    [105, 55, 1]
]

# ============================================
# Función para clasificar el compromiso
# ============================================

def clasificar_compromiso(duracion, clics):

    # Clasificación ALTO
    if duracion > 180 and clics > 8:
        return "Alto"

    # Clasificación BAJO
    elif duracion < 60 or clics < 3:
        return "Bajo"

    # Clasificación MEDIA
    else:
        return "Medio"


# ============================================
# ENCABEZADO DEL INFORME
# ============================================

print("===================================")
print(" INFORME DE CLASIFICACIÓN")
print(" SESIONES DE CLIENTES")
print("===================================")

# ============================================
# RECORRIDO DE LA MATRIZ
# ============================================

for sesion in sesiones:

    # Extraer de datos
    cliente_id = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    # Llamar la función
    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostrar resultados
    print("-----------------------------------")
    print("Cliente ID:", cliente_id)
    print("Duración:", duracion, "segundos")
    print("Clics:", clics)
    print("Nivel de compromiso:", clasificacion)

# ============================================
# FIN DEL PROGRAMA
# ============================================

print("===================================")
print(" FIN DEL INFORME")
print("===================================")