#Poblar tabla Recursos_Academico

import json

from configuracion import Session
from crear_base_entidades import Profesor, RecursoAcademico

session = Session()

with open(
    "data/datos_universidad/datos/recursos_academicos.json",
    encoding="utf-8"
) as archivo:

    datos = json.load(archivo)

    for fila in datos:

        profesor = session.query(Profesor).filter_by(
            nombre=fila["profesor"]
        ).first()

        if profesor is not None:

            recurso = session.query(RecursoAcademico).filter_by(
                titulo=fila["titulo"]
            ).first()

            if recurso is None:

                recurso = RecursoAcademico(
                    id=fila["id"],
                    titulo=fila["titulo"],
                    tipo=fila["tipo"],
                    fecha_publicacion=fila["fecha_publicacion"],
                    url=fila["url"],
                    profesor=profesor
                )

                session.add(recurso)

session.commit()
session.close()

print("Recursos académicos agregados correctamente")