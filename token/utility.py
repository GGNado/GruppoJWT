import time
import jwt

SECRET = b'f9c194151872cdf2e88831377e40d3d5bdc91773dd1c640b'
ALGORITHM = 'HS256'

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