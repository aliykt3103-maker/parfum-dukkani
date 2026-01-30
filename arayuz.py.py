import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TÜM PARFÜMLER (50 ERKEK + 50 KADIN BURAYA EKLENEBİLİR) ---
envanter = [
    # --- ERKEK KOLEKSİYONU ---
    {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "notalar": "Lavanta, Tarçın, Meyan Kökü", "tip": "Erkek"},
    {"ad": "Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Huş Ağacı, Misk", "tip": "Erkek"},
    {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "notalar": "Nane, Yeşil Elma, Tonka", "tip": "Erkek"},
    {"ad": "Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "notalar": "Ananas, Meşe Yosunu", "tip": "Erkek"},
    {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "notalar": "Greyfurt, Tütsü, Zencefil", "tip": "Erkek"},
    {"ad": "Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "notalar": "Elma, Lavanta, Vanilya", "tip": "Erkek"},
    {"ad": "Green Irish Tweed", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.474.jpg", "notalar": "Limon Otu, Menekşe", "tip": "Erkek"},
    {"ad": "Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "notalar": "Bal, Tütün, Lavanta", "tip": "Erkek"},
    
    # --- KADIN KOLEKSİYONU ---
    {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "notalar": "Lavanta, Portakal Çiçeği", "tip": "Kadın"},
    {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "notalar": "Badem, Kahve, Kakao", "tip": "Kadın"},
    {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "notalar": "Gül, Liçi, Tütsü", "tip": "Kadın"},
    {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "notalar": "Safran, Yasemin, Amber", "tip": "Kadın"},
    {"ad": "Crystal Noir", "fiyat": 80, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.631.jpg", "notalar": "Zencefil, Hindistan Cevizi", "tip": "Kadın"},
    {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.25317.jpg", "notalar": "Kahve, Vanilya, Yasemin", "tip": "Kadın"},
    {"ad": "L'Interdit Rouge", "fiyat": 95, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.68656.jpg", "notalar": "Kan Portakalı, Zencefil", "tip": "Kadın"},
    {"ad": "Chance Tendre", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.8069.jpg", "notalar": "Ayva, Greyfurt, Sümbül", "tip": "Kadın"}
]

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- TASARIM (Az önceki fotoğraftaki gibi premium stil) ---
st.markdown(f"""
<style>
    .stApp {{ background-color: #fdfdfd; }}
    .parfum-kart {{ 
        background: white; border-radius: 25px; padding: 20px; text-align: center; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 25px;
    }}
    img {{ border-radius: 20px; max-height: 280px; width: 100%; object-fit: contain; margin-bottom: 15px; }}
    .notalar {{ color: white; font-size: 12px; background: #e74c3c; padding: 6px 12px; border-radius: 8px; display: inline-block; margin-bottom: 10px; }}
    .cat-tag {{ background: #ffebee; color: #ff8a80; padding: 4px 12px; border-radius: 10px; font-size: 11px; font-weight: bold; text-transform: uppercase; }}
    .stButton>button {{ border-radius: 12px; height: 45px; font-weight: bold; background-color: #3498db !important; color: white !important; }}
</style>
""", unsafe_allow_html=True)

if 'ekran' not in st.session_state: st.session_state.ekran = "GİRİŞ"

# --- GİRİŞ EKRANI ---
if st.session_state.ekran == "GİRİŞ":
    st.markdown("<h1 style='text-align:center; color:#333;'>🛡 ALİY DEKANT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Premium Parfüm Koleksiyonu</p>", unsafe_allow_html=True)
    st.write("---")
    if st.button("👔 ERKEK KOLEKSİYONU", use_container_width=True):
        st.session_state.ekran = "Erkek"; st.rerun()
    if st.button("👗 KADIN KOLEKSİYONU", use_container_width=True):
        st.session_state.ekran = "Kadın"; st.rerun()

# --- KOLEKSİYON EKRANI ---
else:
    st.markdown(f"### 🛡 ALİY DEKANT - {st.session_state.ekran.upper()} VİTRİNİ")
    if st.button("⬅️ ANA MENÜ", use_container_width=True):
        st.session_state.ekran = "GİRİŞ"; st.rerun()
    
    # Filtreler
    if st.session_state.ekran == "Erkek":
        kats = ["TÜMÜ", "🟦 BLUE", "🟩 GREEN", "🌬 FRESH", "🟥 RED"]
    else:
        kats = ["TÜMÜ", "🌸 FLORAL", "🍯 GOURMAND", "✨ MYSTERY", "🌬 FRESH"]
    
    secilen = st.radio("Karakter Seçin:", kats, horizontal=True)
    
    # Listeleme
    goster = [p for p in envanter if p['tip'] == st.session_state.sayfa if True] # Basitleştirilmiş filtre
    goster = [p for p in envanter if p['tip'] == st.session_state.ekran and (secilen == "TÜMÜ" or p['cat'] == secilen)]

    for p in goster:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <span class="cat-tag">{p["cat"]}</span>
                <img src="{p["img"]}">
                <h2 style="font-size:24px; color:#111; margin-bottom:5px;">{p["ad"]}</h2>
                <div class="notalar">Notalar: {p["notalar"]}</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], value=5, key=f"sl_{p['ad']}")
            if st.button(f"{int(ml * p['fiyat'])} TL - SATIN AL", key=f"bt_{p['ad']}", use_container_width=True):
                st.warning("⚠️ Bu ürün yakında satışa sunulacaktır!")
            st.write("---")
