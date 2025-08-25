#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests
import csv
from datetime import datetime
import os

# ---------- Settings ----------
N8N_WEBHOOK_URL = "https://omniafawzy.app.n8n.cloud/webhook/bb7703a6-9697-4062-b8cd-8d6fbe3de489/chat"
FIXED_PASSWORD = "1052003"  # Fixed password anyone can use

# ---------- Create CSV if it doesn't exist ----------
if not os.path.exists("users_log.csv"):
    with open("users_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "login_time"])

st.title("AI Agent Chat")

# ---------- User Input ----------
username = st.text_input("Enter your name")
password = st.text_input("Enter the password", type="password")

if password == FIXED_PASSWORD and username:
    st.success(f"Welcome {username}! You can start chatting now.")
    
    # ---------- Log user entry ----------
    with open("users_log.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    # ---------- Chat Interface ----------
    message = st.text_input("Type your message here")
    
    if st.button("Send"):
        try:
            # Send message to n8n webhook
            response = requests.post(
                N8N_WEBHOOK_URL,
                json={"message": message, "user": username}
            )
            data = response.json()
            st.write(data.get("reply", "No reply received yet."))
        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    if username or password:
        st.warning("Incorrect password or missing name")


# In[ ]:




