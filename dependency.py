from redis import Redis
from rq import Queue

redis_conn = Redis(host='test_redis', port=6379)
q = Queue('my_queue', connection=redis_conn)
