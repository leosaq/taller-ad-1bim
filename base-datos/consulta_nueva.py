from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Facultad específica
nombre_facultad = "Facultad de Ingeniería"

recursos = session.query(RecursoAcademico).join(Profesor).join(Carrera).join(Facultad).filter(
    Facultad.nombre == nombre_facultad
).all()

print("RECURSOS ACADÉMICOS DE LA %s" % nombre_facultad)

for r in recursos:
    print("Título: %s" % r.titulo)
    print("Tipo: %s" % r.tipo)
    print("Fecha publicación: %s" % r.fecha_publicacion)
    print("Profesor: %s" % r.profesor.nombre)
    print("Carrera: %s" % r.profesor.carrera.nombre)
    print("----------")

session.close()