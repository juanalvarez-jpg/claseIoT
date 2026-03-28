from fastapi import FastAPI
from router import diabetes_router
from schemas.diabetes_schemas import PatientData

app = FastAPI()
app.include_router(diabetes_router.router)

@app.get("/")
async def root():
    return{"message": "Hola mundo"}

@app.post("/patient")
async def patient(data: PatientData):
    print(data.last_name)
    return {"message": data.first_name}

