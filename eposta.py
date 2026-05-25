import streamlit as st
import requests

API_KEY = "YOUR_API_KEY"

st.title("📧 AI E-posta Yazıcı")
st.write("Konu gir, AI profesyonel e-posta yazsın!")

konu = st.text_input("📝 E-posta konusu:")
alici = st.text_input("👤 Alıcı (örn: müşteri, patron, tedarikçi):")
ton = st.selectbox("🎯 Ton:", ["Profesyonel", "Samimi", "Resmi", "Özür dileyen", "Satış odaklı"])
uzunluk = st.selectbox("📏 Uzunluk:", ["Kısa", "Orta", "Uzun"])

if st.button("✉️ E-posta Yaz"):
    if konu:
        with st.spinner("AI yazıyor..."):
            prompt = f"Sen profesyonel bir iş yazışması uzmanısın. {alici} kişisine {ton} tonda ve {uzunluk} uzunlukta şu konuda e-posta yaz: {konu}. Konu satırı, selamlama, içerik ve kapanış ekle."
            
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": "Bearer " + API_KEY},
                json={
                    "model": "openai/gpt-4o-mini",
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            sonuc = response.json()
            st.markdown(sonuc["choices"][0]["message"]["content"])
    else:
        st.warning("Lütfen e-posta konusunu girin!")