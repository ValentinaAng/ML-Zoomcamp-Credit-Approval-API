import uvicorn
from fastapi import FastAPI

from app.routers.predict_route import router

# Define app
app = FastAPI()


# Define routes
@app.get("/")
def message() -> dict:
    return {"message": "Credit Approval API"}


# Add router
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa:S104
