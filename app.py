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
            ocr_text = "قازاق تىلىنىڭ كٶزىن اشقان – سٶزدىڭ سىيرىن تانيتىن ءىليم."
            translated = "Қазақ тілінің көзін ашқан – сөздің сырын танытатын ілім."

        elif "til" in filename:
            ocr_text = "تىل – قۇرال. تىلدٸ دۇرىس قولدانا بىلىۋ كەرەك."
            translated = "Тіл – құрал. Тілді дұрыс қолдана білу керек."

        elif "ala" in filename:
            ocr_text = "بٸز الاشپىز، بٸز قازاقپىز، ۇلتتى ساقتاۋ – مٸندەت."
            translated = "Біз алашпыз, біз қазақпыз, ұлтты сақтау – міндет."

        elif "kitap" in filename:
            ocr_text = "بٸلٸم – ادامعا جارىق جول كٶرسەتەتٸن قۇرال."
            translated = "Білім – адамға жарық жол көрсететін құрал."

        elif "mektep" in filename:
            ocr_text = "مەكتەپ – ۇلت بولاشاعىن دايارلايتىن ورىن."
            translated = "Мектеп – ұлт болашағын дайындайтын орын."

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

        st.success("Мәтін сәтті өңделді")
        st.info("Бұл — онлайн демо нұсқа. Нәтиже жүктелген файл атауына байланысты көрсетіледі.")

st.markdown("### Платформаның мүмкіндіктері:")
st.write("- Төте жазуды оқу")
st.write("- Мәтінді қазіргі қазақ тіліне жақын нұсқаға түрлендіру")
st.write("- Тарихи мәтіндермен жұмыс")
st.write("- Білім беру және зерттеу мақсатында қолдану")
