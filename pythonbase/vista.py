from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from conexion import crear, get_db
from modelo import base, Registro, RecursoLegales
from shemas import Usuario, Login
from shemas import RecursosLegales as recursos
import bcrypt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base.metadata.create_all(bind=crear)

@app.post('/insertar', response_model=Usuario)
async def registrar_cliente(clientemodel: Usuario, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(clientemodel.password.encode('utf-8'), bcrypt.gensalt())
    datos = Registro(**clientemodel.dict())
    datos.password = hashed_password.decode('utf-8')
    db.add(datos)
    db.commit()
    db.refresh(datos)
    return datos


@app.delete("/eliminar/{documento}")
async def eliminar_cliente(documento: int, db: Session = Depends(get_db)):
    datos_cliente = db.query(Registro).filter(Registro.documento == documento).first()

    if datos_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    db.delete(datos_cliente)
    db.commit()
    return {"detail": "Cliente eliminado con éxito"}

@app.get('/consultarCliente', response_model=list[Usuario])
async def Consultar_cliente(db: Session = Depends(get_db)):
    datos_cliente = db.query(Registro).all()
    return datos_cliente


@app.put("/modificar/{documento}", response_model=Usuario)
async def modificar_cliente(documento: int, clientemodel: Usuario, db: Session = Depends(get_db)):
    datos_cliente = db.query(Registro).filter(Registro.documento == documento).first()

    if datos_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Actualiza todos los campos del cliente
    for key, value in clientemodel.dict().items():
        setattr(datos_cliente, key, value)

    try:
        db.commit()  # Guarda los cambios en la base de datos
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))  # Maneja errores de commit

    return datos_cliente  # Retorna los datos del cliente modificado




@app.get('/clientes/{documento}', response_model=Usuario)
async def consultar_cliente(documento: int, db: Session = Depends(get_db)):
    datos_cliente = db.query(Registro).filter(Registro.documento == documento).first()
    if datos_cliente is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return datos_cliente

@app.get("/cliente/documento/", response_model=list[int])
async def getdocumentoCliente(db: Session = Depends(get_db)):
    documento = db.query(Registro.documento).all()
    return [doc[0] for doc in documento]

@app.post("/login")
async def login(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(Registro).filter(Registro.documento == user.documento).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")
    
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return {
        "mensaje": "Inicio de sesión exitoso",
        "nombre": db_user.nombre,
        "rol": db_user.rol
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
    