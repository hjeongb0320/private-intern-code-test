from redis import Redis
from rq import Queue

# redis와 rq가 연결되면서 자동으로 로그가 q에 남는 중이다.

redis_conn = Redis(host='test_redis', port=6379)
q = Queue('my_queue', connection=redis_conn)
