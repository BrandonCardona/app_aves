import streamlit as st
import pandas as pd
import os
from PIL import Image

def mostrar_especies():
    excel_path = "C:/Users/BRANDON/Desktop/streamlit-app/aves2_app/base_datos/base_datos.xlsx"
    imagenes_base = "C:/Users/BRANDON/Desktop/streamlit-app/aves2_app/base_datos/imagenes_aves"

    df = pd.read_excel(excel_path)

    st.title("📚 Catálogo de Aves")

    for idx, row in df.iterrows():
        st.header(f"{row['nombre_comun']} ({row['nombre_cientifico']})")
        st.markdown(f"**Familia:** {row['familia']}")
        st.markdown(f"**Descripción:** {row['descripcion']}")
        st.markdown(f"**Distribución:** {row['distribucion']}")
        st.markdown(f"**Estado de conservación:** {row['estado_conservacion']}")

        clase_dir = os.path.join(imagenes_base, f"clase{idx + 1}")
        if os.path.exists(clase_dir):
            imagenes = sorted([
                f for f in os.listdir(clase_dir)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            ])[:3]

            cols = st.columns(3)
            for i, img_name in enumerate(imagenes):
                img_path = os.path.join(clase_dir, img_name)
                image = Image.open(img_path).copy()
                cols[i].image(image, caption=img_name, use_container_width=True)
        else:
            st.warning(f"No se encontró la carpeta para clase{idx + 1}")

        st.markdown("---")
