import streamlit as st

st.set_page_config(page_title="Baitursyn AI", page_icon="📜", layout="wide")

st.title("📜 Baitursyn AI")
st.subheader("Төте жазуды оқу және түрлендіру платформасы")

uploaded_file = st.file_uploader(
    "Сурет немесе PDF жүктеңіз",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file is not None:
    st.success("Файл сәтті жүктелді.")

    if uploaded_file.type and uploaded_file.type.startswith("image"):
        st.image(uploaded_file, caption="Жүктелген сурет", use_container_width=True)

    if st.button("Оқу"):
        filename = uploaded_file.name.lower()

        if "ahmet" in filename:
            ocr_text = "گٶنْدەوْ. بۇ سٶز قازاق تٸلٸندە ..."
            translated = "Күндеу. Бұл сөз қазақ тілінде ..."
        elif "kitap" in filename:
            ocr_text = "كىتاب ..."
            translated = "Кітап ..."
        else:
            ocr_text = "Бұл жерде төте жазумен танылған мәтін көрсетіледі."
            translated = "Бұл жерде мәтіннің қазіргі қазақ тіліне жақындатылған нұсқасы көрсетіледі."

        st.subheader("OCR нәтижесі")
        st.text_area("Танылған мәтін", value=ocr_text, height=150)

        st.subheader("Түрлендірілген мәтін")
        st.text_area("Қазіргі қазақ тіліне жақын нұсқа", value=translated, height=150)
