#Poblar tabla Facultad

import json

from configuracion import Session
from crear_base_entidades import Facultad

session = Session()

with open(
    "data/datos_universidad/datos/facultades.json",
    encoding="utf-8"
) as archivo:

    datos = json.load(archivo)

    for fila in datos:

        facultad = session.query(Facultad).filter_by(
            nombre=fila["nombre"]
        ).first()

        if facultad is None:

            facultad = Facultad(
                id=fila["id"],
                nombre=fila["nombre"],
                ubicacion=fila["ubicacion"],
                decano=fila["decano"]
            )

            session.add(facultad)

session.commit()
session.close()

print("Facultades agregadas correctamente")