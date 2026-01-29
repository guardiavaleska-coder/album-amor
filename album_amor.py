import streamlit as st
from PIL import Image
import os
from datetime import datetime

# ================= CONFIGURACIÓN GENERAL =================
st.set_page_config(
    page_title="Nuestro Álbum de Amor 💖",
    page_icon="💝",
    layout="centered"
)

# Carpeta para guardar fotos
CARPETA_FOTOS = "fotos_album"
os.makedirs(CARPETA_FOTOS, exist_ok=True)

# ================= ESTILOS ROMÁNTICOS =================
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
.titulo {
    text-align: center;
    font-size: 40px;
    color: #d63384;
}
.mensaje {
    text-align: center;
    font-size: 18px;
    color: #6f42c1;
}
.marco {
    border: 4px solid #ffb6c1;
    padding: 15px;
    border-radius: 20px;
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ================= TÍTULO =================
st.markdown("<div class='titulo'>💞 Nuestro Álbum de Recuerdos 💞</div>", unsafe_allow_html=True)
st.markdown("<div class='mensaje'>Cada foto guarda un pedacito de nuestro amor ✨</div>", unsafe_allow_html=True)
st.write("")

# ================= SUBIR FOTOS =================
st.subheader("📸 Agregar nuevos recuerdos")

fotos = st.file_uploader(
    "Selecciona muchas fotos 💕",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

mensaje = st.text_input("💌 Mensaje bonito para este día:")

if st.button("Guardar en el Álbum 💖"):
    if fotos:
        for foto in fotos:
            imagen = Image.open(foto)
            fecha = datetime.now().strftime("%Y%m%d%H%M%S")
            nombre_archivo = f"{fecha}_{foto.name}"
            ruta = os.path.join(CARPETA_FOTOS, nombre_archivo)
            imagen.save(ruta)

            # Guardar mensaje
            with open(ruta + ".txt", "w", encoding="utf-8") as f:
                f.write(mensaje)

        st.success("💝 ¡Recuerdos guardados con amor!")
    else:
        st.warning("Selecciona al menos una foto")

# ================= MOSTRAR ÁLBUM =================
st.write("")
st.subheader("📖 Nuestro Libro de Recuerdos")

archivos = sorted(os.listdir(CARPETA_FOTOS), reverse=True)

for archivo in archivos:
    if archivo.lower().endswith((".jpg", ".png", ".jpeg")):
        ruta_imagen = os.path.join(CARPETA_FOTOS, archivo)
        ruta_texto = ruta_imagen + ".txt"

        st.markdown("<div class='marco'>", unsafe_allow_html=True)
        st.image(ruta_imagen, use_container_width=True)

        if os.path.exists(ruta_texto):
            with open(ruta_texto, "r", encoding="utf-8") as f:
                texto = f.read()
                st.markdown(f"💌 *{texto}*")

        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
