import bcrypt
from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from conexion import crear,get_db
from modelo import base,Registro,RegistroUsuario, RecursoLegales
from shemas import Usuario as cli ,UsuarioC  as usu 
from shemas import RecursosLegales as recursos
from shemas import Login
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
base.metadata.create_all(bind=crear)

@app.post('/insertar',response_model=cli)
async def registrar_cliente(clientemodel:cli, db:Session=Depends(get_db)):
    datos=Registro(**clientemodel.dict())
    db.add(datos)
    db.commit()
    db.refresh(datos)
    return datos

@app.get('/consultarCliente',response_model=list[cli])
async def Consultar_cliente(db:Session=Depends(get_db)):
    datos_cliente=db.query(Registro).all()
    return datos_cliente

@app.get('/clientes/{documento}',response_model=cli)
async def consultar_cliente(documento:int,db:Session=Depends(get_db)):
    datos_cliente=db.query(Registro).filter(Registro.documento == documento).first()

    if datos_cliente is None:
        raise HTTPException(status_code=404,detail="dato no encontrado")
    return datos_cliente

@app.get("/cliente/documento/",response_model=list[int])
async def getdocumentoCliente(db:Session=Depends(get_db)):
    documento=db.query(Registro.documento).all()
    return[doc[0] for doc in documento]


@app.post("/registrousuario")
async def registrar_usuario(user:usu,db:Session=Depends(get_db)):
    nombre_user=db.query(RegistroUsuario).filter(RegistroUsuario.nombre_usuario==user.nombre_usuario).first()
    if nombre_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    encriptacion=bcrypt.hashpw(user.password.encode('utf-8'),bcrypt.gensalt())
    nuevo_user=RegistroUsuario(documento=user.documento,nombre_usuario=user.nombre_usuario,password=encriptacion.decode('utf-8'),rol=user.rol)
    db.add(nuevo_user)
    db.commit()
    db.refresh(nuevo_user)

    return{"documento":nuevo_user.documento,"nombre":nuevo_user.nombre_usuario,"rol":nuevo_user.rol}


@app.post("/login")
async def login(user:Login,db:Session=Depends(get_db)):
    db_user=db.query(RegistroUsuario).filter(RegistroUsuario.nombre_usuario==user.nombre_usuario).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="Usuario no  existe")
    if not bcrypt.checkpw(user.password.encode('utf-8'),db_user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return{
        "mensaje":"Inicio de sesión Ok",
        "nombreUsuario":db_user.nombre_usuario,
        "rol":db_user.rol
    }

@app.post('/insertarRecurso', response_model=recursos)
async def registrar_Recurso(recur: recursos, db: Session = Depends(get_db)):
    datos = RecursoLegales(**recur.dict())
    db.add(datos)
    db.commit()
    db.refresh(datos)
    return datos

    
@app.get('/consultarRecurso',response_model=list[recursos])
async def Consultar_cliente(db:Session=Depends(get_db)):
    datos_cliente=db.query(RecursoLegales).all()
    return datos_cliente


@app.delete('/eliminarRecurso/{id}', response_model=recursos)
async def eliminar_recurso(id: int, db: Session = Depends(get_db)):
    recurso = db.query(RecursoLegales).filter(RecursoLegales.id_documento == id).first()
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    
    db.delete(recurso)
    db.commit()
    return recurso
