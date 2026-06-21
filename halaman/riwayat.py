import streamlit as st

def render(atm):
    st.subheader("📜 Riwayat Transaksi")

    akun = st.session_state.akun_login

    if len(akun.riwayat) == 0:
        st.info("Belum ada riwayat transaksi.")
    else:
        for item in akun.riwayat:
            st.write(item)

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()