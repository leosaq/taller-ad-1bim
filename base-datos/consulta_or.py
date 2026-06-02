from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from crear_base_entidades import RecursoAcademico
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Mostrar los recursos académicos que sean de tipo: Libro o Artículo
recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Libro",
        RecursoAcademico.tipo == "Artículo"
    )
).all()

print("RECURSOS TIPO LIBRO O ARTÍCULO")

for r in recursos:
    print("Título: %s" % r.titulo)
    print("Tipo: %s" % r.tipo)
    print("Profesor: %s" % r.profesor.nombre)
    print("----------")

session.close()