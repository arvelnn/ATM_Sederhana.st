import streamlit as st

def render(atm):
    st.title("🏧 ATM BCI")
    st.subheader("Modern Banking")

    no_rekening = st.text_input(
        "Masukkan nomor rekening"
    )

    pin = st.text_input(
        "Masukkan PIN",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):
        akun = atm.login(
            no_rekening,
            pin
        )

        if akun:
            st.session_state.akun_login = akun
            st.session_state.page = "menu"
            st.success(
                f"Login berhasil! Selamat datang, {akun.nama}"
            )
            st.rerun()

        else:
            st.error(
                "Nomor rekening atau PIN salah."
            )