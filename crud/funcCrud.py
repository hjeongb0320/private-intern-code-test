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

        result = q.enqueue_in(timedelta(seconds=waitingTime), runTask, nowUuid, result_ttl=0)
        # result = q.enqueue(runTask, nowUuid, waitingTime, ttl=10)
        async_results.append(result)

    # done = False

    # while not done:
    #     done = True
        
    #     for i, x in enumerate(async_results):
    #         result = x.result

    #         if result is None:
    #             done = False

    return async_results

def delete_random_values():
    # 1. 몇개를 지울 것인지 랜덤으로 숫자 하나를 뽑는다
    # 2. 가지고 있는 keys를 모두 가져온다
    # 3. 우선 keys의 개수가 random_number보다 적지는 않은지 체크 -> 적다면 keys 개수만큼 삭제 (해당 함수의 실패를 없애기 위함 (어지간하면 유저의 행위를 막지 않기 위해))
    # 4. 전체 keys 중 랜덤 숫자만큼 랜덤으로 key를 뽑음
    # 5. 랜덤 숫자만큼 for문 돌며 key delete
    # 6. 지운 개수 return

    # 1
    random_number = random.randint(0, 10)

    # 2 3 4 5 6
    data = redisCrud.delete_values(random_number)

    ret = data

    return ret