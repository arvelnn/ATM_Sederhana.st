import streamlit as st
from login import login
from data import akun
from cek_saldo import tampilkan_saldo

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = None

st.title("BCI")
st.subheader("Mobile Banking")

no_rekening = st.text_input("Masukkan nomor rekening: ")
pin = st.text_input("Masukkan PIN: ", type="password")

if st.button("Login"):
    user = login(no_rekening, pin)
    if user:
        st.session_state.login = True
        st.session_state.user = user

        st.success(f"Login berhasil! Selamat datang, {akun[user]['nama']}!")
    else:
        st.error("Nomor rekening atau PIN salah. Silakan coba lagi.")

if st.session_state.login:

    tampilkan_saldo(st.session_state.user)

    if st.button("Logout"):
        st.session_state.login = False
        st.session_state.user = None
        st.rerun()