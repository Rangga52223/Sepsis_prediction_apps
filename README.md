
# Sepsis Prediction API

## Deskripsi Proyek

Proyek ini adalah sistem prediksi sepsis berbasis machine learning yang menggunakan **Artificial Neural Network (ANN)** dan **XGBOOST** untuk mengklasifikasi risiko sepsis pada pasien rumah sakit. Model dilatih dengan pendekatan handling imbalanced data dan di-deploy sebagai REST API menggunakan Fastapi dengan containerization Docker.

**Akurasi Model: 95%**

## Performa Model

| Metrik | Nilai |
|--------|-------|
| F1-Score | 95% |
| Model Type | ANN (Keras) & XGBoost |
| Input Features | Clinical parameters |
| Output | Binary classification (Sepsis/Non-Sepsis) |

## Setup & Instalasi

### Prasyarat
- Docker
- Python 3.8+
- pip

### Build Docker Image

```bash
cd f:\Project_ai\Rumah_sakit\apps
docker build -t sepsis-api .
```

### Jalankan Container

```bash
docker run -p 8000:8000 sepsis-api
```

API akan berjalan di `http://localhost:8000`

## Penggunaan API

### Contoh Request dengan cURL

```bash
curl -X POST http://localhost:8000/api/v1/predict \
    -H "Content-Type: application/json" \
    -d '{
  "heart_rate": 103.0,
  "respiratory_rate": 21.0,
  "temperature": 37.9,
  "wbc_count": 12.5,
  "lactate_level": 2.3,
  "age": 69.0,
  "num_comorbidities": 2
}'
```

### Contoh Request dengan Python

```python
import requests

url = "http://localhost:8000/api/v1/predict"
data = {
  "heart_rate": 103.0,
  "respiratory_rate": 21.0,
  "temperature": 37.9,
  "wbc_count": 12.5,
  "lactate_level": 2.3,
  "age": 69.0,
  "num_comorbidities": 2
}
response = requests.post(url, json=data)
print(response.json())
```

## Desain & Asumsi

- **Preprocessing**: Standarisasi fitur menggunakan scaler yang tersimpan di `models_scaller/`
- **Imbalanced Data**: Ditangani dengan teknik SMOTE dan weighted loss function
- **Model**: ANN dengan layer optimization untuk mencapai akurasi 95%
- **Deployment**: FastApi untuk development, siap production dengan Gunicorn

## Struktur File

```
├── app.py - Main Fastapi application
├── requirements.txt - Dependencies
├── Dockerfile - Container configuration
├── models_scaller/ - Serialized model & scaler
├── preprocessing/ - Data preprocessing logic
└── routes/ - API endpoints & schema validation
```
