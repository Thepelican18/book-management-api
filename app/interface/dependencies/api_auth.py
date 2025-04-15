from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from config import ServerConfig

api_key_header = APIKeyHeader(name=ServerConfig.API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    
    if api_key == ServerConfig.API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
