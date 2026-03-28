import pickle
import numpy as np

from schemas.diabetes_schemas import PatientDiabetesData

# Cargar modelo
with open('RFDiabetesv132.pkl', 'rb') as file:
    RF_model2 = pickle.load(file)

labels = ['sano', 'diabetes']

def diabetes_prediction(data: PatientDiabetesData):
    xin = np.array([
        data.pregnancies,
        data.glucose,
        data.bloodpresure,
        data.skinthickness,
        data.insulin,
        data.bmi,
        data.diabetespedigreefuntion,
        data.age
    ]).reshape(1, 8)

    print("xin shape:", xin.shape)

    prediction = RF_model2.predict(xin)
    return labels[prediction[0]]