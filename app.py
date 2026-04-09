import streamlit as st

st.set_page_config(page_title="Baitursyn AI", page_icon="📜", layout="wide")

st.title("📜 Baitursyn AI")
st.subheader("Төте жазуды оқу және түрлендіру платформасы")

st.write(
    "Бұл платформа төте жазумен жазылған мәтіндерді тануға, "
    "оларды қазіргі қазақ тіліне жақын нұсқаға келтіруге арналған."
)

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
            ocr_text = "گٶندەو. بۇ سٶز قازاق تىلىندە قولدانىلعان."
            translated = "Көндеу. Бұл сөз қазақ тілінде қолданылған."
        elif "kitap" in filename:
            ocr_text = "كىتاب – بىلىم بۇلاعى."
            translated = "Кітап – білім бұлағы."
        elif "baitursyn" in filename:
            ocr_text = "احمەت بايتۇرسىنۇلى – قازاق تىل بىلىمىنىڭ نەگىزىن قالاۋشى."
            translated = "Ахмет Байтұрсынұлы – қазақ тіл білімінің негізін қалаушы."
        else:
            ocr_text = "بۇل جەردە تٶتە جازۋمەن تانىلعان مٵتىن كٶرسەتىلەدى."
            translated = "Бұл жерде мәтіннің қазіргі қазақ тіліне жақындатылған нұсқасы көрсетіледі."

        st.subheader("OCR нәтижесі")
        st.text_area(
            "Танылған мәтін",
            value=ocr_text,
            height=150
        )

        st.subheader("Түрлендірілген мәтін")
        st.text_area(
            "Қазіргі қазақ тіліне жақын нұсқа",
            value=translated,
            height=150
        )

        st.info("Бұл — онлайн демо нұсқа. Нәтиже жүктелген файл атауына қарай өзгеріп көрсетіледі.")

st.markdown("### Мүмкіндіктер:")
st.write("- Төте жазуды оқу")
st.write("- Мәтінді түрлендіру")
st.write("- Тарихи мәтіндермен жұмыс")
