sesiones = [
    [1, 245, 12],
    [2,  45,  2],
    [3, 130,  6],
    [4, 300, 10],
    [5,  55,  9],
    [6, 200,  4],
    [7,  990, 116],
    [8,  20,  1],
    [9, 185,  9],
    [10,  70,  3],
]

def clasificar_sesion(duracion, clics):
 
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_informe(sesiones):

    print(f"{'ID Cliente':<14} {'Duración':<15} {'Clics':<10} {'Clasificación'}")
    print("-" * 50)

    conteo = {"Alto": 0, "Medio": 0, "Bajo": 0}

    for sesion in sesiones:
        id_cliente, duracion, clics = sesion
        nivel = clasificar_sesion(duracion, clics)
        conteo[nivel] += 1
        print(f"{id_cliente:<14} {duracion:<15} {clics:<10} {nivel}")

    print("RESUMEN")
    for nivel, cantidad in conteo.items():
        print("-" * 50)
        print(f"{nivel:<10}: {cantidad} sesión")


if __name__ == "__main__":
    generar_informe(sesiones)