from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from crear_base_entidades import Profesor, Carrera
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Profesores que cumplan dos condiciones al mismo tiempo:
# Que pertenezcan a una carrera específica.
# Que tengan una especialidad específica.

profesores = session.query(Profesor).join(Carrera).filter(
    and_(
        Carrera.nombre == "Ingeniería en Software",
        Profesor.especialidad == "Inteligencia Artificial"
    )
).all()

print("PROFESORES DE INGENIERÍA EN SOFTWARE E INTELIGENCIA ARTIFICIAL")

for p in profesores:
    print("Nombre: %s" % p.nombre)
    print("Correo: %s" % p.correo)
    print("Especialidad: %s" % p.especialidad)
    print("Carrera: %s" % p.carrera.nombre)
    print("----------")

session.close()