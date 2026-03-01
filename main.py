from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from items_view import router as items_router
from users.views import router as viev_router
from api_v1 import router as router_v1
from core.config import settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(items_router, tags=['items'])
app.include_router(viev_router, tags=['view'])
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)





@app.get('/')
def hello_index():
    return {
        'message': "Hello index"
    }

@app.get("/hello/")
def hello(name: str = "World!"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)