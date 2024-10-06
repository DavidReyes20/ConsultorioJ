from pydantic import BaseModel

class Usuario(BaseModel):
    documento: int
    nombre: str
    apellido: str
    correo: str
    password: str
    rol: str


class Login(BaseModel):
    documento: int
    password: str


class RecursosLegales(BaseModel):
    id_documento: int
    nombre_recurso: str
    descripcion: str
    tipo: str

