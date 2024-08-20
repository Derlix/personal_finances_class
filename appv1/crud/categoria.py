from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.categoria import CategoryCreate
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_category_sql(db:Session, Category: CategoryCreate):
    try:
        sql_query = text(
            "INSERT INTO category (category_name, category_description, category_status) "
            "VALUES (:category_name, :category_description, :category_status)"
        )
        params = {
            "category_name": Category.category_name,
            "category_description": Category.category_description,
            "category_status": True
        }
        db.execute(sql_query, params)
        db.commit()
        return True
    
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear la categoria: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID generado ya existe, vuelva a intentarlo")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
        
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear la categoria: {e}")
        raise HTTPException(status_code=500, detail="Error. Error al crear la categoria")
    
    
    
#Obtener categoria por nombre
def get_category_by_name(db: Session, name: str):
    try:
        sql = text("SELECT * FROM category WHERE category_name = :category_name")
        result = db.execute(sql, {"category_name": name}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar la categoria por nombre: {e}")
        raise HTTPException(status_code=500, detail="Error. Error al buscar la categoria por nombre")
    
#Obtener categorias
def get_all_category(db: Session):
    try:
        sql = text("SELECT * FROM category")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener las categorias: {e}")
        raise HTTPException(status_code=500, detail="Error. Error al obtener las categorias")