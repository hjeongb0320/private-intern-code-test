from datetime import datetime
from dependency import redis_conn

def set_value(key: str, value: str):
  redis_conn.set(key, value)

  return f'{key}, {value}'

def get_value(key: str):
  value = redis_conn.get(key)

  return value

def get_all_values():
  all_keys = redis_conn.keys()

  all_values = {}
  for key in all_keys:
      temp = key.decode('ascii').split(":")

      if len(temp) > 1:
        continue

      value = redis_conn.get(key)

      all_values[key] = value.decode('utf-8') if value else None

  return all_values

def delete_value(key: str):
  deleted_count = redis_conn.delete(key)

  return deleted_count

def delete_all_values():
  redis_conn.flushdb()

  return None