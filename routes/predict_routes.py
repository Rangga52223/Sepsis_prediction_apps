from routes import prediction
from routes.schema import PatientData
from preprocessing.preprocessing import predict
@prediction.post('/')
def predictions_routes(data:PatientData):
    return predict(data)