from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las facultades
facultades = session.query(Facultad).all()

print("LISTA DE FACULTADES")

for f in facultades:
    print("%s - %s - %s" % (
        f.nombre,
        f.ubicacion,
        f.decano
    ))
    print("----------")