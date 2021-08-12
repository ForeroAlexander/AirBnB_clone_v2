#!/usr/bin/python3
""" Place Module for HBNB project """
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref
import os
from sqlalchemy import MetaData, Table

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True))


class Place(BaseModel, Base):
    """This class define a table with various atributtes"""
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, amenity):
            """setter amenities ids to Amenity instances"""
            if self.__class__.__name__ == 'Amenity' and amenity.id\
               not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)

"""if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
getter method place
            _review = []
            for _id, obj in models.storage.all(Review).items():
                if self.id == obj.place_id:
                    _review.append(obj)
            return _review

        @property
        def kamenities(self):
getter method amenities
            _amenities = []
            for _id, obj in models.storage.all(Amenity).items():
                if self.id == obj.place_id:
                    _amenities.append(obj)
            return _amenities

        @amenities.setter
        def amenities(self, value):
setter method
            if type(value) is 'Amenity':
                self.amenity_ids.append(value.id)
"""
