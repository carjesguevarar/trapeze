inter = []


def f(x):
    """
    Dado un punto 'x', evalua la función.
    :param x: Punto a evaluar.
    :return: Valor numérico de la función en el punto dado.
    """
    return x/((x + 1)*(x + 2))


def divinter(a, b, n):
    """
    Dado el límite inferior y superior de un intervalo divide este en 'n' segmentos iguales.
    :param a: Límite inferior.
    :param b: Límite superior.
    :param n: Cantidad de segmentos.
    :return: None.
    """
    ha = h(a, b, n)
    inter.append(a)
    for i in range(n):
        inter.append(inter[len(inter) - 1] + ha)


def h(a, b, n):
    """
    Dado los valores de 'a', 'b' y 'n', evalua la función 'h'.
    :param a: Límite inferior.
    :param b: Límite superior
    :param n: Cantidad de sub-intervalor.
    :return: Diferencia de el superior al inferior dividido entre dos.
    """
    return (b - a)/n


def trapezesimple(a, b):
    """
    Método del Trapesio simple.
    :param a: Límite inferior.
    :param b: Límite superior
    :return: Valor de la aproximación de la integral.
    """
    return (h(a, b, 2))*(f(a) + f(b))


def trapezecompound(a, b, n):
    """
    Método de los Trapesoides compuesto.
    :param a: Límite inferior.
    :param b: Límite superior
    :param n: Cantidad de subintervalor.
    :return: Valor de la aproximación de la integral.
    """
    divinter(a, b, n)
    p = 0
    for i in range(1, n):
        p = p + f(inter[i])
    return (h(a, b, n)/2)*(f(a) + 2*p + f(b))
