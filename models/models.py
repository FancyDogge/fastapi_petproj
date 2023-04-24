from sqlalchemy import MetaData, Integer, String, Boolean, Column, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    role_id = Column(Integer, ForeignKey('role.id'))
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

# Второй метод создания таблицы в бд
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