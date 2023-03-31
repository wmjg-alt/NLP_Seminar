import streamlit as st
from ner import dependencies, get_entities_with_markup
st.set_page_config(layout="wide")

with open("static/css/app2.css") as f:
    st.markdown(f'<style> {f.read()} </style>',unsafe_allow_html=True)

with open('input.txt','r',encoding='utf8') as fx:
    exampleX = str(fx.read())

st.sidebar.markdown('# Spacy models')
model_select = st.sidebar.radio('Pick a letter', ["en_core_web_sm","en_core_web_md","en_core_web_lg"])
st.sidebar.info(f'Selected: {model_select}   \n   {"" if model_select == "en_core_web_sm" else "You may need to download the model"}' )

st.markdown('## SPACY TEXT FUN')

txt = st.text_area('NER analysis', exampleX)
if st.button('beautify'):
    with open("static/css/app2.css") as f:
        st.markdown(f'<div> {get_entities_with_markup(txt,model=model_select)}</div>', unsafe_allow_html=True)

txt2 = st.text_area('Dependency analysis', "She saw a duck with binoculars with binoculars")
if st.button('dependencies'):
    dp = dependencies(txt2,model=model_select)
    st.markdown(dp, unsafe_allow_html=True)

