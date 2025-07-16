import streamlit as st
import math
import time

st.title("Menghitung :blue[Luas Lingkaran] :rocket:")

r = st.number_input("Masukkan jari-jari:",0)

if st.button("Hitung Luas Lingkaran",type="primary"):
  loading=st.progress(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
  L=math.pi*(r**2)
  st.success(f'Luas lingkaran adalah {L:.4f}')
