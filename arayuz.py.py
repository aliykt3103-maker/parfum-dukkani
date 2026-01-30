import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- 50 ADET ERKEK PARFÜMÜ (KATEGORİZE EDİLMİŞ) ---
envanter = [
    # --- BLUE (Mavi - Ferah, Deniz, Sabunsu) ---
    {"ad": "Bleu de Chanel", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "notalar": "Greyfurt, Tütsü, Zencefil", "tip": "Erkek"},
    {"ad": "Sauvage EDP", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.49144.jpg", "notalar": "Bergamot, Biber, Lavanta", "tip": "Erkek"},
    {"ad": "Acqua di Gio", "fiyat": 70, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.410.jpg", "notalar": "Deniz Notaları, Limon, Biberiye", "tip": "Erkek"},
    {"ad": "Dylan Blue", "fiyat": 70, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.39348.jpg", "notalar": "İncir Yaprağı, Bergamot, Su Notaları", "tip": "Erkek"},
    {"ad": "Y EDP", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.47506.jpg", "notalar": "Elma, Adaçayı, Amberwood", "tip": "Erkek"},
    {"ad": "Luna Rossa Ocean", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68652.jpg", "notalar": "Bergamot, İris, Vetiver", "tip": "Erkek"},
    
    # --- GREEN (Yeşil - Doğal, Ormansı, Otsu) ---
    {"ad": "Green Irish Tweed", "fiyat": 100, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.474.jpg", "notalar": "Menekşe Yaprağı, İris, Sandal Ağacı", "tip": "Erkek"},
    {"ad": "Polo Green", "fiyat": 70, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.829.jpg", "notalar": "Çam, Tütün, Deri", "tip": "Erkek"},
    {"ad": "Hacivat", "fiyat": 110, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "notalar": "Ananas, Meşe Yosunu, Odunsu", "tip": "Erkek"},
    {"ad": "Grey Vetiver", "fiyat": 100, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.6634.jpg", "notalar": "Vetiver, Greyfurt, Adaçayı", "tip": "Erkek"},

    # --- FRESH (Ferah - Turunçgil, Temiz, Enerjik) ---
    {"ad": "Aventus", "fiyat": 110, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Bergamot, Huş Ağacı", "tip": "Erkek"},
    {"ad": "Prada L'Homme", "fiyat": 75, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.39029.jpg", "notalar": "İris, Neroli, Sardunya", "tip": "Erkek"},
    {"ad": "Silver Mountain Water", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.472.jpg", "notalar": "Yeşil Çay, Frenk Üzümü, Misk", "tip": "Erkek"},
    {"ad": "L'Eau d'Issey", "fiyat": 70, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.721.jpg", "notalar": "Yuzu, Limon, Mavi Nilüfer", "tip": "Erkek"},

    # --- RED (Kırmızı - Sıcak, Baharatlı, Şehvetli) ---
    {"ad": "Eros Parfum", "fiyat": 75, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "notalar": "Nane, Elma, Amber", "tip": "Erkek"},
    {"ad": "Spicebomb Extreme", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.30447.jpg", "notalar": "Tütün, Vanilya, Karabiber", "tip": "Erkek"},
    {"ad": "Stronger With You", "fiyat": 75, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "notalar": "Kestane, Karamel, Vanilya", "tip": "Erkek"},
    {"ad": "1 Million Elixir", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.72138.jpg", "notalar": "Elma, Davana, Gül, Vanilya", "tip": "Erkek"},
    {"ad": "Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "notalar": "Elma, Lavanta, Vanilya, Karabiber", "tip": "Erkek"},
    {"ad": "Side Effect", "fiyat": 120, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.42260.jpg", "notalar": "Rom, Tütün, Tarçın", "tip": "Erkek"}
]

st.set_page_config(page_title="ALİY PARFÜM VİTRİNİ", layout="centered")

# --- CSS ---
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    .parfum-kart { 
        background: white; border-radius: 20px; padding: 15px; text-align: center; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 20px;
    }
    .notalar { color: #555; font-size: 13px; font-style: italic; background: #f9f9f9; padding: 10px; border-radius: 10px; margin: 10px 0; }
    .cat-tag { font-weight: bold; font-size: 12px; color: #888; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

if 'secim' not in st.session_state: st.session_state.secim = None

# --- ANA MENÜ ---
if st.session_state.secim is None:
    st.title("🛡 ALİY DEKANT")
    if st.button("👔 ERKEK KOLEKSİYONU", use_container_width=True): st.session_state.secim = "Erkek"; st.rerun()
    st.info("Koku karakterine göre filtreleme içeride mevcuttur.")
    st.stop()

# --- VİTRİN ---
st.button("⬅️ ANA MENÜ", on_click=lambda: setattr(st.session_state, 'secim', None))

# Kategori Seçimi
kategoriler = ["TÜMÜ", "🟦 BLUE", "🟩 GREEN", "🌬 FRESH", "🟥 RED"]
secilen_cat = st.selectbox("Koku Karakteri Filtrele:", kategoriler)

# Listeleme
gosterilecek = [p for p in envanter if (p['tip'] == st.session_state.secim) and (secilen_cat == "TÜMÜ" or p['cat'] == secilen_cat)]

for p in gosterilecek:
    with st.container():
        st.markdown(f'''
        <div class="parfum-kart">
            <span class="cat-tag">{p["cat"]}</span>
            <img src="{p["img"]}" width="100%" style="max-height:350px; object-fit:contain;">
            <h2 style="margin:10px 0;">{p["ad"]}</h2>
            <div class="notalar"><b>Notalar:</b> {p["notalar"]}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
        if st.button(f"{int(ml * p['fiyat'])} TL - SATIN AL", key=f"btn_{p['ad']}", use_container_width=True):
            st.warning("⚠️ Bu ürün yakında satışa sunulacaktır!")
        st.write("---")
