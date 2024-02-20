from datetime import datetime

from pydantic import BaseModel

class Token(BaseModel):
	id: int
	token: str
	data: datetime