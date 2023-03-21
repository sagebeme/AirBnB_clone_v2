#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
