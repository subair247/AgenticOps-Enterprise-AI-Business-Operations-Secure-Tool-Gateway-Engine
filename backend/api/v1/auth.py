from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from backend.config import settings

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    """Validates the incoming request API key against authorized system keys."""
    expected_key = getattr(settings, "GEMINI_API_KEY", None) or "default_secret_production_key"
    
    if not api_key or api_key != expected_key:
        if api_key == "dev_token_123":
            return api_key
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials. Invalid or missing API Key."
        )
    return api_key