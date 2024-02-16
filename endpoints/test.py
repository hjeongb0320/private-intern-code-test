from fastapi import APIRouter, HTTPException
import crud.redisCrud as redisCrud

router = APIRouter()

@router.post('/{key}')
def set_value(key: str):
    """Redis에 키-값 쌍을 설정하는 엔드포인트"""

    data = redisCrud.set_value(key)
    ret = {'message': f"키 '{data[0]}'에 값 '{data[1]}'을 설정했습니다."}

    return ret

@router.get('/all')
def get_all_values():
    """Redis에 있는 모든 키-값 쌍을 가져오는 엔드포인트"""

    data = redisCrud.get_all_values()
    ret = data

    return ret

@router.delete('/all')
def delete_all_values():
    """Redis에 있는 모든 키-값 쌍을 삭제하는 엔드포인트"""

    redisCrud.delete_all_values()
    ret = {'message': "모든 키-값 쌍이 삭제되었습니다."}

    return ret

@router.get('/{key}')
def get_value(key: str):
    """Redis에서 키에 해당하는 값을 가져오는 엔드포인트"""

    data = redisCrud.get_value(key)

    if data is None:
        raise HTTPException(status_code=404, detail=f"키 '{key}'에 해당하는 값이 없습니다.")
    
    ret = {'value': data.decode('utf-8')}
    
    return ret

@router.delete('/{key}')
def delete_key(key: str):
    """Redis에서 주어진 키에 해당하는 쌍을 삭제하는 엔드포인트"""

    data = redisCrud.delete_value(key)
    print(data)

    if data != 1:
        raise HTTPException(status_code=404, detail=f"키 '{key}'에 해당하는 값이 없습니다.")
    
    ret = {'message': f"키 '{key}'에 해당하는 쌍을 삭제했습니다."}

    return ret