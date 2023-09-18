from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    capital = Column(String)
    currency = Column(String)
    population = Column(Integer)
    flag = Column(String)
    languages = relationship('Language', secondary='country_languages', backref='countries')
    currencies = relationship('Currency', secondary='country_currencies', backref='countries')
    continent_id = Column(Integer, ForeignKey('continents.id'))

class CountryLanguage(Base):
    __tablename__ = 'country_languages'
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
    language_id = Column(Integer, ForeignKey('languages.id'), primary_key=True)

class CountryCurrency(Base):
    __tablename__ = 'country_currencies'
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
    currency_id = Column(Integer, ForeignKey('currencies.id'), primary_key=True)

class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    name = Column(String)

class Continent(Base):
    __tablename__ = 'continents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    