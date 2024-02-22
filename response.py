from pydantic import BaseModel, Field
from typing import Dict

class ResponseRedisDataList(BaseModel):
    data: Dict[str, str] = Field(..., description="Key-value pairs from Redis")

class ResponseCount(BaseModel):
    count: int