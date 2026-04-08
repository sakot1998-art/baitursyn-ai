import streamlit as st

st.set_page_config(page_title="Baitursyn AI", page_icon="📜")

st.title("📜 Baitursyn AI")
st.subheader("Төте жазуды оқу платформасы")

st.write("Бұл платформа төте жазуды оқуға арналған.")

file = st.file_uploader("Сурет жүкте", type=["png","jpg","jpeg"])

if file:
    st.image(file, caption="Жүктелген сурет")
    st.success("Файл қабылданды")

st.markdown("### Мүмкіндіктер:")
st.write("- Төте жазуды оқу")
st.write("- Мәтінді түрлендіру")
st.write("- Тарихи мәтіндермен жұмыс")
