from appv1.crud.permissions import get_permissions
from appv1.crud.user import create_user_sql, get_all_users,get_user_by_email, get_user_by_id, update_user,get_all_users_paginated,delete_user
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.user import UserCreate, UserResponse, UserUpdate,PaginatedUsersResponse
from db.database import get_db
from typing import List
from appv1.routers.login import get_current_user


router = APIRouter()
MODULE = 'usuarios'

@router.post("/create")
                #Esquema para recibir datos
async def insert_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.user_role, MODULE)
    if not permisos.p_insert:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    if current_user.user_role != 'SuperAdmin':
        if  user.user_role == 'SuperAdmin':
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    respuesta = create_user_sql(db,user)
    if respuesta:
        return {
            "mensaje":"Usuario Registrado con exito"}

                                        #Esquema para responder datos
@router.get("/get_user_by_email/", response_model=UserResponse)
async def read_user_by_email(
    email:str,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
    ):
    permisos = get_permissions(db, current_user.user_role, MODULE)
    if  current_user.mail != email :
        if not permisos.p_select:
            raise HTTPException(status_code=404, detail="Usuario no autorizado")
    
    usuario = get_user_by_email(db,email)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/get_all/", response_model=List[UserResponse])
async def read_all_users(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
    ):
    permisos = get_permissions(db, current_user.user_role, MODULE)
    if not permisos.p_select:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    usuarios = get_all_users(db)
    if len(usuarios) == 0:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    return usuarios

# Endpoint para actualizar un usuario
@router.put("/update/", response_model=dict)
def update_user_by_id(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):
    verify_user = get_user_by_id(db,user_id)
    if verify_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db_user = update_user(db, user_id, user)
    if db_user:
        return {"mensaje": "registro actualizado con éxito" }

# usuarios paginados
@router.get("/users-by-page/", response_model=PaginatedUsersResponse)
def get_all_users_by_page(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    
    users, total_pages = get_all_users_paginated(db, page, page_size)

    return {
        "users": users,
        "total_pages": total_pages,
        "current_page": page,
        "page_size":page_size
        }


@router.delete("/delete/{user_id}", response_model=dict)
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    result = delete_user(db, user_id)
    if result:
        return {"mensaje": "Usuario eliminado con éxito"}