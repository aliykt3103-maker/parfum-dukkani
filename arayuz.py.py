import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER (YÜKSEK KALİTE RESİMLER VE NOTALAR) ---
envanter = [
    # --- ERKEK ---
    {
        "ad": "Sauvage Elixir", 
        "marka": "Dior", 
        "fiyat": 75, "tip": "Erkek", 
        "img": "https://pimages.parfumo.de/720/155355_img-9714-dior-sauvage-elixir_720.jpg",
        "notalar": "Üst: Tarçın, Kakule | Orta: Lavanta | Alt: Meyan Kökü, Sandal Ağacı"
    },
    {
        "ad": "Aventus", 
        "marka": "Creed", 
        "fiyat": 100, "tip": "Erkek", 
        "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg",
        "notalar": "Üst: Ananas, Bergamot | Orta: Huş Ağacı, Yasemin | Alt: Misk, Meşe Yosunu"
    },
    {
        "ad": "Eros Parfum", 
        "marka": "Versace", 
        "fiyat": 75, "tip": "Erkek", 
        "img": "https://pimages.parfumo.de/720/155700_img-4171-versace-eros-parfum_720.jpg",
        "notalar": "Üst: Nane, Limon | Orta: Elma, Sardunya | Alt: Tonka Fasulyesi, Amber"
    },
    # --- KADIN ---
    {
        "ad": "Libre Intense", 
        "marka": "YSL", 
        "fiyat": 75, "tip": "Kadın", 
        "img": "https://pimages.parfumo.de/720/141873_img-9169-ysl-libre-eau-de-parfum-intense_720.jpg",
        "notalar": "Üst: Mandalina, Lavanta | Orta: Orkide, Portakal Çiçeği | Alt: Vanilya, Amber"
    },
    {
        "ad": "Good Girl", 
        "marka": "C. Herrera", 
        "fiyat": 75, "tip": "Kadın", 
        "img": "https://pimages.parfumo.de/720/79361_img-6617-carolina-herrera-good-girl_720.jpg",
        "notalar": "Üst: Badem, Kahve | Orta: Yasemin, Zambak | Alt: Tonka Fasulyesi, Kakao"
    },
    # --- UNİSEKS ---
    {
        "ad": "Baccarat Rouge 540", 
        "marka": "MFK", 
        "fiyat": 100, "tip": "Uniseks", 
        "img": "https://pimages.parfumo.de/720/63510_img-1313-maison-francis-kurkdjian-baccarat-rouge-540_720.jpg",
        "notalar": "Üst: Safran, Yasemin | Orta: Amberwood | Alt: Çam Reçinesi, Sedir"
    },
    {
        "ad": "Angels' Share", 
        "marka": "Kilian", 
        "fiyat": 100, "tip": "Uniseks", 
        "img": "https://pimages.parfumo.de/720/144675_img-2821-by-kilian-angels-share_720.jpg",
        "notalar": "Üst: Konyak | Orta: Tarçın, Meşe | Alt: Vanilya, Pralin, Sandal"
    }
]

st.set_page_config(page_title="DEKANT MAĞAZASI", layout="centered")

# --- GELİŞMİŞ TASARIM ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .parfum-kart { 
        background: white;
        border-radius: 20px; 
        padding: 20px; 
        text-align: center; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .notalar { color: #666; font-size: 14px; line-height: 1.4; background: #fdf2f2; padding: 10px; border-radius: 10px; margin: 10px 0; border: 1px dashed red; }
    .isim { font-size: 26px; font-weight: 800; color: #111; margin-top: 15px; }
    .marka { font-size: 14px; color: #888; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

if 'secim' not in st.session_state:
    st.session_state.secim = None

# --- GİRİŞ EKRANI ---
if st.session_state.secim is None:
    st.markdown("<h1 style='text-align:center; font-size:40px;'>KOLEKSİYON SEÇİN</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(1)
    if st.button("👔 ERKEK PARFÜMLERİ", use_container_width=True): st.session_state.secim = "Erkek"; st.rerun()
    if st.button("👗 KADIN PARFÜMLERİ", use_container_width=True): st.session_state.secim = "Kadın"; st.rerun()
    if st.button("✨ NİŞ / UNİSEKS", use_container_width=True): st.session_state.secim = "Uniseks"; st.rerun()
    st.stop()

# --- VİTRİN ---
st.button("⬅️ ANA MENÜYE DÖN", on_click=lambda: setattr(st.session_state, 'secim', None))

filtreli = [p for p in envanter if p['tip'] == st.session_state.secim]

for p in filtreli:
    with st.container():
        st.markdown(f"""
        <div class="parfum-kart">
            <p class="marka">{p['marka']}</p>
            <img src="{p['img']}" style="width:100%; max-height:400px; object-fit:contain;">
            <p class="isim">{p['ad']}</p>
            <div class="notalar">
                <b>Koku Piramidi:</b><br>{p['notalar']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
        fiyat = int(ml * p['fiyat'])
        st.button(f"SİPARİŞ VER: {fiyat} TL", use_container_width=True, disabled=True, key=f"btn_{p['ad']}")
        st.markdown("<br>", unsafe_allow_html=True)
