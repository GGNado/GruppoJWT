import datetime

from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class TokenModel(Base):
	__tablename__ = 'Tokens'
	id = Column(Integer, primary_key = True, autoincrement=True)
	token = Column(String(255), nullable = False)
	data = Column(DateTime, nullable= False, default=datetime.datetime.now())