from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import structlog
import uvicorn
from fastapi import FastAPI

from app.config.logging_config import configure_logging
from app.routers.predict_route import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: ARG001
    configure_logging()
    logger = structlog.get_logger()
    logger.info("Starting the FastAPI app")
    yield


# Define app
app = FastAPI(lifespan=lifespan)


# Define routes
@app.get("/")
def message() -> dict:
    return {"message": "Credit Approval API"}


# Add router
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa:S104
