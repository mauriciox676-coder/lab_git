import math


def area_circulo(radio):
    """Retorna el área de un círculo a partir de su radio."""
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    """Retorna el área de un rectángulo."""
    return base * altura


def area_triangulo(base, altura):
    """Retorna el área de un triángulo."""
    return base * altura / 2


def mostrar_area(figura, area):
    print(f"Área del {figura}: {area:.2f}")


def main():
    mostrar_area("círculo", area_circulo(5))
    mostrar_area("rectángulo", area_rectangulo(4, 6))
    mostrar_area("triángulo", area_triangulo(3, 8))


if __name__ == "__main__":
    main()