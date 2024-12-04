import pandas as pd
from fastapi import APIRouter

from app.schemas.input_schema import InputData
from app.schemas.output_schema import OutputData
from app.services.latest_model import load_model
from app.services.status_response import map_prediction_to_status

# Define router
router = APIRouter()


@router.post("/predict")
def predict_credit_loan(data: InputData) -> OutputData:
    # Convert the input data into a DataFrame
    data_dict = data.model_dump()
    data = pd.DataFrame([data_dict])  # type: ignore[reportArgumentType]

    # Make predictions
    model = load_model()
    predictions = model.predict(data)

    # Extract prediction
    prediction = predictions[0]  # because of ndarray[unknown,unknown]

    # Convert to list
    predictions_list = prediction.tolist()

    status = map_prediction_to_status(predictions_list)

    # Return the prediction result
    return OutputData(prediction=predictions_list, status=status)
