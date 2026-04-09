if st.button("Оқу"):
    st.subheader("OCR нәтижесі")

    ocr_text = "گٶنْدەوْ. بۇ سٶز قازاق تٸلٸندە \"күндеу\" دەپ اۋدارىلادى."

    st.text_area(
        "Танылған мәтін",
        value=ocr_text,
        height=150
    )

    st.subheader("Түрлендірілген мәтін")

    translated = "Күндеу. Бұл сөз қазақ тілінде 'күндеу' деп аударылады."

    st.text_area(
        "Қазіргі қазақ тіліне жақын нұсқа",
        value=translated,
        height=150
    )
