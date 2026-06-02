# Poblar tabla Profesor

import json

from configuracion import Session
from crear_base_entidades import Carrera, Profesor

session = Session()

with open(
    "data/datos_universidad/datos/profesores.json",
    encoding="utf-8"
) as archivo:

    datos = json.load(archivo)

    for fila in datos:

        carrera = session.query(Carrera).filter_by(
            nombre=fila["carrera"]
        ).first()

        if carrera is not None:

            nombre_completo = fila["nombres"] + " " + fila["apellidos"]

            profesor = session.query(Profesor).filter_by(
                nombre=nombre_completo
            ).first()

            if profesor is None:

                profesor = Profesor(
                    id=fila["id"],
                    nombre=nombre_completo,
                    correo=fila["correo"],
                    especialidad=fila["especialidad"],
                    carrera=carrera
                )

                session.add(profesor)

session.commit()
session.close()

print("Profesores agregados correctamente")