def map_prediction_to_status(prediction: int) -> str:
    return "Credit Loan Approved" if prediction == 1 else "Credit Loan Denied"
