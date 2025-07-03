import pickle
import streamlit as st

# Load model
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
except FileNotFoundError:
    st.error("❌ Model tidak ditemukan. Pastikan file 'diabetes_model.sav' tersedia.")
    st.stop()

# Tambahkan Bootstrap CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container-custom {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title"><h1 class="text-primary">🩺 Prediksi Diabetes</h1><p>Dengan Machine Learning & Bootstrap Styling</p></div>', unsafe_allow_html=True)

# Mulai form input
st.markdown('<div class="container-custom">', unsafe_allow_html=True)

st.subheader("🔢 Masukkan Data Pasien:")

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Kehamilan (Pregnancies)', '0')
    BloodPressure = st.text_input('Tekanan Darah', '0')
    Insulin = st.text_input('Insulin', '0')
    DiabetesPedigreeFunction = st.text_input('Riwayat Keluarga', '0')

with col2:
    Glucose = st.text_input('Glukosa', '0')
    SkinThickness = st.text_input('Ketebalan Kulit', '0')
    BMI = st.text_input('BMI (Indeks Massa Tubuh)', '0')
    Age = st.text_input('Usia', '0')

st.markdown('</div>', unsafe_allow_html=True)  # Tutup div container

# Tombol prediksi
st.markdown('<br>', unsafe_allow_html=True)
if st.button('🔍 Cek Prediksi'):

    try:
        # Konversi ke float
        input_data = [
            float(Pregnancies), float(Glucose), float(BloodPressure),
            float(SkinThickness), float(Insulin), float(BMI),
            float(DiabetesPedigreeFunction), float(Age)
        ]

        prediction = diabetes_model.predict([input_data])

        if prediction[0] == 1:
            st.markdown(
                '<div class="alert alert-danger mt-4" role="alert">'
                '⚠️ <strong>Hasil:</strong> Pasien kemungkinan <strong>terkena diabetes</strong>.'
                '</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="alert alert-success mt-4" role="alert">'
                '✅ <strong>Hasil:</strong> Pasien <strong>tidak terkena diabetes</strong>.'
                '</div>', unsafe_allow_html=True)

    except ValueError:
        st.markdown(
            '<div class="alert alert-warning mt-4" role="alert">'
            '⚠️ Mohon isi semua kolom dengan angka yang valid.'
            '</div>', unsafe_allow_html=True)
