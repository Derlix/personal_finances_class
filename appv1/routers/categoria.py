from typing import List
from appv1.crud.categoria import create_category_sql, get_all_category, get_category_by_name
from appv1.schemas.categoria import CategoryCreate, CategoryResponse
from fastapi import APIRouter,Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
async def insert_category(category: CategoryCreate, db: Session = Depends(get_db)):
    respuesta = create_category_sql(db, category)
    if respuesta:
        return {"mensaje":"Categoria registrada con exito"}
    
@router.get("/get-category-by-name/", response_model=CategoryResponse)
async def read_category_by_name(name: str, db: Session = Depends(get_db)):
    categoria = get_category_by_name(db,name)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    
    return categoria

@router.get("/get-all/", response_model=List[CategoryResponse])
async def read_all_category(db:Session = Depends(get_db)):
    categorias = get_all_category(db)
    if len(categorias) == 0:
        raise HTTPException(status_code=404, detail="Nada para mostrar")
    
    return categorias