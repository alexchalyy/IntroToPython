'''   

      This is a circle class.

      Written by Alex Chalyy on 5/20/2022.

'''

from Point import Point

class Circle:

#----------------------------------------------------------------------------------

    def __init__(self, radius, point): 

    # init method or constructor

        self._radius = radius
        self._point = point

#----------------------------------------------------------------------------------

    def __repr__(self):

    #   This is repr method of point.

        rep = self._point.__repr__() + '. ' + ' Circle has radius of ' + str(self._radius) + '.'

        return rep

#----------------------------------------------------------------------------------

    def move(self, x, y):

    #   This method sets new center of a circle.

        self._point.move(x, y)

#----------------------------------------------------------------------------------

if __name__ == '__main__':
    circle = Circle(1, Point(0, 0))
    print(repr(circle))
    circle.move(1, 1)
    print(repr(circle))
