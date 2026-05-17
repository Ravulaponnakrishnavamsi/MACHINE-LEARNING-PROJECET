import os
import streamlit as st
import openai

# ==========================
# Configuration
# ==========================
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


if not OPENROUTER_API_KEY:
    st.error("Please set the OPENROUTER_API_KEY environment variable.")
    st.stop()

openai.api_base = OPENROUTER_API_BASE
openai.api_key = OPENROUTER_API_KEY

# ==========================
# Streamlit Page Config
# ==========================
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 AI Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# Chatbot Function
# ==========================
def get_bot_reply(user_input: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state.messages,
                {"role": "user", "content": user_input},
            ],
        )
        reply = response.choices[0].message["content"]
        return reply
    except Exception as e:
        return f"An error occurred: {e}"


# ==========================
# User Input
# ==========================
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot reply
    bot_reply = get_bot_reply(user_input)

    # Append bot reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# ==========================
# Display Chat History
# ==========================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
