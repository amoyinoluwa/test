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
        with open(self.__file_path, "w") as f:
            json.dump({objName: obj.to_dict() for objName, obj in self.__objects}, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                load = json.load(f)
                for key in load:
                    self.__objects[key] = classes[load[key]["__class__"]](**load[key]) 
        except IOError:
            pass
        
    
