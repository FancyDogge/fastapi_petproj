from sqlalchemy import MetaData, Integer, String, Table, Column, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    role_id = Column(Integer, ForeignKey('roles.id'))

# users = Table(
#     'users',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('username', String, nullable=False),
#     Column('email', String, nullable=False),
#     Column('password', String, nullable=False),
#     Column('created_at', TIMESTAMP, default=datetime.utcnow()),
#     Column('role_id', Integer, ForeignKey('roles.id')),
# )