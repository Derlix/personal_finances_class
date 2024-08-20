from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.rol import RolCreate
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from fastapi import HTTPException
# Crear un rol
def create_rol_sql(db: Session, rol:RolCreate):
    sql_query = text(
        "INSERT INTO roles (rol_name) "
        "VALUES (:rol_name)"
    )
    params = {
        "rol_name":rol.rol_name
    }
    db.execute(sql_query, params)
    db.commit()
    return True  # Retorna True si la inserción fue exitosa


def get_rol_by_rolname(db: Session, rol: str):
    try:
        sql = text("SELECT * FROM roles WHERE rol_name = :rol_name")
        result = db.execute(sql, {"rol_name": rol}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar rol por el nombre: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar rol por el nombre")


def get_all_roles(db: Session):
    try:
        sql = text("SELECT * FROM roles")
        result = db.execute(sql).fetchall()
        return result

    except SQLAlchemyError as e:
        print(f"Error al buscar los roles: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar roles")
        