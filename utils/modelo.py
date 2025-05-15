from keras.models import load_model
import os

def cargar_modelo():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "../model_VGG16_v2_os.keras")

    if os.path.exists(model_path):
        try:
            return load_model(model_path)
        except:
            return None
    return None