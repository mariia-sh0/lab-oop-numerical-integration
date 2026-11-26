"""Головний модуль запуску чисельного інтегрування."""

import math

from integrators import (
    RectangleIntegrator,
    SimpsonIntegrator,
    TrapezoidIntegrator,
)


def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    return math.cos(x**2)

def main():
    """Точка входу програми."""
    integrators = [
        RectangleIntegrator(target_function, 0.0, 1.0),
        TrapezoidIntegrator(target_function, 0.0, 1.0),
        SimpsonIntegrator(target_function, 0.0, 1.0),]
    for eps in (3e-6,3e-5):
        print(f"\nДля точності eps={eps} матимемо:\n")    
        for integrator in integrators:
            res, n_min, delta = integrator.adaptive_integrate(eps)
            print(f"{integrator}:")
            print(f"  Результат = {res:.7f}, n_min = {n_min}, похибка = {delta:.2e}")


if __name__ == "__main__":
    main()
