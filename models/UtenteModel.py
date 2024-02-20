from db.database import Base
from sqlalchemy import Column, Integer, String

class UtenteModel(Base):
	__tablename__ = 'Utenti'
	id = Column(Integer, primary_key = True)
	username = Column(String(48), nullable = False)
	secret = Column(String(48), nullable = False)