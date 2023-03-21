#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, **kwargs):
        BaseModel.__init__(self)
        if kwargs:
            self.__dict__.update(kwargs)
