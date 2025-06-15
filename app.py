import streamlit as st

st.title("Aplikasi Quiz Sederhana")
st.write("Selamat datang di aplikasi quiz sederhana!")
name = st.text_input("Masukkan nama Anda:")

if st.button("Mulai Quiz"):
    st.write(f"Halo, {name}! Ayo mulai kuisnya.")

st.image("logo2.jpeg", caption="Logo Quiz", width=200)

question = "Apa ibu kota Indonesia?"
options = ["Jakarta", "Bandung", "Surabaya"]

answer = st.radio(question, options)

if st.button("Submit Jawaban"):
    if answer == "Jakarta":
        st.success("Jawaban kamu benar!")
    else:
        st.error("Jawaban salah, coba lagi!")