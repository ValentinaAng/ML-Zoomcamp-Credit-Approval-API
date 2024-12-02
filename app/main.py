import os
from pathlib import Path

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException

from app.schemas.input_schema import InputData

# Define the path where your models are stored
MODEL_DIR = Path("C:/Users/Dell/ML-Zoomcamp/models")


def get_latest_model_path(model_dir: str) -> str:
    # List all model files in the directory
    model_files = [
        f for f in os.listdir(model_dir) if f.startswith("best_model") and f.endswith(".pkl")
    ]

    # Sort files based on version number extracted from the filename
    # Add error handling to skip files that cannot be parsed correctly
    model_files.sort(
        key=lambda x: (
            int(x.split("_v")[-1].split(".")[0])
            if x.split("_v")[-1].split(".")[0].isdigit()
            else -1
        ),
        reverse=True,
    )

    # Get the latest model file path
    latest_model = model_files[0] if model_files else None

    if latest_model:
        return str(Path(model_dir) / latest_model)
    raise HTTPException(status_code=404, detail="No model file found!")


MODEL_PATH = get_latest_model_path(str(MODEL_DIR))
model = joblib.load(MODEL_PATH)

# Define app
app = FastAPI()


@app.get("/")
def message() -> dict:
    return {"message": "Credit Approval API"}


@app.post("/predict")
def predict_credit_loan(data: InputData) -> dict:
    # Convert the input data into a DataFrame
    data_dict = data.model_dump()
    data = pd.DataFrame([data_dict])  # type: ignore[reportArgumentType]

    # Make predictions
    predictions = model.predict(data)

    # Return the prediction result
    return {"prediction": predictions.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa:S104
