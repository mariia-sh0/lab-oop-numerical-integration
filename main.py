"""Головний модуль запуску чисельного інтегрування."""

import math

from integrators import (
    RectangleIntegrator,
    SimpsonIntegrator,
    TrapezoidIntegrator,
)


def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    if abs(x)<=10**-8:
        return -0.5
    return (math.cos(x) - 1)/(x**2)


def main():
    """Точка входу програми."""
    integrators = [
        RectangleIntegrator(target_function, 0.0, 1.0),
        TrapezoidIntegrator(target_function, 0.0, 1.0),
        SimpsonIntegrator(target_function, 0.0, 1.0),]
    for integrator in integrators:
        res, n_min, delta = integrator.adaptive_integrate(1e-4)
        print(f"{integrator}:")
        print(f"  Результат = {res:.7f}, n_min = {n_min}, похибка = {delta:.2e}")


if __name__ == "__main__":
    main()
