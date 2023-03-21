#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel,base
from sqlalchemy import Column,String,Integer,ForeignKey

class City(BaseModel, base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60),Foreign_Key("states.id"),nullable = False)
    name = Column(String(128),nullable = False )

    def __init__(self, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)

    __tablename__ = "cities"
