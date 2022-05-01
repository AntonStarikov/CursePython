class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.heidht = height

    def getWidth(self):
        return self.width

    def getHeidht(self):
        return self.heidht

    # Метод расчитывающий площадь
    def getArea(self):
        return self.width * self.heidht
