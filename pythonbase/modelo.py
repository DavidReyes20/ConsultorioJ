from sqlalchemy import String, Integer, Column, ForeignKey
from conexion import base

class Registro(base):
    __tablename__ = "usuarios"
    
    documento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(60), unique=True)
    password = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False)



class RecursoLegales(base):
    __tablename__ = "recursos_legales"

    id_documento = Column(Integer, primary_key=True, index=True)
    nombre_recurso = Column(String(60), nullable=False)
    descripcion = Column(String(100), nullable=True)
    tipo = Column(String(20), nullable=True)


class GestionCasos(base):
    __tablename__ = "gestion_casos"
    
    numero_caso = Column(String(40), primary_key=True)
    nombre_usuario = Column(String(60), nullable=False)
    apellido_usuario = Column(String(60), nullable=False)
    documento_usuario = Column(String(60), nullable=False)
    tipo_caso = Column(String(60), nullable=False)
    estado_caso = Column(String(60), nullable=False)
    link_carpeta = Column(String(60), nullable=False)
    
    id_persona_abre_caso = Column(Integer, ForeignKey('usuarios.documento'), primary_key=True)
    
    