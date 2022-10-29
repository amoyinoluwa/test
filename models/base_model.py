#!/usr/bin/python3
""" Module base_model
Contains BaseModel class
"""

import uuid
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Represent a class BaseModel that defines
    all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value,time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, time_format)
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)
        else:
            """Initializes the unique id for each BaseModel"""    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
    def __str__(self):
        """prints model"""
        s = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return s
    
    def save(self):
        """updates the public instance attribute `updated_at with 
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        class_dict = {
            "name": getattr(self, "name"),
            "my_number": getattr(self, "my_number"),
            "id": self.id,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        return class_dict 
