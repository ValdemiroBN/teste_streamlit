import streamlit as st
import bcrypt

# Simula banco de dados de usuários
users_db = {
    "medico@exemplo.com": bcrypt.hashpw("senha123".encode(), bcrypt.gensalt())
}

def login(email, password):
    if email in users_db:
        hashed = users_db[email]
        if bcrypt.checkpw(password.encode(), hashed):
            return True
    return False

def main():
    st.title("Login simples")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if login(email, password):
                st.session_state.logged_in = True
                st.success("Logado com sucesso!")
            else:
                st.error("Email ou senha incorretos.")
    else:
        st.write("Bem-vindo ao sistema!")
        if st.button("Sair"):
            st.session_state.logged_in = False

if __name__ == "__main__":
    main()
