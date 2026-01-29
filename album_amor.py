import streamlit as st

st.set_page_config(
    page_title="Nuestro Libro de Amor 💖",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
body { background-color: #fff0f5; }
.titulo { text-align:center; font-size:40px; color:#d63384; font-weight:bold; }
.sub { text-align:center; font-size:18px; color:#6f42c1; }
.pagina {
    background:white;
    border:4px solid #ffb6c1;
    border-radius:25px;
    padding:25px;
    margin-bottom:40px;
}
.sticker {
    font-size:30px;
    color:#e83e8c;
    font-weight:bold;
    text-align:center;
}
.mensaje {
    font-size:18px;
    text-align:center;
    color:#444;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>📖 Nuestro Libro de Recuerdos 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Un pedacito de nuestro amor ✨</div>", unsafe_allow_html=True)
st.write("")

st.markdown("<div class='pagina'>", unsafe_allow_html=True)
st.markdown("<div class='sticker'>💖 Nuestro comienzo 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='mensaje'>Aquí va nuestra historia, escrita con amor 💌</div>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1529333166437-7750a6dd5a70", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

