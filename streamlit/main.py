import streamlit as st

st.title("Streamlit App")
st.write("This is a simple Streamlit application.")

st.subheader("User Input")
st.text("Please enter some text below:")
user_input = st.text_input("Enter some text:")

input_box = st.selectbox(
    "Choose an option",
    ["Option 1", "Option 2", "Option 3"]
)

res = "You selected: " + input_box

st.write("You entered:", res)

