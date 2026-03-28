from pydantic import BaseModel 


class PatientData(BaseModel):
    first_name: str
    last_name: str

class PatientDiabetesData(BaseModel):
    first_name: str
    last_name: str
    pregnancies: int
    glucose: int
    bloodpresure: int
    skinthickness: int
    insulin: int
    bmi: float
    diabetespedigreefuntion: float
    age: int

class PatientDiabetesOutput(BaseModel):
    first_name: str
    last_name: str
    prediction: str