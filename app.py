from fastapi import FastAPI
from routes.predict_routes import prediction
import uvicorn
app = FastAPI(
    title="Sepsis",
    version="Alpha 1.0.0",
    description="Sepsis Prediction Apps",
    openapi_url=None,      
    docs_url=None,         
    redoc_url=None         
)
app.include_router(prediction)
if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)