from pydantic import BaseModel, Field


class OutputData(BaseModel):
    prediction: int = Field(..., description="Prediction if the credit load is approved or not")
    status: str = Field(..., description="Status of the credit load")
