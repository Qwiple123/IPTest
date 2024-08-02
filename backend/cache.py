import json
import redis
from typing import Optional, Any




class Cache:
    def __init__(self, redis_client: redis.StrictRedis):
        self.redis = redis_client

        
    def get(self, key: str) -> Optional[Any]:
        value = self.redis.get(key)
        if value:
            return json.loads(value)
        return None
    
    def set(self, key: str, value: Any):
        self.redis.set(key, json.dumps(value, default=str))
        
    def delete(self, key: str):
        self.redis.delete(key)

    

def get_cache() -> Cache:
    redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
    return Cache(redis_client)