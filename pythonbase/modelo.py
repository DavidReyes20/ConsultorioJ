from sqlalchemy import String,Integer,Column,ForeignKey
from conexion import base
from sqlalchemy.orm import relationship


class Registro(base):
    __tablename__="usuarios"
    documento=Column(Integer,primary_key=True,index=True)
    nombre=Column(String(50),nullable=False)
    apellido=Column(String(50),nullable=False)
    correo=Column(String(60),unique=True)

class RegistroUsuario(base):
    __tablename__="usuariosL"

    documento=Column(Integer,ForeignKey('usuarios.documento'),primary_key=True ,index=True)

    nombre_usuario=Column(String(50),nullable=False)
    password=Column(String(100),nullable=False)
    rol=Column(String(20),nullable=False )


class RecursoLegales(base):
    __tablename__ = "recursos_legales"

    id_documento = Column(Integer, primary_key=True, index=True)
    nombre_recurso = Column(String(60), nullable=False)
    descripcion = Column(String(100), nullable=True)
    tipo = Column(String(20), nullable=True)
    




    