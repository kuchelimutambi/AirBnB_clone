#!/usr/bin/python3
""" City module """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class inheriting from basemodel """
    state_id = ""
    name = ""
