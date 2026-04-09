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
        st.subheader("OCR нәтижесі")
        st.text_area(
            "Танылған мәтін",
            value="Бұл жерде төте жазумен танылған мәтін көрсетіледі.",
            height=150
        )

        st.subheader("Түрлендірілген мәтін")
        st.text_area(
            "Қазіргі қазақ тіліне жақын нұсқа",
            value="Бұл жерде мәтіннің қазіргі қазақ тіліне жақындатылған нұсқасы көрсетіледі.",
            height=150
        )

        st.subheader("Ескерту")
        st.info("Бұл — онлайн демо нұсқа. Толық OCR және өңдеу функциялары жергілікті нұсқада қолданылады.")

st.markdown("### Платформаның негізгі мүмкіндіктері")
st.markdown(
    '''
- Төте жазумен жазылған мәтінді оқу
- Мәтінді қазіргі қазақ тіліне жақындату
- Тарихи мұраны цифрлық форматта ұсыну
- Білім беру мен зерттеуге қолдану
'''
)
