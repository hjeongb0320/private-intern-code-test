from fastapi import APIRouter, HTTPException
from crud import funcCrud

router = APIRouter()

@router.post('')
async def gen_values():
    """uuid v4를 key로, 생성 시간을 value로 가지는 객체를 10초동안 랜덤 시간 간격으로 50개 생성해서 redis에 삽입하는 함수"""

    await funcCrud.gen_values()

    return None

@router.delete('/random')
def delete_random_values():
    """redis에 저장된 객체를 0~10개 사이로 랜덤하게 삭제하는 함수"""

    data = funcCrud.delete_random_values()
    ret = data
    
    return ret

@router.get('/total')
def get_total():
    """redis에 저장된 객체가 몇 개인지 리턴하는 함수"""

    data = funcCrud.get_len()
    ret = data

    return ret
    

@router.get('/{count}')
def get_cnt(count: int):
    """redis에 저장된 객체를 입력한 값 수 만큼 리턴하는 함수"""