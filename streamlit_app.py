import streamlit as st
import math

st.title("Menghitung :blue[Luas Lingkaran] :rocket:")

r = st.number_input("Masukkan jari-jari:",0)

if st.button("Hitung Luas Lingkaran",type="primary"):
  L=math.pi*(r**2)
  st.succcess(f.'Luas lingkaran adalah {L:.4f}')
