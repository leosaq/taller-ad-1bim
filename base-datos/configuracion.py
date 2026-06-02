from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cadena_base_datos = "sqlite:///universidad.db"

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)