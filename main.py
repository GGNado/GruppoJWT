import uvicorn
import db.create_db
import jinja2
import httptools
from models.UtenteModel import UtenteModel
from fastapi import FastAPI, Request
from db.database import SessionLocal
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.LoginRotte import router as loginRouter

webapp = FastAPI(
	title = 'Auth e JWT',
	decription = 'Web Example: Auth e JWT su MySQL DBMS'
)

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

webapp.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

session = SessionLocal()

@webapp.get('/', response_class = HTMLResponse, tags = ['HomePage'])
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
			'author': 'birg81',
		}
	)

webapp.include_router(loginRouter)

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		use_colors = False,
		http = 'httptools',
		reload = True
	)

