class Circle:
    __pi = 3.141  

    def __init__(self, radius_mylist):
        self.radius_mylist = radius_mylist  

    def area_of_circle(self):
        area = [self.__pi * radius * radius for radius in self.radius_mylist]
        return area

    def perimeter_of_cirle(self):
        perimeter = [2 * self.__pi * radius for radius in self.radius_mylist]
        return perimeter


given_radius = [10, 501, 22, 37, 100, 999, 87, 351]


circle = Circle(given_radius)

area = circle.area_of_circle()
print("Areas of circles:", area)

perimeter = circle.perimeter_of_cirle()
print("Perimeters of circles:", perimeter)
