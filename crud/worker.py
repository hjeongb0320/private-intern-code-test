from crud import redisCrud

import uuid

def runTask():
    nowUuid = uuid.uuid4()

    ret = redisCrud.set_value(nowUuid)

    return ret
