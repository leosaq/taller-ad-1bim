from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from configuracion import cadena_base_datos

Base = declarative_base()

engine = create_engine(cadena_base_datos)



class Facultad(Base):

    __tablename__ = "facultad"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    ubicacion = Column(String(100))
    decano = Column(String(100))

    carreras = relationship("Carrera", back_populates="facultad")

    def __str__(self):
        return "%s" % (self.nombre)
    
    
class Carrera(Base):

    __tablename__ = "carrera"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    codigo = Column(String(20))

    facultad_id = Column(Integer,
                         ForeignKey("facultad.id"))

    facultad = relationship("Facultad",
                            back_populates="carreras")

    profesores = relationship("Profesor",
                               back_populates="carrera")

    def __str__(self):
        return "%s" % (self.nombre)
    
    

class Profesor(Base):

    __tablename__ = "profesor"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    especialidad = Column(String(100))

    carrera_id = Column(Integer,
                        ForeignKey("carrera.id"))

    carrera = relationship("Carrera",
                           back_populates="profesores")

    recursos = relationship("RecursoAcademico",
                            back_populates="profesor")

    def __str__(self):
        return "%s" % (self.nombre)
    
    
    
    
class RecursoAcademico(Base):

    __tablename__ = "recurso_academico"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150))
    tipo = Column(String(50))
    fecha_publicacion = Column(String(20))
    url = Column(String(200))

    profesor_id = Column(Integer,
                         ForeignKey("profesor.id"))

    profesor = relationship("Profesor",
                            back_populates="recursos")

    def __str__(self):
        return "%s" % (self.titulo)

Base.metadata.create_all(engine)
