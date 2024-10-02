from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from conexion import crear,get_db
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

@app.post("/alter-table")
async def alter_table(db:Session=Depends(get_db)):
    try:
        alteraT = text("ALTER TABLE usuariosL MODIFY password VARCHAR(60)")
        db.execute(alteraT)
        db.commit()
        return{"men":"tabla ok"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))