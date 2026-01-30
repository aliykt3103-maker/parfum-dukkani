import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TÜM PARFÜMLERİN OLDUĞU DEV LİSTE ---
envanter = [
    # --- ERKEK KOLEKSİYONU ---
    {"ad": "Sauvage Elixir", "marka": "Dior", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.68405.jpg"},
    {"ad": "Aventus", "marka": "Creed", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.9828.jpg"},
    {"ad": "Eros Parfum", "marka": "Versace", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.64205.jpg"},
    {"ad": "Layton", "marka": "PdM", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.40387.jpg"},
    {"ad": "Stronger With You Intensely", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.52834.jpg"},
    {"ad": "Le Male Elixir", "marka": "JPG", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.81640.jpg"},
    {"ad": "Acqua di Gio Profumo", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.29725.jpg"},
    {"ad": "Terre d'Hermes", "marka": "Hermes", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.823.jpg"},
    {"ad": "Bleu de Chanel Parfum", "marka": "Chanel", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.49911.jpg"},
    {"ad": "Interlude Man", "marka": "Amouage", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.15460.jpg"},
    {"ad": "Spicebomb Extreme", "marka": "V&R", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.30449.jpg"},
    {"ad": "Prada L'Homme", "marka": "Prada", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.39029.jpg"},
    {"ad": "Reflection Man", "marka": "Amouage", "fiyat": 100, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.920.jpg"},
    {"ad": "Valentino Uomo Born In Roma", "marka": "Valentino", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.55580.jpg"},
    {"ad": "L'Aventure", "marka": "Al Haramain", "fiyat": 75, "tip": "Erkek", "img": "https://www.fragrantica.com/images/perfume/o.40405.jpg"},
    
    # --- KADIN KOLEKSİYONU ---
    {"ad": "Libre Intense", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.62318.jpg"},
    {"ad": "Delina Exclusif", "marka": "PdM", "fiyat": 100, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.48169.jpg"},
    {"ad": "Good Girl", "marka": "C. Herrera", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.39683.jpg"},
    {"ad": "Black Opium Le Parfum", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.77144.jpg"},
    {"ad": "La Vie Est Belle", "marka": "Lancome", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.14973.jpg"},
    {"ad": "Crystal Noir", "marka": "Versace", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.631.jpg"},
    {"ad": "Alien", "marka": "Mugler", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.707.jpg"},
    {"ad": "J'adore", "marka": "Dior", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.210.jpg"},
    {"ad": "L'Interdit Rouge", "marka": "Givenchy", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.68306.jpg"},
    {"ad": "Coco Mademoiselle", "marka": "Chanel", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.611.jpg"},
    {"ad": "Hypnotic Poison", "marka": "Dior", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.219.jpg"},
    {"ad": "La Nuit Tresor", "marka": "Lancome", "fiyat": 75, "tip": "Kadın", "img": "https://www.fragrantica.com/images/perfume/o.29157.jpg"},
    
    # --- NİŞ / UNİSEKS KOLEKSİYONU ---
    {"ad": "Baccarat Rouge 540", "marka": "MFK", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.33531.jpg"},
    {"ad": "Naxos", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.30487.jpg"},
    {"ad": "Hacivat", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.44174.jpg"},
    {"ad": "Angels' Share", "marka": "Kilian", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.62615.jpg"},
    {"ad": "Ganimede", "marka": "M.A. Barrois", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.54733.jpg"},
    {"ad": "Ani", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.54785.jpg"},
    {"ad": "Erba Pura", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.54502.jpg"},
    {"ad": "Tobacco Vanille", "marka": "Tom Ford", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.1825.jpg"},
    {"ad": "Ombre Nomade", "marka": "Louis Vuitton", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.49751.jpg"},
    {"ad": "Side Effect", "marka": "Initio", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.42260.jpg"},
    {"ad": "Lost Cherry", "marka": "Tom Ford", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.51411.jpg"},
    {"ad": "Oud Wood", "marka": "Tom Ford", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.1826.jpg"},
    {"ad": "Alexandria II", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.15370.jpg"},
    {"ad": "Black Phantom", "marka": "Kilian", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.43632.jpg"},
    {"ad": "Portrait of a Lady", "marka": "Frederic Malle", "fiyat": 100, "tip": "Uniseks", "img": "https://www.fragrantica.com/images/perfume/o.10464.jpg"}
]

st.set_page_config(page_title="DEKANT MAĞAZASI", layout="centered")

# --- DEV MOBİL TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .dev-baslik { font-size: 50px !important; font-weight: 900; text-align: center; margin-bottom: 30px; }
    div.stButton > button {
        height: 120px !important;
        font-size: 30px !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        border: 3px solid black !important;
        margin-bottom: 15px;
    }
    .parfum-kart { 
        border: 1px solid #f0f0f0; 
        border-radius: 25px; 
        padding: 20px; 
        text-align: center; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    .marka { color: #888; font-size: 16px; font-weight: bold; text-transform: uppercase; }
    .isim { font-size: 32px; font-weight: 800; color: #111; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'secim' not in st.session_state:
    st.session_state.secim = None

# --- GİRİŞ EKRANI ---
if st.session_state.secim is None:
    st.markdown("<p class='dev-baslik'>KOLEKSİYON SEÇİN</p>", unsafe_allow_html=True)
    if st.button("👔 ERKEK PARFÜMLERİ", use_container_width=True):
        st.session_state.secim = "Erkek"; st.rerun()
    if st.button("👗 KADIN PARFÜMLERİ", use_container_width=True):
        st.session_state.secim = "Kadın"; st.rerun()
    if st.button("✨ NİŞ / UNİSEKS", use_container_width=True):
        st.session_state.secim = "Uniseks"; st.rerun()
    st.stop()

# --- MAĞAZA EKRANI ---
st.button("⬅️ ANA MENÜYE DÖN", on_click=lambda: setattr(st.session_state, 'secim', None))
st.markdown(f"<h1 style='text-align:center;'>{st.session_state.secim} Vitrini</h1>", unsafe_allow_html=True)

filtreli = [p for p in envanter if p['tip'] == st.session_state.secim]

for p in filtreli:
    with st.container():
        st.markdown(f"""
        <div class="parfum-kart">
            <img src="{p['img']}" style="width:100%; max-height:450px; object-fit:contain; border-radius:15px;">
            <p class="marka">{p['marka']}</p>
            <p class="isim">{p['ad']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        ml = st.select_slider(f"Miktar seçin ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
        fiyat = int(ml * p['fiyat'])
        
        # ŞİMDİLİK SADECE TANITIM MODUNDA (SİPARİŞ GİTMEZ)
        st.button(f"✨ {fiyat} TL - YAKINDA STOKTA", use_container_width=True, disabled=True, key=f"btn_{p['ad']}")
        st.markdown("<br><br>", unsafe_allow_html=True)