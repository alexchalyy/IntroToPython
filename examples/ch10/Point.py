'''

This is a Point class (represents point at the center of a circle).

Written by Alex Chalyy on 5/20/2022.

'''

class Point:

#----------------------------------------------------------------------------------

    def __init__(self, x, y): 

    # init method or constructor

        self._x = x
        self._y = y

#----------------------------------------------------------------------------------

    def __repr__(self):

    #   This is repr method of point.

        rep = 'Circle has center with x-coordinate of ' + str(self._x) + ' and y-coordinate of ' + str(self._y)

        return rep

#----------------------------------------------------------------------------------

    def get_x(self):

    #   This is getter method for x-coordinate.

        return self._x

#----------------------------------------------------------------------------------

    def get_y(self):

    #   This is getter method for y-coordinate.

        return self._y

#----------------------------------------------------------------------------------

    def set_x(self, x):

    #   This is getter method for x-coordinate.

        self._x = x

#----------------------------------------------------------------------------------

    def set_y(self, y):

    #   This is getter method for y-coordinate.

        self._y = y          

#----------------------------------------------------------------------------------

    def move(self, x, y):

    #   This method sets new center of a circle.

        self._x = x
        self._y = y