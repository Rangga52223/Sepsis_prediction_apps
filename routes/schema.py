from pydantic import BaseModel
class PatientData(BaseModel):
    heart_rate: float
    respiratory_rate: float # ganti dari resp_rate
    temperature: float      # ganti dari temp
    wbc_count: float
    lactate_level: float    # ganti dari lactate
    age: float
    num_comorbidities: int