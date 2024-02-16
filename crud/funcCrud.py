from worker import runTask
from datetime import datetime
from dependency import q
import time
import uuid

async def gen_value():
    async_results = []

    for _ in range(50):
        nowUuid = str(uuid.uuid4())
        value = datetime.today().isoformat()
        result = q.enqueue(runTask, nowUuid, value, ttl=10)
        async_results.append(result)

    start_time = time.time()
    print(f'start_time: {start_time}')
    
    end_time = time.time()
    print(f'end_time: {end_time}')

    return async_results
