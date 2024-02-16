from fastapi import FastAPI
from pydantic import BaseModel
import test

from worker import runTask

app = FastAPI()

app.include_router(test.router, prefix="/test", tags = ["test"])
    
