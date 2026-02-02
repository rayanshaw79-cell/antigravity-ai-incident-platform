from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.errors import global_exception_handler

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
    )

    app.add_exception_handler(Exception, global_exception_handler)

    @app.get("/health", tags=["system"])
    async def health_check():
        return {"status": "ok"}

    return app

app = create_app()
