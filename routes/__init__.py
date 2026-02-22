from fastapi import APIRouter

prediction = APIRouter(
    prefix="/api/v1/predict",
    tags=["prediksi"]
)