#Poblar tabla Carrera

import json

from configuracion import Session
from crear_base_entidades import Facultad, Carrera

session = Session()

with open(
    "data/datos_universidad/datos/carreras.json",
    encoding="utf-8"
) as archivo:

    datos = json.load(archivo)

    for fila in datos:

        facultad = session.query(Facultad).filter_by(
            nombre=fila["facultad"]
        ).first()

        if facultad is not None:

            carrera = session.query(Carrera).filter_by(
                nombre=fila["nombre"]
            ).first()

            if carrera is None:

                carrera = Carrera(
                    id=fila["id"],
                    nombre=fila["nombre"],
                    codigo=fila["codigo"],
                    facultad=facultad
                )

                session.add(carrera)

session.commit()
session.close()

print("Carreras agregadas correctamente")