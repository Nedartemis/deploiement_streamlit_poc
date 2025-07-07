import sys

sys.path.append("../")
sys.path.append("src/")

import os

import streamlit as st

from backend.claude_client import ClaudeClient

TITLE = "Hello Wolrd !!!"

st.set_page_config(page_title=TITLE, layout="centered")

st.title(TITLE)


if "app_just_started" not in st.session_state:
    st.session_state.logs = ["started"]
    st.session_state.app_just_started = True
else:
    st.session_state.logs.append(f"{len(st.session_state.logs)+1} reset(s)")


def say_hello_to_claude():
    messages = [{"role": "user", "content": "Hello Claude"}]

    api_key = os.environ["API_KEY_CLAUDE"]
    print(api_key)
    st.text(api_key)
    client = ClaudeClient(api_key=api_key)
    response = client.create_message(
        messages=messages,
        max_tokens=10,
    )
    st.text(f"Claude : {response['content'][0]['text']}")


st.text(st.session_state.logs)
st.button(label="Say hello", on_click=say_hello_to_claude)
