from fastapi import APIRouter
from schemas.diabetes_schemas import PatientDiabetesData, PatientDiabetesOutput
from service.diabetes_service import diabetes_prediction
router = APIRouter()

@router.post("/predict")
async def predict(data: PatientDiabetesData):
    # prediction = "sano"
    prediction = diabetes_prediction(data)

    result =PatientDiabetesOutput(
        first_name=data.first_name,
        last_name=data.last_name,
        prediction=prediction
    )
    return result