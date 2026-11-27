"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""

    order = 1
    method_name = "Базовий метод"

    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""
        self.validate_bounds(a, b)
        self.func = func
        self.a = a
        self.b = b
        self.calls = 0
        
        


    @classmethod
    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""
        return cls(func, params["a"], params["b"])

    @staticmethod
    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""
        if a >= b:
            raise ValueError("Перевірте коректність меж інтегрування!")
        

    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError

    def adaptive_integrate(self, eps=3e-5, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""
        n = initial_n
        divisor = (2 ** self.order)-1
        I_h = self.integrate(n)
        while True:
            I_h2 = self.integrate(2 * n)
            delta = abs(I_h2-I_h)/divisor
            if delta < eps:
                I_yt = I_h2 + (I_h2-I_h)/divisor
                n_min = 2 * n
                return I_yt, n_min, delta
            n = n * 2
            I_h = I_h2            

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""
        return f"{self.method_name} на відрізку [{self.a}; {self.b}]"
    


class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)

    def integrate(self, n):
        self.calls += 1
        if n <= 0:
            raise ValueError("Кількість розбиттів n має бути додатною")
        h = (self.b - self.a)/n 
        total = 0.0
        for i in range(n):
            x_mid = self.a + (i + 0.5) * h
            total += self.func(x_mid)
        return total * h



class TrapezoidIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою трапецій."""

    order = 2
    method_name = "Формула трапецій"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)

    def integrate(self, n):
        self.calls += 1
        if n <= 0:
            raise ValueError("Кількість розбиттів n має бути додатною")
        h = (self.b - self.a)/n 
        total = 0.5 * (self.func(self.a) + self.func(self.b))
        for i in range(1,n):
            x = self.a + i * h
            total += self.func(x) 
        return total * h


    
class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""

    order = 4
    method_name = "Формула Сімпсона"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)

    def integrate(self, n):
        self.calls += 1
        if n <= 0 or n % 2 != 0:
            raise ValueError("Кількість розбиттів n має бути додатним парним числом")
        
        h = (self.b - self.a)/n 
        total = (self.func(self.a)+ self.func(self.b))
    
        for i in range(1,n):
            x = self.a + i * h
            if i%2 == 1:
                total += 4 * self.func(x)
            else:
                total += 2 * self.func(x)
        return total*(h/3)
            

