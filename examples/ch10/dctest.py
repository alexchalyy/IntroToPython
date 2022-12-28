'''

Create a script containing the following maximum function:

def maximum(value1, value2, value3):

    """Return the maximum of three values."""

    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3

    return max_value

Modify the function’s docstring to define tests for calling function maximum with three ints, three floats and three strings. For each 
type, provide three tests—one with the largest value as the first argument, one with the largest value as the second argument, one with 
the largest value as the third argument. Use doctest to run your tests and confirm that all execute correctly. Next, modify the maximum
function.

Written by Alex Chalyy on 5/19/2022.

'''

class Maximum():

#-------------------------------------------------------------------------------------

    def maximum(self, value1, value2, value3):

        """Return the maximum of three values."""

        max_value = value1
        if value2 > max_value:
            max_value = value2
        if value3 > max_value:
            max_value = value3

        return max_value

#-------------------------------------------------------------------------------------

    def __init__(self):

        """ This is contructor method.

        >>> m = Maximum()
        >>> print(m.maximum(1, 2, 3))
        3
        >>> print(m.maximum(1, 3, 2))
        3
        >>> print(m.maximum(3, 1, 2))
        3
        >>> print(m.maximum(1.1, 1.2, 1.3))
        1.3
        >>> print(m.maximum(1.1, 1.3, 1.2))
        1.3
        >>> print(m.maximum(1.3, 1.1, 1.2))
        1.3
        >>> print(m.maximum('hi', 'bye', 'hello'))
        'hell'
        """

        #print("one")
        #c = self.maximum(1, 2, 3)
        #print("two")

        '''
        print(f"self.maximum(1, 2, 3) = {self.maximum(1, 2, 3)}")
        print(f"self.maximum(1, 3, 2) = {self.maximum(1, 3, 2)}")
        print(f"self.maximum(3, 1, 2) = {self.maximum(3, 1, 2)}")

        print(f"self.maximum(1.1, 1.2, 1.3) = {self.maximum(1.1, 1.2, 1.3)}")
        print(f"self.maximum(1.1, 1.3, 1.2) = {self.maximum(1.1, 1.3, 1.2)}")
        print(f"self.maximum(1.3, 1.1, 1.2) = {self.maximum(1.3, 1.1, 1.2)}")

        print(f"self.maximum('hi', 'hello', 'bye') = {self.maximum('hi', 'hello', 'bye')}")
        print(f"self.maximum('hello', 'hi', 'bye') = {self.maximum('hello', 'hi', 'bye')}")
        print(f"self.maximum('hi', 'bye', 'hello') = {self.maximum('hi', 'bye', 'hello')}")
        '''

#-------------------------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    #m = Maximum()
    doctest.testmod(verbose=True)