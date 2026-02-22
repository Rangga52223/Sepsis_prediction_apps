import numpy as np
from preprocessing import scaller, xgb_models, model_ann
from fastapi import HTTPException
import pandas as pd
def predict(data):
    try:
# 2. Konversi input Pydantic ke Dictionary
        input_dict = data.dict()
        
        # 3. Definisikan urutan kolom sesuai yang diharapkan model (Critical Step!)
        # Urutan ini harus PERSIS sama dengan urutan kolom DataFrame saat training
        cols_when_model_builds = [
            'heart_rate', 'respiratory_rate', 'temperature', 
            'wbc_count', 'lactate_level', 'age', 'num_comorbidities'
        ]
        
        # 4. Ubah ke DataFrame dengan urutan kolom yang benar
        # Ini akan otomatis menghilangkan "UserWarning: X does not have valid feature names"
        input_df = pd.DataFrame([input_dict])[cols_when_model_builds]
        
        # 5. Scaling data
        # Pastikan variabel 'scaler' sudah di-load di bagian atas main.py Anda
        data_scaled = scaller.transform(input_df)
        
        # 6. Dapatkan Probabilitas dari kedua model
        # prob_xgb akan menghasilkan array seperti [[prob_0, prob_1]]
        prob_xgb = xgb_models.predict_proba(data_scaled)[:, 1]
        prob_ann = model_ann.predict(data_scaled, verbose=0).flatten()
        
        # 7. Soft Voting Ensemble (Rata-rata Probabilitas)
        # Ambil indeks [0] karena kita hanya memproses satu baris data
        final_prob = float((0.5 * prob_xgb[0]) + (0.5 * prob_ann[0]))
        
        # 8. Klasifikasi akhir (Threshold 0.5)
        prediction = 1 if final_prob >= 0.5 else 0
        status = "Sepsis" if prediction == 1 else "Normal"
        
        # 9. Return Response JSON
        return {
            "prediction": prediction,
            "status": status,
            "probability": round(final_prob, 4),
            "model_confidence": {
                "xgb_score": round(float(prob_xgb[0]), 4),
                "ann_score": round(float(prob_ann[0]), 4)
        }
            }
    except Exception as e:
        # Jika kena 400, print error di terminal buat debug
        print(f"Error Detail: {str(e)}") 
        raise HTTPException(status_code=400, detail=str(e))