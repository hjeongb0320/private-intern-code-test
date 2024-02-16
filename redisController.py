from fastapi import FastAPI, APIRouter, HTTPException
from redis import Redis
from rq import Queue
from datetime import datetime

router = APIRouter()

redis_conn = Redis(host='test_redis', port=6379)
q = Queue('my_queue', connection=redis_conn)

@router.post('/{key}')
def set_value(key: str):
    """Redis에 키-값 쌍을 설정하는 엔드포인트"""
    redis_conn.set(key, datetime.today().isoformat())

    return {'message': f"키 '{key}'에 값 현재시각을 설정했습니다."}

@router.get('/all')
def get_all_values():
    """Redis에 있는 모든 키-값 쌍을 가져오는 엔드포인트"""
    all_keys = redis_conn.keys()

    all_values = {}
    for key in all_keys:
        value = redis_conn.get(key)
        all_values[key.decode('utf-8')] = value.decode('utf-8') if value else None

    return all_values

@router.delete('/all')
def delete_all_values():
    """Redis에 있는 모든 키-값 쌍을 삭제하는 엔드포인트"""
    redis_conn.flushdb()

    return {'message': "모든 키-값 쌍이 삭제되었습니다."}

@router.get('/{key}')
def get_value(key: str):
    """Redis에서 키에 해당하는 값을 가져오는 엔드포인트"""
    value = redis_conn.get(key)

    if value is None:
        raise HTTPException(status_code=404, detail=f"키 '{key}'에 해당하는 값이 없습니다.")
    
    return {'value': value.decode('utf-8')}

@router.delete('/{key}')
def delete_key(key: str):
    """Redis에서 주어진 키에 해당하는 쌍을 삭제하는 엔드포인트"""
    deleted_count = redis_conn.delete(key)

    if deleted_count != 1:
        raise HTTPException(status_code=404, detail=f"키 '{key}'에 해당하는 쌍을 삭제했습니다.")

    return {'message': f"키 '{key}'에 해당하는 쌍을 삭제했습니다."}