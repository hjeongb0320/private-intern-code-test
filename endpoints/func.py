from fastapi import APIRouter
from crud import funcCrud, redisCrud
from response import ResponseRedisDataList, ResponseCount

router = APIRouter()

@router.post('')
async def gen_values():
    """uuid v4를 key로, 생성 시간을 value로 가지는 객체를 10초동안 랜덤 시간 간격으로 50개 생성해서 redis에 삽입하는 함수"""

    await funcCrud.gen_values()

    return None

@router.delete('/random', response_model=ResponseCount)
def delete_random_values():
    """redis에 저장된 객체를 0~10개 사이로 랜덤하게 삭제하는 함수"""

    data = funcCrud.delete_random_values()
    ret = {"count": data}
    
    return ret

@router.get('/total', response_model=ResponseCount)
def get_total():
    """redis에 저장된 객체가 몇 개인지 리턴하는 함수"""

    data = redisCrud.get_len()
    ret = {"count": data}

    return ret
    

@router.get('', response_model=ResponseRedisDataList)
def get_values(count: int):
    """redis에 저장된 객체를 입력한 값 수 만큼 리턴하는 함수"""

    data = redisCrud.get_values(count)
    ret = {"data": data}

    return ret