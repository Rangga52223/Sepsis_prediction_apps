# Gunakan image python yang stabil
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Hindari pembuatan file .pyc dan aktifkan buffering log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies sistem (jika diperlukan untuk XGBoost/TF)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements dan install library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file project (termasuk .pkl dan .keras)
COPY . .

# Expose port FastAPI
EXPOSE 8000

# Jalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]