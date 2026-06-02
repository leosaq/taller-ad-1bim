from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Profesor
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Filtrar profesores cuya especialidad sea Inteligencia Artificial
profesores = session.query(Profesor).filter(
    Profesor.especialidad == "Inteligencia Artificial"
).all()

print("PROFESORES DE INTELIGENCIA ARTIFICIAL")

for p in profesores:
    print("Nombre: %s" % p.nombre)
    print("Correo: %s" % p.correo)
    print("Especialidad: %s" % p.especialidad)
    print("Carrera: %s" % p.carrera.nombre)
    print("----------")

session.close()