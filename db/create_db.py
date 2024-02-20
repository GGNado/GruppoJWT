from db.database import Base, engine
from models.UtenteModel import UtenteModel
from models.TokenModel import TokenModel
Base.metadata.create_all(engine)