from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
import redisController

# from worker import runTask

app = FastAPI()

app.include_router(redisController.router, prefix="/redis", tags = ["redis"])