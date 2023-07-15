#!/usr/bin/python3
""" the base model """
import uuid
from datetime import datetime

class BaseModel:
    """ Defines all common attributes and methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializes an instance """
        if kwargs:
            kwargs.pop('__class__', None)
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """ returns a formatted string that includes the class name, the instance ID, and the dictionary representation of the instance's attributes. """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Save updates made to an instance calls the save() method of the storage object to reflect the changes. """
        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of all instances """
        return {
            **self.__dict__,
            '__class__': type(self).__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
