import streamlit as st

def render(atm):
    st.success("✅ Transaksi berhasil!")

    st.markdown("### Apakah Anda ingin melakukan transaksi lain?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Ya", use_container_width=True):
            st.session_state.page = "menu"
            st.rerun()

    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.akun_login = None
            st.session_state.page = "menu"
            st.rerun()