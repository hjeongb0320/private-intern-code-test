from fastapi import APIRouter, HTTPException
from crud import funcCrud

router = APIRouter()

@router.post('')
async def gen_value():
    """uuid v4를 key로, 생성 시간을 value로 가지는 객체를 10초동안 랜덤 시간 간격으로 50개 생성해서 redis에 삽입하는 함수"""

    data = await funcCrud.gen_value()
    
    ret = len(data)

    return ret

@router.delete('/random')
def gen_value():
    """redis에 저장된 객체를 0~10개 사이로 랜덤하게 삭제하는 함수"""

@router.get('/total')
def gen_value():
    """redis에 저장된 객체가 몇 개인지 리턴하는 함수"""

@router.get('/{count}')
def gen_value(count: int):
    """redis에 저장된 객체를 입력한 값 수 만큼 리턴하는 함수"""