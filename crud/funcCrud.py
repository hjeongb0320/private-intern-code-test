from worker import runTask
from dependency import q
from crud import redisCrud
from datetime import timedelta
import uuid
import random

async def gen_values():
    async_results = []

    for _ in range(50):
        nowUuid = str(uuid.uuid4())
        waitingTime = random.uniform(0, 9.8)
        # waitingTime = random.uniform(0, 1.1)

        result = q.enqueue_in(timedelta(seconds=waitingTime), runTask, nowUuid)
        # result = q.enqueue(runTask, nowUuid, waitingTime, ttl=10)
        async_results.append(result)

    done = False

    # while not done:
    #     done = True
        
    #     for i, x in enumerate(async_results):
    #         result = x.result

    #         if result is None:
    #             done = False

    return async_results

def get_len():
    data = redisCrud.get_len()

    ret = data

    return ret
    
