import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- GÜNCELLENMİŞ ENVANTER (NOTALAR EKLENDİ) ---
envanter = [
    # --- ERKEK KOLEKSİYONU ---
    {"ad": "Sauvage Elixir", "marka": "Dior", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.68405.jpg", "notalar": "Tarçın, Küçük Hindistan Cevizi, Lavanta, Meyan Kökü"},
    {"ad": "Aventus", "marka": "Creed", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.9828.jpg", "notalar": "Ananas, Huş Ağacı, Misk, Elma"},
    {"ad": "Eros Parfum", "marka": "Versace", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.64205.jpg", "notalar": "Nane, Yeşil Elma, Tonka Fasulyesi, Amboksan"},
    {"ad": "Layton", "marka": "PdM", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.40387.jpg", "notalar": "Elma, Lavanta, Vanilya, Kakule"},
    
    # --- KADIN KOLEKSİYONU ---
    {"ad": "Libre Intense", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.62318.jpg", "notalar": "Lavanta, Portakal Çiçeği, Vanilya, Ambergris"},
    {"ad": "Delina Exclusif", "marka": "PdM", "fiyat": 100, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.48169.jpg", "notalar": "Liçi, Armut, Gül, Tütsü, Oud"},
    
    # --- UNİSEKS KOLEKSİYONU ---
    {"ad": "Baccarat Rouge 540", "marka": "MFK", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.33531.jpg", "notalar": "Safran, Yasemin, Amberwood, Çam Reçinesi"},
    {"ad": "Angels' Share", "marka": "Kilian", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.62615.jpg", "notalar": "Konyak, Tarçın, Meşe Odunu, Vanilya"}
    # Diğerlerini de benzer şekilde ekleyebilirsin...
]

st.set_page_config(page_title="DEKANT MAĞAZASI", layout="centered")

# --- CSS TASARIMI ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .parfum-kart { 
        border-radius: 25px; 
        padding: 15px; 
        text-align: center; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        background: white;
    }
    .notalar { color: #555; font-size: 14px; font-style: italic; margin-top: 5px; }
    .isim { font-size: 28px; font-weight: 800; color: #111; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

if 'secim' not in st.session_state:
    st.session_state.secim = None

# Giriş ekranı kodları buraya gelecek...
if st.session_state.secim is None:
    st.markdown("<h1 style='text-align:center;'>VİTRİN SEÇİN</h1>", unsafe_allow_html=True)
    if st.button("👔 ERKEK"): st.session_state.secim = "Erkek"; st.rerun()
    if st.button("👗 KADIN"): st.session_state.secim = "Kadın"; st.rerun()
    if st.button("✨ UNİSEKS"): st.session_state.secim = "Uniseks"; st.rerun()
    st.stop()

# --- MAĞAZA EKRANI ---
st.button("⬅️ GERİ", on_click=lambda: setattr(st.session_state, 'secim', None))

filtreli = [p for p in envanter if p['tip'] == st.session_state.secim]

for p in filtreli:
    with st.container():
        st.markdown(f"""
        <div class="parfum-kart">
            <img src="{p['img']}" style="width:100%; border-radius:15px;">
            <p class="isim">{p['ad']}</p>
            <p style="color:red; font-weight:bold;">Koku Piramidi:</p>
            <p class="notalar">{p.get('notalar', 'Notalar yükleniyor...')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        ml = st.select_slider(f"Miktar ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
        st.button(f"Sipariş Ver - {int(ml * p['fiyat'])} TL", key=f"btn_{p['ad']}", disabled=True)
