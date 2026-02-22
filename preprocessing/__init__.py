import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
scaller = joblib.load('apps/models_scaller/scaler_sepsis.pkl')
xgb_models = joblib.load('apps/models_scaller/model_sepsis_xgboost.pkl')
model_ann = load_model('apps/models_scaller/model_sepsis_ann.keras')
