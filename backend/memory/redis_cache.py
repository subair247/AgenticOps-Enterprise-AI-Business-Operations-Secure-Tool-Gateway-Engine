import redis
from backend.config import settings

class RedisManager:
    def __init__(self):
        self.client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

    def set_session_data(self, session_id: str, data: str, expire_seconds: int = 3600):
        self.client.setex(session_id, expire_seconds, data)

    def get_session_data(self, session_id: str) -> str:
        return self.client.get(session_id)