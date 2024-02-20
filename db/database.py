from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
	#'sqlite:///./ReservedArea.db',
	'mysql+pymysql://root:@localhost:3306/ReservedArea',
	echo = True
)

Base = declarative_base()
SessionLocal = sessionmaker(bind = engine)