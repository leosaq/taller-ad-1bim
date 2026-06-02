from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Carrera
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Ordenar carreras por nombre alfabéticamente
carreras = session.query(Carrera).order_by(
    Carrera.nombre
).all()

print("CARRERAS ORDENADAS")

for c in carreras:
    print("Carrera: %s" % c.nombre)
    print("Código: %s" % c.codigo)
    print("Facultad: %s" % c.facultad.nombre)
    print("----------")

session.close()