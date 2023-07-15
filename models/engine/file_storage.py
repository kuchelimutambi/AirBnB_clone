#!/usr/bin/python3
""" Serializes instances to a JSON file and deserializes JSON file to instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ an instance method that returns the dictionary __objects, which contains all the stored instances. """
        return FileStorage.__objects

    def new(self, obj):
        """ adds a new instance to the __objects dictionary """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializing the instances in the __objects dictionary to a JSON file """
        objs_dictionary = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w+') as f:
            json.dump(objs_dictionary, f)

    def reload(self):
        """ deserializing instances from the JSON file and reloading them into the __objects dictionary. """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs_dictionary = json.load(f)
                for key, value in objs_dictionary.items():
                    if value.get('__class__') == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value.get('__class__') == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif value.get('__class__') == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif value.get('__class__') == 'City':
                        FileStorage.__objects[key] = City(**value)
                    elif value.get('__class__') == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value.get('__class__') == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif value.get('__class__') == 'Review':
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
