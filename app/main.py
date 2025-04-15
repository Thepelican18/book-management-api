import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import ServerConfig
from interface.routes.book_routes import book_router

def create_app():
    fast_api_app = FastAPI(
        title="Book management API",
        description="",
        version="1.0.0",
    )
    
    fast_api_app.include_router(book_router)

    fast_api_app.add_middleware(
    CORSMiddleware,
    allow_origins=[ServerConfig.CORS_CREDENTIALS],
    allow_credentials=True,
    allow_methods=[ServerConfig.CORS_METHODS],  
    allow_headers=[ServerConfig.CORS_HEADERS],  
)
    return fast_api_app


def run_server():
    fast_api_app = create_app()
    uvicorn.run(fast_api_app, host=ServerConfig.API_HOSTNAME, port=ServerConfig.API_PORT, workers=ServerConfig.API_WORKERS)



if __name__ =="__main__":

    run_server()