#!/usr/bin/python3
"""
Module documentation : base class to all other
classes which handle id attribute
"""
import json
import csv


class Base:
    """
    a class with private attribute __nb_objects with an increament
    algorithm if id is None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialiez id attribute and assigns to self
        else increment to __nb_object atrribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns [] if empty else JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ return obj to JSON string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        else:
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ make a list of instance attributes """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
                return [cls.create(**inst) for inst in instances]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ list objects to CSV file serialization """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ from CSV file to list objects deserialization """
        filename = cls.__name__ + ".csv"
        inst_list = []
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    inst_list.append(cls.create(**row))
                return inst_list
        except FileNotFoundError:
            return []
