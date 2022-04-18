class Complex:
    real = 0
    img = 0

    def __init__(self, r=0, i=0):
        self.real = r
        self.img = i

    def __str__(self):
        if self.img:
            if self.img == 1:
                img = ''
            elif self.img == -1:
                img = '-'
            else:
                img = str(self.img)
            if self.real:
                res = f"{self.real}"
                if self.img > 0:
                    return res + f"+{img}i"
                else:
                    return res + f"{img}i"
            else:
                return f"{img}i"
        else:
            return f"{self.real}"

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)


print(Complex())
print(Complex(1))
print(Complex(-1))
print(Complex(0, 1))
print(Complex(0, -1))
print(Complex(0.5, 0.5))
print(Complex(1, 1) + Complex(5, -5))
print(Complex(1, 1) * Complex(5, 5))
