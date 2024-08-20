from appv1.routers import user,rol,login
from appv1.schemas.user import UserCreate
from fastapi import FastAPI
from db.database import test_db_connection

app = FastAPI()
#Inclur Router

#arias@gmail.com cortez@gmail.com 12345
#12345

app.include_router(rol.router,prefix="/rol", tags=["insert"])

app.include_router(user.router,prefix="/users", tags=["insert"])

app.include_router(login.router , prefix="/access",tags=["access"])

@app. on_event("startup")
def on_startup():
    test_db_connection()

@app.get("/")
def read_root():
    return {
        "Message": "ADSO 2670586",
        "Autor": "Aricaz Christian "
    }

##pepepasds
##sasd

#Tarea 
#Si esta actualizando se a si mismo que lo deje, permitir al usuario actualizar sus propios datos,
#NO dejar que otro usuario actulice los datos de otro usuario
#Proteger usuarios por pagina , 
#Solo cambie el estado a false,desactivar el usuario s