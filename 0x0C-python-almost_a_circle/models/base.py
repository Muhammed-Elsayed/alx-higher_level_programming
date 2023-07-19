#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv


class Base:
    """Base class that everyother class inheret from it """
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saving a json format to a file after converting the object"""

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                json_data = cls.to_json_string(obj_dicts)
                file.write(json_data)
