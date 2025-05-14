from keras.models import load_model
import os

def cargar_modelo():
    model_path = "C:/Users/BRANDON/Desktop/streamlit-app/aves_cardona_acosta_app/model_VGG16_v2_os.keras"
    if os.path.exists(model_path):
        try:
            return load_model(model_path)
        except:
            return None
    return None
