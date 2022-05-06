class NonPositiveDigitException(ValueError):
    pass
class Square:
    def __init__(self, a):
        self.a = a
        if a<=0:
            raise NonPositiveDigitException('Стороноа квадрата не может быть меньше или равно 0!')
    def get_area(self):
        return self.a**2
p_sqvare = Square(0)
print(p_sqvare.get_area())