#!/usr/bin/python3
""" Review module """
from .base_model import BaseModel


class Review(BaseModel):
    """ generates reviewer objects """
    user_id = ""
    place_id = ""
    text = ""
