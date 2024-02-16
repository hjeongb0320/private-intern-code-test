from crud import redisCrud

def runTask(uuid: str, value: str):
    ret = redisCrud.set_value(uuid, value)

    return ret
