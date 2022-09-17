#!/usr/bin/python3
"""base_model module."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialise attributes of BaseModel object."""
        if kwargs is not None and len(kwargs):
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    dt = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    kwargs[key] = dt

                self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel object."""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict