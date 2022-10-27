#!/usr/bin/python3
"""defines FileStorage class"""


import json
import uuid


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances:
    
    Args:
        file_path (str): path to the JSON file
        objects (dictionary): stores all objects
    """
    
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """returns the dictionary objects"""
        return self.__objects
    
    
    def new(self, obj):
        """serializes objects in the obj with key <obj class name>.id"""
        _id = obj.id
        store = self.__class__.__name__ + "." + _id
        self.__objects[store] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dump = json.dumps(self.__objects)
        with open(self.__file_path, "a") as file:
            file.write(dump)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                load = json.load(self.__file_path)
                return load
        except IOError:
            pass
        
    
