import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER (HATA RİSKİ SIFIRLANMIŞ LİSTE) ---
erkek_parfumler = [
    {"ad": "Sauvage Elixir", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "notalar": "Lavanta, Meyan Kökü"},
    {"ad": "Creed Aventus", "fiyat": 120, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Bergamot, Misk"},
    {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "notalar": "Nane, Elma, Tonka"},
    {"ad": "Bleu de Chanel", "fiyat": 85, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "notalar": "Greyfurt, Tütsü"},
    {"ad": "Hacivat", "fiyat": 110, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "notalar": "Ananas, Meşe Yosunu"},
    {"ad": "Stronger With You", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "notalar": "Kestane, Vanilya"},
    {"ad": "Prada L'Homme", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.39029.jpg", "notalar": "İris, Neroli"},
    {"ad": "Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "notalar": "Elma, Lavanta, Vanilya"}
]

kadin_parfumler = [
    {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "notalar": "Lavanta, Orkide, Vanilya"},
    {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "notalar": "Badem, Kahve, Kakao"},
    {"ad": "Baccarat Rouge 540", "fiyat": 150, "cat": "✨ MYSTERIOUS", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "notalar": "Safran, Yasemin, Amber"},
    {"ad": "Delina Exclusif", "fiyat": 130, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "notalar": "Gül, Liçi, Tütsü"},
    {"ad": "Black Opium", "fiyat": 85, "cat": "✨ MYSTERIOUS", "img": "https://fimgs.net/mdimg/perfume/m.25317.jpg", "notalar": "Kahve, Vanilya"},
    {"ad": "Crystal Noir", "fiyat": 80, "cat": "✨ MYSTERIOUS", "img": "https://fimgs.net/mdimg/perfume/m.631.jpg", "notalar": "Hindistan Cevizi, Kehribar"},
    {"ad": "La Vie Est Belle", "fiyat": 80, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.14973.jpg", "notalar": "Pralin, Vanilya"},
    {"ad": "L'Interdit Rouge", "fiyat": 90, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.68656.jpg", "notalar": "Kan Portakalı, Zencefil"}
]

st.set_page_config(page_title="ALİY DEKANT", layout="wide")

# --- TASARIM (CSS) ---
st.markdown("""
<style>
    .parfum-kart { 
        background: white; border-radius: 15px; padding: 15px; text-align: center; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 20px;
    }
    img { border-radius: 10px; max-height: 250px; object-fit: contain; width: 100%; }
    .notalar { color: #d32f2f; font-size: 12px; font-weight: bold; background: #fff5f5; padding: 5px; border-radius: 5px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- SİSTEM ---
if 'sayfa' not in st.session_state: st.session_state.sayfa = "GİRİŞ"

if st.session_state.sayfa == "GİRİŞ":
    st.title("🛡 ALİY DEKANT VİTRİNİ")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👔 ERKEK KOLEKSİYONU", use_container_width=True):
            st.session_state.sayfa = "ERKEK"; st.rerun()
    with col2:
        if st.button("👗 KADIN KOLEKSİYONU", use_container_width=True):
            st.session_state.sayfa = "KADIN"; st.rerun()

else:
    st.button("⬅️ ANA MENÜ", on_click=lambda: setattr(st.session_state, 'sayfa', "GİRİŞ"))
    
    liste = erkek_parfumler if st.session_state.sayfa == "ERKEK" else kadin_parfumler
    st.subheader(f"✨ {st.session_state.sayfa} KOLEKSİYONU")

    cols = st.columns(2)
    for i, p in enumerate(liste):
        with cols[i % 2]:
            st.markdown(f'''
            <div class="parfum-kart">
                <small>{p["cat"]}</small>
                <img src="{p["img"]}">
                <h3 style="font-size:18px;">{p["ad"]}</h3>
                <div class="notalar">{p["notalar"]}</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider("Miktar", options=[3, 5, 10], key=f"ml_{p['ad']}_{i}")
            if st.button(f"{int(ml * p['fiyat'])} TL - SATIN AL", key=f"btn_{p['ad']}_{i}", use_container_width=True):
                st.warning("⚠️ Bu ürün yakında satışa sunulacaktır!")
