from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from db.database import SessionLocal
from entity.Utente import Utente
from models.UtenteModel import UtenteModel
from models.TokenModel import TokenModel

router = APIRouter(
	tags=['Login'],
	prefix='/api/v1.0/gruppoMassa/login'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)

import time
import jwt
from jwt import PyJWTError

SECRET = b'f9c194151872cdf2e88831377e40d3d5bdc91773dd1c640b'
ALGORITHM = 'HS256'

oauth2 = OAuth2PasswordBearer(tokenUrl="token")
def signJWT(id: int, username: str):
	payload = {
		'id': id,
		'username': username,
		'expires': time.time() + 600
	}
	token = jwt.encode(payload, SECRET, algorithm = ALGORITHM)
	print(token)
	return token

def decodeJWT(token: str):
	try:
		payload = jwt.decode(token, SECRET, algorithms = [ALGORITHM])
		return payload if time.time() <= payload['expires'] else None
	except:
		return {}



def verify(token: str = Depends(oauth2)) -> str:
	try:
		payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
		return token
	except PyJWTError:
		raise HTTPException(status_code=404, detail="Token non valido")


session = SessionLocal()

@router.post("/")
async def tentatoLogin(utente: Utente):
	user = session.query(UtenteModel).filter_by(username = utente.username, secret = utente.secret).first()
	if user:
		tk = signJWT(user.id, user.username)
		session.add(TokenModel(token=tk))
		session.commit()
		return tk

	raise HTTPException(detail="Errore", status_code=404)


@router.get("/controllo")
async def controllo(token: str = Depends(verify)):
	return {"message": "Na-MO"}






