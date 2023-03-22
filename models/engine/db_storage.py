#!/urs/bin/python3

import models
from models.amenity import Amenity
from models.base_model import BaseModel, base
from models.city import City
from models.place import Place
from models.place import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
        "Place": Place, "Review": Review,"State": State, "User": User}

Class DBStorage:
    "interactes with the MySQL Database"
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER =getenv(HBNB_MYSQL_USER)
        HBNB_MYSQL_PWD = getenv(HBNB_MYSQL_PWD)
        HBNB_MYSQL_HOST = getenv(HBNB_MYSQL_HOST)
        HBNB_MYSQL_DB = getenv(HBNB_MYSQL_DB)
        HBNB_ENV = getenv(HBNB_ENV)
        self.__engine = create_engine('mysql+mysqldb:{}:{}@{}/{}'.
                format("HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB,
                HBNB_ENV"),pool_pre_ping=True)
        if HBNB_ENV == "test":
            base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current DB session
        """
        new_dict = {}
        for cls in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss].all())
                for obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads data from the database
        """
        base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=false)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (valur.id == id):
                return value
        return None
    def count(self, cls=None):
        """
        count the number of objevts in storage
        """

        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls.values())

        return count
