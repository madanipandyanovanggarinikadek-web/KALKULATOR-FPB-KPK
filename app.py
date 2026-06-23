import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================

st.set_page_config(
    page_title="Kalkulator FPB & KPK",
    page_icon="🌌",
    layout="wide"
)

# =========================
# CSS GALAXY THEME
# =========================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background-image:url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564");
background-size:cover;
background-position:center;
background-attachment:fixed;
}

[data-testid="stHeader"]{
background:rgba(0,0,0,0);
}

h1,h2,h3,h4,p,label{
color:white !important;
}

.block-container{
background:rgba(0,0,0,0.45);
padding:2rem;
border-radius:20px;
backdrop-filter:blur(10px);
}

.result-box{
background:rgba(255,255,255,0.08);
padding:15px;
border-radius:15px;
margin-top:10px;
}

.euclid-box{
background:rgba(0,0,0,0.35);
padding:12px;
border-radius:12px;
margin-top:8px;
color:white;
font-size:18px;
}

.stButton>button{
background:linear-gradient(90deg,#6A5ACD,#9370DB);
color:white;
font-weight:bold;
border:none;
border-radius:10px;
height:50px;
width:100%;
}

.math-icon{
font-size:35px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

col_logo, col_title = st.columns([1,4])

with col_logo:
    st.image(
        "https://upload.wikimedia.org/wikipedia/id/0/09/Logo_Undiksha.png",
        width=120
    )

with col_title:
    st.markdown("""
    <h1>
    🌌 Kalkulator FPB & KPK
    </h1>
    <h3>
    Menggunakan Algoritma Euclid
    </h3>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='math-icon'>
∑ &nbsp; π &nbsp; √ &nbsp; ∞
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# RIWAYAT
# =========================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# =========================
# FUNGSI EUCLID
# =========================

def euclid(a, b):

    langkah = []

    x, y = a, b

    while y != 0:

        q = x // y
        r = x % y

        langkah.append(
            f"{x} = {y} × {q} + {r}"
        )

        x, y = y, r

    return x, langkah

# =========================
# INPUT
# =========================

st.subheader("📥 Input Bilangan")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Bilangan Kedua",
        min_value=1,
        step=1
    )

# =========================
# TOMBOL
# =========================

colh1, colh2 = st.columns(2)

with colh1:
    hitung = st.button("🚀 Hitung FPB & KPK")

with colh2:
    reset = st.button("🔄 Reset Riwayat")

if reset:
    st.session_state.riwayat = []
    st.rerun()

# =========================
# PROSES
# =========================

if hitung:

    fpb, langkah = euclid(a, b)

    kpk = (a * b) // fpb

    st.subheader("📋 Langkah Algoritma Euclid")

    for i, step in enumerate(langkah, start=1):
        st.markdown(
            f"""
            <div class='euclid-box'>
            Langkah {i}: {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(f"✅ FPB = {fpb}")

    st.info(f"✨ KPK = {kpk}")

    st.markdown(f"""
    <div class='result-box'>

    <h3>Perhitungan KPK</h3>

    KPK = (a × b) / FPB

    <br>

    KPK = ({a} × {b}) / {fpb}

    <br>

    KPK = {kpk}

    </div>
    """, unsafe_allow_html=True)

    st.session_state.riwayat.append(
        f"{a} dan {b} ➜ FPB = {fpb}, KPK = {kpk}"
    )

# =========================
# RIWAYAT PERHITUNGAN
# =========================

st.subheader("📜 Riwayat Perhitungan")

if len(st.session_state.riwayat) == 0:
    st.write("Belum ada riwayat perhitungan.")
else:
    for item in reversed(st.session_state.riwayat):
        st.write("•", item)
