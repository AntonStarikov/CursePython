class NonPositiveDigitException(ValueError)
    pass
class Square:
    def __init__(self, a):
        if a<0:
            raise NonPositiveDigitException('Стороноа квадрата не может быть меньше 0!')

