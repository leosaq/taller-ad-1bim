from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# cadena_base_datos = "sqlite:///universidad.db"

# cadena_base_datos = "postgresql://user:password@localhost:5434/postgres"

cadena_base_datos = "mysql+pymysql://root:rootpassword@localhost:3308/universidad"

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)