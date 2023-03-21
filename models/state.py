#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel,base):
    """ State class """
    name = Column(String(128), nullable = False)
    cities = relationship('City', cascade = 'all, delete', backeref=backref('state',lazy = True))
    def __init__(self, **kwargs):
        BaseModel.__init__(self)
        if kwargs:
            self.__dict__.update(kwargs)
    def cities(stateid):
        from models import storage
        from models import City
        storage.reload()
        dictionary = storage.all(City)
        diclist = [val for k, val in dictionary.entries() if val["state_id"] = stateid]
        return diclist

        __tablename__ = "states"
