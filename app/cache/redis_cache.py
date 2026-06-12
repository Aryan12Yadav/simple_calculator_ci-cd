import json 
import os
from dotenv import load_dotenv
import redis

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT",6379))
REDIS_DB = int(os.getenv("REDIS_DB",0))

redis_client = redis.Redis(
    host = REDIS_HOST,
    port = REDIS_PORT,
    db = REDIS_DB,
    decode_responses = True
)

class RedisCache:

    @staticmethod
    def get(key:str):
        value = redis_client.get(key)
        if value:
            return json.loads(value)
        
        return None
    
    @staticmethod
    def set(key:str,value:dict,expire:int = 300):
        redis_client.set(key,
                         json.dumps(value),
                         ex = expire)

    @staticmethod   
    def delete(key:str):
        redis_client.delete(key)
        






