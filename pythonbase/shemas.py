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

class GestionCasos(BaseModel):
    numero_caso: str
    nombre_usuario:str
    apellido_usuario:str
    documento_usuario:str
    tipo_caso:str
    estado_caso:str
    link_carpeta:str
    id_persona_abre_caso:int

