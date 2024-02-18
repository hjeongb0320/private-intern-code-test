from crud import redisCrud
from datetime import datetime
import asyncio
import time

def runTask(uuid: str):
    # time.sleep(waitingTime)

    value = datetime.today().isoformat()
    
    ret = redisCrud.set_value(uuid, value)

    return ret
