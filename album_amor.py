import streamlit as st
from PIL import Image
import os
from datetime import datetime

# ================= CONFIGURACIÓN =================
st.set_page_config(
    page_title="Nuestro Libro de Amor 💖",
    page_icon="📖",
    layout="centered"
)

BASE = "libro_recuerdos"
os.makedirs(BASE, exist_ok=True)

# ================= ESTILOS =================
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
.titulo-principal {
    text-align: center;
    font-size: 42px;
    color: #d63384;
    font-weight: bold;
}
.subtitulo {
    text-align: center;
    font-size: 18px;
    color: #6f42c1;
}
.pagina {
    background-color: #ffffff;
    border-radius: 25px;
    padding: 20px;
    margin-bottom: 40px;
    border: 4px solid #ffb6c1;
}
.sticker {
    font-size: 30px;
    color: #e83e8c;
    font-weight: bold;
    text-align: center;
}
.mensaje {
    font-size: 18px;
    color: #444;
    text-align: center;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ================= TÍTULO =================
st.markdown("<div class='titulo-principal'>📖 Nuestro Libro de Recuerdos 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Cada página guarda un pedacito de nuestro amor ✨</div>", unsafe_allow_html=True)
st.write("")

# ================= MENÚ =================
opcion = st.radio(
    "💗 ¿Qué quieres hacer?",
    ["📖 Ver el libro", "➕ Agregar un recuerdo"],
    horizontal=True
)

# ================= AGREGAR RECUERDO =================
if opcion == "➕ Agregar un recuerdo":
    st.subheader("💌 Nuevo recuerdo")

    titulo = st.text_input("✨ Título grande (tipo sticker):")
    mensaje = st.text_area("💖 Mensaje bonito de ese día:", height=120)
    fotos = st.file_uploader(
        "📸 Sube muchas fotos",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if st.button("Guardar recuerdo 💕"):
        if titulo and fotos:
            fecha = datetime.now().strftime("%Y%m%d%H%M%S")
            carpeta = os.path.join(BASE, fecha)
            os.makedirs(carpeta, exist_ok=True)

            with open(os.path.join(carpeta, "titulo.txt"), "w", encoding="utf-8") as f:
                f.write(titulo)

            with open(os.path.join(carpeta, "mensaje.txt"), "w", encoding="utf-8") as f:
                f.write(mensaje)

            for foto in fotos:
                img = Image.open(foto)
                img.save(os.path.join(carpeta, foto.name))

            st.success("💖 Recuerdo guardado en nuestro libro")
        else:
            st.warning("Agrega al menos un título y una foto")

# ================= VER LIBRO =================
if opcion == "📖 Ver el libro":
    carpetas = sorted(os.listdir(BASE), reverse=True)

    if not carpetas:
        st.info("Aún no hay recuerdos guardados 💭")
    else:
        for carpeta in carpetas:
            ruta = os.path.join(BASE, carpeta)
            st.markdown("<div class='pagina'>", unsafe_allow_html=True)

            try:
                with open(os.path.join(ruta, "titulo.txt"), "r", encoding="utf-8") as f:
                    titulo = f.read()
                st.markdown(f"<div class='sticker'>💖 {titulo} 💖</div>", unsafe_allow_html=True)
            except:
                pass

            try:
                with open(os.path.join(ruta, "mensaje.txt"), "r", encoding="utf-8") as f:
                    mensaje = f.read()
                st.markdown(f"<div class='mensaje'>{mensaje}</div>", unsafe_allow_html=True)
            except:
                pass

            for archivo in os.listdir(ruta):
                if archivo.lower().endswith(("jpg", "jpeg", "png")):
                    st.image(os.path.join(ruta, archivo), use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)
