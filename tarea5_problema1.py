"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación (213022)
Problema 1: Evaluación de nivel de compromiso en sesiones de clientes.
"""


def clasificar_compromiso(duracion_segundos: int, numero_clics: int) -> str:
    """
    Evalúa el nivel de compromiso de una sesión según duración y número de clics.

    Reglas:
    - "Alto": duración > 180 segundos Y clics > 8
    - "Bajo": duración < 60 segundos O clics < 3
    - "Medio": cualquier otro caso
    """
    if duracion_segundos > 180 and numero_clics > 8:
        return "Alto"
    elif duracion_segundos < 60 or numero_clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe_compromiso(sesiones: list[list]) -> None:
    """Recorre la matriz de sesiones e imprime el ID del cliente y su clasificación."""
    print("=== INFORME DE COMPROMISO DE SESIONES ===")
    print(f"{'ID Cliente':<15} | {'Clasificación':<15}")
    print("-" * 33)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15} | {clasificacion:<15}")


def main() -> None:
    # Matriz: [ID del Cliente, Duración (segundos), Número de clics]
    matriz_sesiones = [
        ["CLI-001", 240, 12],  # Alto (>180s y >8 clics)
        ["CLI-002", 45, 5],     # Bajo (<60s)
        ["CLI-003", 120, 2],    # Bajo (<3 clics)
        ["CLI-004", 150, 6],    # Medio
        ["CLI-005", 310, 7],    # Medio (duración alta, pero clics no > 8)
        ["CLI-006", 195, 10],   # Alto
    ]

    generar_informe_compromiso(matriz_sesiones)


if __name__ == "__main__":
    main()