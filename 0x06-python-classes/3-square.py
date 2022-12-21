#!/usr/bin/python3

"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    """A simple ``Square`` class
    Attributes:
        size (`int`): The size of the ``Square``.
    """
    def __init__(self, size=0):
        """Constructs a ``Square`` objet
        Args:
            size (`int`): The size of the ``Square``.
                The default value is 0.
        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """Computes the area of the ``Square``.
        Returns:
            int: The area of the ``Square``.
        """
        return self._Square__size ** 2
