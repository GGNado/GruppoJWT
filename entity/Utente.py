from pydantic import BaseModel

class Utente(BaseModel):
	id: int
	username: str
	secret: str
