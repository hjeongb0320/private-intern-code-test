from fastapi import FastAPI
from pydantic import BaseModel
from endpoints import test, func

app = FastAPI()

app.include_router(test.router, prefix="/test", tags = ["test"])
app.include_router(func.router, prefix="/func", tags = ["func"])
  