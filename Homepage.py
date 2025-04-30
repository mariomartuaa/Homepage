import streamlit as st
from PIL import Image

# Set halaman
st.set_page_config(page_title="Klasifikasi Instar Crocidolomia", layout="wide")

# === HEADER UTAMA ===
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .main .block-container {
            padding-top: 0rem;
        }
        
[data-testid="stHeader"] {
    background-color: #ffff;
}

[data-testid="stAppViewBlockContainer"] {
    background: linear-gradient(130deg, #fdf6ec 0%, #e6f4ea 50%, #fff9c4 100%);
}

.banner {
    background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20230912/pngtree-the-whole-field-was-full-of-cabbages-image_13120953.png');
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.banner h1 {
    font-size: 3rem;
    color: #ffffff;
    margin: 10px;
    text-shadow: 1px 1px 3px #000;
}
.banner h2 {
    font-size: 1.5rem;
    color: #f0f0f0;
    margin: 0 20px;
    text-shadow: 1px 1px 2px #000;
}
.banner button {
    height: 45px;
    padding: 0 40px;
    border-radius: 100px;
    border: 1px solid #ffffff;
    background-color: rgba(255, 255, 255, 0.8);
    color: #1b4332;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
}

.streamlit-expanderHeader {
    color: red;
}

/* Judul besar */
.big-title {
    font-size: 36px;
    font-weight: 700;
    color: #1b4332;
}

/* Subjudul */
.sub-title {
    font-size: 20px;
    color: #3a5a40;
}

/* Kartu fitur dan deskripsi instar */
.card {
    border-radius: 10px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    background-color: #ffff;
    border: 1px solid #2e5339;
    color: #2e5339;
}

.card-informasi {
    border-radius: 10px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    background-color: #ffff;
    border: 1px solid #2e5339;
    color: #2e5339;
    height: 250px;
}

/* Optional: semua heading dan teks lainnya */
</style>
""", unsafe_allow_html=True)

# === BANNER ===
# st.image("assets/banner.jpg", use_column_width=True)
st.markdown("""
    <div class="banner">
        <h1>Klasifikasi Tahapan Instar Crocidolomia Pavonana</h1>
        <h2>Unggah gambar larva Crocidolomia pavonana dan lihat hasil prediksi tahapan instarnya secara otomatis.</h2>
        <button onclick="window.scrollTo({ top: 800, behavior: 'smooth' })">Mulai</button>
    </div>
""", unsafe_allow_html=True)


# === FITUR UTAMA ===
st.markdown("---")
with st.container():
    st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Fitur Utama</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="card">🔍 <strong>Prediksi Instar Otomatis</strong><br>'
            'Model AI kami mengidentifikasi instar larva dengan akurat berdasarkan citra yang diunggah.</div>',
            unsafe_allow_html=True
        )
        
        with st.expander("Baca selengkapnya"):
            st.markdown(
                """
                <div class="card">
                    <ul>
                        <li>Menggunakan Model Pretrained CNN InceptionV3.</li>
                        <li>Memprediksi tahapan instar (1 hingga 4) berdasarkan citra larva yang diunggah.</li>
                        <li>Menampilkan hasil prediksi berserta tingkat kepercayaan (confidence score) dari setiap model.</li>
                        <li>Membantu petani dan peneliti mengidentifikasi fase larva dengan cepat dan akurat.</li>
                    </ul>
                </div>""",
                unsafe_allow_html=True
            )
            st.image("assets/banner.jpg")


    with col2:
        st.markdown(
            '<div class="card">🔥 <strong>Visualisasi Grad-CAM</strong><br>'
            'Lihat bagian gambar mana yang menjadi fokus model dalam menentukan klasifikasi.</div>',
            unsafe_allow_html=True
        )
        with st.expander("Baca selengkapnya"):
            st.markdown(
                """
                <div class="card">
                    <ul>
                        <li>Menampilkan area penting pada gambar yang memengaruhi keputusan model.</li>
                        <li>Dihasilkan dari layer konvolusi akhir dari model.</li>
                        <li>Disajikan dalam bentuk gambar heatmap superimposed di atas gambar asli.</li>
                    </ul>
                </div>""",
                unsafe_allow_html=True
            )
            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.image('assets/grad-cam.jpg')
            with col3:
                st.write('')


# === GAMBAR CROCIDILOMIA DEWASA ===
st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Crocidolomia Pavonana</h1>', unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write(' ')

# with col2:
#     st.image("assets/crocidolomia_adult.jpg")

# with col3:
#     st.write(' ')
    

st.markdown('<div style="display: flex; justify-content: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Crocidolomia_pavonana_%28ento-csiro-au%29.jpg" alt="Alternative text" style="height: 40%;"></div>', unsafe_allow_html=True)

# === PENJELASAN ILMIAH ===
# === INFORMASI PENTING (Menyamping 2 kolom seperti fitur utama) ===
col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Klasifikasi Ilmiah</h1>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card-informasi">'
        '- <strong>Kingdom</strong>: Animalia<br>'
        '- <strong>Phylum</strong>: Arthropoda<br>'
        '- <strong>Class</strong>: Insecta<br>'
        '- <strong>Ordo</strong>: Lepidoptera<br>'
        '- <strong>Family</strong>: Crambidae<br>'
        '- <strong>Genus</strong>: Crocidolomia<br>'
        '- <strong>Spesies</strong>: <em>Crocidolomia pavonana</em> (Fabricius)</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Dampak Kerusakan</h1>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card-informasi">'
        '- Menyerang <strong>daun muda</strong> dan <strong>titik tumbuh tanaman</strong>.<br>'
        '- <strong>Kerusakan hingga 100%</strong> pada musim kemarau.<br>'
        '- Larva memakan daun hingga tersisa tulangnya saja.<br>'
        '- Mengakibatkan <strong>gagal panen total</strong> jika tidak dikendalikan.</div>',
        unsafe_allow_html=True
    )

st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Tanaman Inang</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Kubis</h1>', unsafe_allow_html=True)
    st.image("assets/kubis.jpg", use_column_width=True)

with col2:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Sawi</h1>', unsafe_allow_html=True)
    st.image("assets/sawi.jpg", use_column_width=True)

with col3:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Brokoli</h1>', unsafe_allow_html=True)
    st.image("assets/sawi.jpg", use_column_width=True)


# === INSTAR SEBAGAI KARTU ===
st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Tahapan Instar Larva</h1>', unsafe_allow_html=True)
instar_data = [
    {
        "title": "Instar 1",
        "img": "assets/instar1.jpg",
        "desc": "Ukuran 1.84–2.51 mm. Warna hijau muda, kepala hitam. Tubuh halus dan lebih banyak diam."
    },
    {
        "title": "Instar 2",
        "img": "assets/instar2.jpg",
        "desc": "Ukuran 5.1–6.82 mm. Kepala coklat kemerahan. Sudah aktif makan dan merusak daun."
    },
    {
        "title": "Instar 3",
        "img": "assets/instar3.jpg",
        "desc": "Ukuran 11.97–15.85 mm. Menyebar, menyerang daun bagian dalam dan pucuk tanaman."
    },
    {
        "title": "Instar 4",
        "img": "assets/instar4.jpg",
        "desc": "Ukuran 14.25–18.7 mm. Garis-garis tubuh lebih jelas. Kepala dan kaki kecoklatan."
    }
]

cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">{instar_data[i]["title"]}</h1>', unsafe_allow_html=True)
        st.image(instar_data[i]["img"], use_column_width=True)
        st.markdown(f'<div class="card">{instar_data[i]["desc"]}</div>', unsafe_allow_html=True)

# === FOOTER ===
st.markdown("___")
st.markdown("📚 Berdasarkan penelitian Frangky J. Paat & Jantje Pelealu (Fakultas Pertanian UNSRAT)")
st.markdown("📧 Kontak: tim@instar-ai.com")
