#класс точка координат
class Point:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Сравнение двух точек
    def __eq__(self, point):
        if(self.x == point.x and self.y == point.y):
            return True
        else:
            return False

    #печать точки
    def __repr__(self):
        return f"({self.x}, {self.y})"    

#класс прямоугольник, состоящий из точек
class Rectangle: 
    #создание прямоугольника по двум точкам
    def __init__(self, pointA, pointB):
        self.lCoordinate = []
        
        for i in range(int(pointA.x), int(pointB.x)+1):
            lLine = []
            for j in range(int(pointA.y), int(pointB.y)+1):
                lLine.append(Point(i, j))
            self.lCoordinate.append(lLine)
            lLine.clear
    
    #печать прямоугольника
    def __str__(self):
        for i in self.lCoordinate:
            print(i)
        return ""

    def perimeter(self):
        return str(2*(len(self.lCoordinate) + len(self.lCoordinate[0])))

    def square(self):
        return str(len(self.lCoordinate) * len(self.lCoordinate[0]))

    #проверка - содержит ли прямоугольник точку
    def isContainsPoint(self, point):
        for i in self.lCoordinate:
            for j in i:
                if j == point:
                    return True
    
    #проверка на пересечение прямоугольников
    def isIntersection(self, rectangle):
        for i in self.lCoordinate:
            for j in i:
                if rectangle.isContainsPoint(j):
                    return True
        


#создали 1й прямоугольник
rectangle_1 = Rectangle(Point(2,3), Point(3,5))
print(rectangle_1)
print("perimeter = " + rectangle_1.perimeter())
print("square = " + rectangle_1.square())

#создали 2й прямоугольник
rectangle_2 = Rectangle(Point(1,1), Point(4,4))
print(rectangle_2)
#проверили пересечение
if rectangle_1.isIntersection(rectangle_2):
    print("rectangle_1 isIntersection rectangle_2")
