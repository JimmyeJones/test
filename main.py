import streamlit as st
st.title("Title")
if st.button("Game 1"):
  select1 = 1
if st.button("Game 2"):
  select1 = 2
if st.button("Game 3"):
  select1 = 3
if st.button("Game 4"):
  select1 = 4
st.session_state["selection1"] = select1
if st.session_state["selection1"] == 1:
  st.title(f"Game {st.session_state["selection1"]}")
  st.text("mo stuff for game 1")
if st.session_state["selection1"] == 2:
  st.title(f"Game {st.session_state["selection1"]}")
  st.text("mo stuff for game 2")
if st.session_state["selection1"] == 3:
  st.title(f"Game {st.session_state["selection1"]}")
  st.text("mo stuff for game 3")
if st.session_state["selection1"] == 4:
  st.title(f"Game {st.session_state["selection1"]}")
  st.text("mo stuff for game 4")
