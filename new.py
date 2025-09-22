import streamlit as st
from PIL import Image
st.title('My First Streamlit App')
st.write('Hello, Streamlit! This app is running from my Conda environment.')
st.info('warning')
if st.checkbox('Show/Hide'):
    st.text('Checked....')
else:
    st.warning('you are slow')
img = Image.open('REPORT 1.png')
st.image(img, width=500)
if st.button('Log in'):
    st.success('Logged in')
else:
    st.warning('Authentication required')

# Add these to your existing code

# Slider
age = st.slider('Select your age', 0, 100, 25)
st.write(f"You are {age} years old")

# Selectbox
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {option}')

# Button
if st.button('Say Hello'):
    st.success('Hello! 👋')

# Text input
name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')
