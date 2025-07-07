import streamlit as st
from tqdm import trange

TITLE = "Hello Wolrd !!!"

st.set_page_config(page_title=TITLE, layout="centered")

st.title(TITLE)


if "app_just_started" not in st.session_state:
    st.session_state.logs = ["started"]
    st.session_state.app_just_started = True
else:
    st.session_state.logs.append(f"{len(st.session_state.logs)+1} connections")

st.text(body=st.session_state.logs)
st.button(label="fake")
st.text(body=trange(1000000))
