import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import ServerConfig
from interface.routes.book_routes import book_router
from domain.exceptions import BookNotFound, BookAlreadyExists

def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(BookNotFound)
    async def book_not_found_handler(request: Request, exc: BookNotFound):
        return JSONResponse(
            status_code=404,
            content={"detail": exc.detail}
        )

    @app.exception_handler(BookAlreadyExists)
    async def book_already_exists_handler(request: Request, exc: BookAlreadyExists):
        return JSONResponse(
            status_code=409,
            content={"detail": exc.detail}
        )
    
def register_middlewares(app: FastAPI) -> None:

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ServerConfig.CORS_ORIGINS, 
        allow_credentials=ServerConfig.CORS_CREDENTIALS,
        allow_methods=ServerConfig.CORS_METHODS,
        allow_headers=ServerConfig.CORS_HEADERS,
    )


def create_app() -> FastAPI:

    app = FastAPI(
        title="Book Management API",
        description="API para gestionar libros usando FastAPI y DDD",
        version="1.0.0",
    )
    app.include_router(book_router)
    register_exception_handlers(app)
    register_middlewares(app)
    return app

def run_server():
    fast_api_app = create_app()
    uvicorn.run(fast_api_app, host=ServerConfig.API_HOSTNAME, port=ServerConfig.API_PORT, workers=ServerConfig.API_WORKERS)

if __name__ =="__main__":
    run_server()