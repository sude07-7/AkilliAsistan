import streamlit as st
import time
import random
from datetime import date

# Sayfa Ayarları
st.set_page_config(page_title="Sude'nin Sayfası", layout="wide")

# ÖZEL CSS
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); }
    .feature-card { background: rgba(255, 255, 255, 0.7); padding: 20px; border-radius: 20px; border: 1px solid rgba(233, 30, 99, 0.2); margin-bottom: 15px; }
    h1, h2, h3 { color: #880e4f !important; text-align: center; }
    .stButton>button { background-color: #ec407a !important; color: white !important; border-radius: 10px !important; width: 100%; }
    </style>
""", unsafe_allow_html=True)

st.title("💖 Sude'nin Dijital Kokpiti")

# Ana sütun yapısı
col1, col2 = st.columns([1, 1])

with col1:
    # 1. Odak Modu
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("⏱️ Odak Modu")
    sure = st.slider("Dakika:", 5, 60, 25)
    if st.button("Başlat"):
        with st.empty():
            for s in range(sure * 60, 0, -1):
                st.metric("Kalan", f"{divmod(s, 60)[0]:02d}:{divmod(s, 60)[1]:02d}")
                time.sleep(1)
            st.success("Mola zamanı!")
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. İlham Panosu (Butonlu)
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("💡 İlham Panosu")
    if 'ilham' not in st.session_state: st.session_state.ilham = ""
    ilham_input = st.text_area("Kod parçacıkları veya fikirler:", value=st.session_state.ilham, height=80)
    if st.button("İlhamı Kaydet"):
        st.session_state.ilham = ilham_input
        st.success("Notun kaydedildi!")
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Günün Mottosu
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("✨ Günün Mottosu")
    mottolar = ["Bugün, başarının başladığı yerdir.", "Kodların karmaşık olabilir ama hayallerin net olsun.", "Sude, bugün harikalar yaratacaksın!"]
    st.info(random.choice(mottolar))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
   # 4. Görevler (Düzeltildi)
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("📌 Yapılacaklar")
    if 'gorevler' not in st.session_state: st.session_state.gorevler = []
    
    # key parametresini ekleyerek eski hafızayı sildik
    yeni = st.text_input("Yeni görev:", key="yeni_gorev_input") 
    
    if st.button("Ekle"):
        if yeni: 
            st.session_state.gorevler.append(yeni)
            # Butona basınca input kutusunu temizlemek için:
            st.rerun() 
            
    for g in st.session_state.gorevler: st.write(f"🎀 {g}")
    st.markdown('</div>', unsafe_allow_html=True)
    # 5. Proje Sayacı
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("📅 Proje Sayacı")
    hedef = st.date_input("Hedef tarih seç:")
    kalan = (hedef - date.today()).days
    st.info(f"Hedefe kalan gün: {kalan}")
    st.markdown('</div>', unsafe_allow_html=True)

    # 6. Hızlı Erişim
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("🔗 Hızlı Erişim")
    linkler = {"GitHub": "https://github.com", "LinkedIn": "https://linkedin.com", "Medium": "https://medium.com", "Odak Müziği": "https://spotify.com"}
    for isim, url in linkler.items():
        st.link_button(f"Git: {isim}", url)
    st.markdown('</div>', unsafe_allow_html=True)