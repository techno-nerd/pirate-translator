import streamlit as st
import utils

st.set_page_config(page_title="Pirate-Speak Translator", page_icon=":pirate_flag:")
st.title("Pirate-Speak Translator")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pirate-Speak -> English")
    input = st.text_area("Enter Pirate-Speak")
    submit = st.button("Get Translation", key="PS to Eng")
    if(input and submit):
        translation = utils.get_translation(input, True)
        st.text(translation)

with col2:
    st.subheader("English -> Pirate-Speak")
    input = st.text_area("Enter English")
    submit = st.button("Get Translation", key="Eng to PS")
    if(input):
        translation = utils.get_translation(input, False)
        st.text(translation)
