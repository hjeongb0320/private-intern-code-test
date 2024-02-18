from dependency import redis_conn

def set_value(key: str, value: str):
  redis_conn.set(key, value)

  return (key, value)

def get_value(key: str):
  value = redis_conn.get(key)

  return value

def get_all_values():
  all_keys = redis_conn.keys()

  # RQ 관련 작업 및 상태를 추적하는 key 제외하고 진짜 value를 찾기 위함
  all_values = {}
  for key in all_keys:
      temp = key.decode('ascii').split(":")

      if len(temp) > 1:
        continue

      value = redis_conn.get(key)

      all_values[key] = value.decode('utf-8') if value else None

  return all_values

def get_len():
  # 데이터 개수를 저장하고 있는 변수를 redis 내에 저장할까 고민해 보았는데
  # 한 번 그렇게 대리자와 강한 관계를 가지게 되면 관리하기가 어려울 것 같아 해당 방식 유지
  all_values = get_all_values()
  total_values = len(all_values)

  return total_values

def delete_value(key: str):
  deleted_count = redis_conn.delete(key)

  return deleted_count

def delete_all_values():
  redis_conn.flushdb()

  return None