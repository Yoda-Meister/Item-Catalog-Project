#!/usr/bin/env python3
# Module to set up database.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Component(Base):

    __tablename__ = "component"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }


class Part(Base):

    __tablename__ = "part"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    component_id = Column(Integer, ForeignKey('component.id'))
    component = relationship(Component)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'id': self.id,
            'name': self.name,
            'component_id': self.component_id,
            'description': self.description,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///pcpart.db')
Base.metadata.create_all(engine)
