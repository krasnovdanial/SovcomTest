from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey, DateTime, Text, Boolean, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Debtor(Base):
    __tablename__ = "debtors"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    inn = Column(String)
    birth_date = Column(Date)
    birth_place = Column(String)
    region = Column(String)
    city = Column(String)
    street = Column(String)
    building = Column(String)
    apartment = Column(String)


class ObligatoryPayment(Base):
    __tablename__ = "obligatory_payment "
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sum = Column(Numeric)


class Bank(Base):
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bik = Column(String)


class MonetaryObligation(Base):
    __tablename__ = "monetary_obligations"
    id = Column(Integer, primary_key=True)
    debtor_id = Column(Integer, ForeignKey('debtors.id'))
    creditor_name = Column(String)
    total_sum = Column(Numeric)
    debt_sum = Column(Numeric)
    content = Column(String)
    basis = Column(String)


class ExtrajudicialBankruptcyMessage(Base):
    __tablename__ = "extrajudicial_bankruptcy_message"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    type = Column(String)
    publish_date = Column(Date)
