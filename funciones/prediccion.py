import streamlit as st
import numpy as np
import cv2
from keras.applications.imagenet_utils import preprocess_input
from utils.modelo import cargar_modelo

def clasificar_ave():
    st.title("🖼️ Clasificación de aves segun su imagen")
    names = ['Solitario Andino','Zorzal sp.','Zorzal Cara Gris', 'Zorzal Pico Naranja', 'Zorzal Sabiá','Zorzal Ventripálido', 
             'Zorzalito Sombrío','Zorzal de Anteojos', 'Zorzal Canelo','Mirlo Azulado', 'Matraca Tropical','Cucarachero Currucuchú', 
             'Cucarachero Ventrinegro','Saltapared Común', 'Chochín Montañés','Cucarachero Ruiseñor Sureño', 'Saltapared Sabanero',
             'Cucarachero Cabecigrís', 'Cucarachero Jaspeado','Cucarachero Bigotudo Montano']

    uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])
    model = cargar_modelo()

    if uploaded_file is not None and model:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        x = preprocess_input(np.expand_dims(image_resized, axis=0))

        st.info("Realizando predicción...")
        try:
            preds = model.predict(x)
            confidence = np.max(preds) * 100
            predicted_class = names[np.argmax(preds)]

            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="📷 Imagen cargada", use_container_width=True)
            st.success(f"🕊️ El modelo predice que es un: **{predicted_class}** con una confianza del **{confidence:.2f}%**")

        except Exception as e:
            st.error(f"❌ Error al predecir: {e}")
