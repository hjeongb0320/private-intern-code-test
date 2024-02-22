from crud import redisCrud
from datetime import datetime, timedelta

def runTask(uuid: str):
    # time.sleep(waitingTime)

    current_time_utc = datetime.utcnow()
    korea_timezone_offset = timedelta(hours=9)
    current_time_korea = current_time_utc + korea_timezone_offset

    value = current_time_korea.isoformat()
    
    ret = redisCrud.set_value(uuid, value)

    return ret
