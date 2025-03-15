import streamlit as st
import random

# Inisialisasi Streamlit
st.title("🎮 Tuties Game - Tebak Angka 🎲")
st.markdown("### Coba tebak angka rahasia dan menangkan permainan! 🏆")

# Warna & Emoji
COLORS = {"text": "#F39C12", "success": "#2ECC71", "error": "#E74C3C"}
EMOJIS = {"low": "🔽 Terlalu kecil!", "high": "🔼 Terlalu besar!", "win": "🎉 Selamat, kamu menang!"}

# Inisialisasi angka rahasia jika belum ada
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 1000)
    st.session_state.percobaan = 0
    st.session_state.hasil_tebakan = ""

# Input angka
st.markdown(f'<p style="color:{COLORS["text"]}; font-size:20px;">🎯 Tebak Angka (1 - 1000)</p>', unsafe_allow_html=True)
tebakan = st.text_input("Masukkan tebakanmu di sini! ✏️")

if st.button("🔍 Tebak!"):
    try:
        tebakan = int(tebakan)
        st.session_state.percobaan += 1
        
        if tebakan < st.session_state.angka_rahasia:
            st.session_state.hasil_tebakan = EMOJIS["low"]
        elif tebakan > st.session_state.angka_rahasia:
            st.session_state.hasil_tebakan = EMOJIS["high"]
        else:
            st.session_state.hasil_tebakan = f'{EMOJIS["win"]} 🎊 ({st.session_state.percobaan} percobaan)'
            st.session_state.angka_rahasia = random.randint(1, 1000)
            st.session_state.percobaan = 0
    except ValueError:
        st.session_state.hasil_tebakan = "⚠️ Masukkan angka yang valid!"

# Hasil tebakan
st.markdown(f'<p style="color:{COLORS["error"] if "⚠️" in st.session_state.hasil_tebakan else COLORS["success"]}; font-size:18px;">{st.session_state.hasil_tebakan}</p>', unsafe_allow_html=True)

# Motivasi
if "Selamat" in st.session_state.hasil_tebakan:
    st.balloons()
    st.markdown("💡 **Tip:** Coba tantang temanmu untuk bermain juga!")
