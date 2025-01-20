from fastapi import FastAPI, HTTPException
import model
import database

app = FastAPI()

@app.get("/health")
async def health_check():
    return database.check_connection()

@app.get("/predict/{feature}")
async def make_prediction(feature: float):
    prediction = model.predict(feature)
    if prediction is None:
        raise HTTPException(status_code=400, detail="Datos de entrada inválidos")
    return {"feature": feature, "prediction": prediction}