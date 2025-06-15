
import streamlit as st
import requests

st.set_page_config(page_title="task-oriented chatbot", layout="centered")
st.title("Task-Oriented Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Please write task order：", key="input")

if st.button("Send") and user_input:
    st.session_state.messages.append(("user", user_input))
    res = requests.post("http://backend:8000/chat", json={"message": user_input})
    data = res.json()
    st.session_state.messages.append(("bot", data["reply"]))

    st.subheader("currently task：")
    for t in data["tasks"]:
        st.markdown(f"- {t}")

for role, msg in reversed(st.session_state.messages):
    st.chat_message(role).write(msg)
