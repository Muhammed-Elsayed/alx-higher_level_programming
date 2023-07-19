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
