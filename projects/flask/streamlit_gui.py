#  this is the UI file


# streamlit_app.py
import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Flask ↔ Discord", page_icon="💬", layout="centered")
st.title("Marom's Project\nFlask ↔ Discord -> UI")

with st.form("send_form", clear_on_submit=True):
    text = st.text_input("Message", placeholder="Type a message…")
    send = st.form_submit_button("Send")
    if send:
        if not text or not text.strip():
            st.warning("Please enter some text.")
        else:
            try:
                r = requests.post(f"{BASE_URL}/input_text",
                                  json={"text": text.strip()},
                                  timeout=8)
                data = r.json() if "application/json" in r.headers.get("content-type", "") else {}
                if r.ok and data.get("status") == "success":
                    st.success("Sent ✅")
                    st.rerun()
                else:
                    st.error(f"Error: {data.get('message', r.text)}")
            except Exception as e:
                st.error(f"Request failed: {e}")

st.divider()
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Recent (last 30 min)")
with col2:
    st.button("Refresh")  # גורם ל-rerun ידני


def load_messages():
    try:
        res = requests.get(f"{BASE_URL}/get_messages", timeout=8)
        data = res.json()
        if data.get("status") != "success":
            st.error(f"API error: {data.get('message')}")
            return
        msgs = data.get("messages", [])
        if not msgs:
            st.info("No messages in the last 30 minutes.")
            return
        for m in msgs:
            st.markdown(
                f"**{m.get('content', '')}**  \n"
                f"<span style='color:#666;font-size:0.9em'>{m.get('created_at', '')}</span>",
                unsafe_allow_html=True
            )
    except Exception as errorMsg:
        st.error(f"Failed to load messages: {errorMsg}")


load_messages()
