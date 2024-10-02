from pydantic import BaseModel


class Usuario(BaseModel):
    documento:int 
    nombre:str
    apellido:str
    correo:str
    
class UsuarioC(BaseModel):
    documento:int
    nombre_usuario:str
    password:str
    rol:str

class Login(BaseModel):
   nombre_usuario:str
   password:str 

class RecursosLegales(BaseModel):
    id_documento: int
    nombre_recurso: str
    descripcion: str
    tipo: str
