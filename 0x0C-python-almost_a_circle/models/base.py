#!/usr/bin/python3
"""
Module documentation : base class to all other classes which handle id attribute
"""

class Base:
    """
    a class with private attribute __nb_objects with an increament 
    algorithm if id is None
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """
        initialiez id attribute and assigns to self else increment to __nb_object atrribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
