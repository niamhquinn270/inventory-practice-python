import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return(f"The area of the circle is {self.area():.2f} and "
                f"Rhe circumference od the circle is {self.circumference():.2f}")





    def area(self):
        return (self.radius*self.radius)*math.pi


    def circumference(self):
        self.circumference = (self.radius*2)*math.pi

