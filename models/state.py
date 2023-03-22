#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, base):
    """ State class """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable = False)
    cities = relationship('City', cascade = 'all, delete')
    def __init__(self, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
        from models import storage
        storage.new(self)

    @property
    def cities(self):
        from models import storage
        from models import City
        storage.reload()
        dictionary = storage.all(City)
        diclist = [val for k, val in dictionary.entries() if val["state_id"] == self.state__id]
        return diclist
