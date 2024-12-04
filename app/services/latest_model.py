from pathlib import Path

import joblib
from fastapi import HTTPException
from sklearn.pipeline import Pipeline

# Define the path where your models are stored
current_dir = Path(__file__).parent
root_dir = current_dir.parent.parent
MODEL_DIR = root_dir / "models"


# Function that retrieves the latest model version
def get_latest_model_path(model_dir: str) -> str:
    # Use Path.glob to find all model files matching the pattern
    model_files = sorted(
        Path(model_dir).glob("best_model*_v*.pkl"),
        key=lambda f: tuple(map(int, f.stem.split("_v")[-1].split("."))),
        reverse=True,
    )

    if model_files:
        return str(model_files[0])  # Return the latest model file path

    raise HTTPException(status_code=404, detail="No model file found!")


# Get the best model
def load_model(model_dir: str = str(MODEL_DIR)) -> Pipeline:
    # Get the latest model path
    model_path = get_latest_model_path(model_dir)

    # Check if the model file exists before loading
    if not Path(model_path).exists():
        raise HTTPException(status_code=404, detail=f"Model file not found at {model_path}")

    return joblib.load(model_path)
