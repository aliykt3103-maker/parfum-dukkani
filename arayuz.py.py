import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TÜM ENVANTER (HATASIZ YAPI) ---
def get_data():
    # Erkek Parfümleri (50 Adet için temel liste)
    erkek = [
        {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "not": "Lavanta, Tarçın"},
        {"ad": "Creed Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "not": "Ananas, Misk"},
        {"ad": "Versace Eros", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "not": "Nane, Elma"},
        {"ad": "Nishane Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "not": "Ananas, Meşe Yosunu"},
        {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "not": "Safran, Süet"},
        {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "not": "Tütsü, Greyfurt"},
        {"ad": "Dior Homme Intense", "fiyat": 95, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.13016.jpg", "not": "İris, Lavanta"},
        {"ad": "Marly Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "not": "Vanilya, Elma"},
        {"ad": "Xerjoff Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "not": "Bal, Tütün"},
        {"ad": "Stronger With You", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "not": "Kestane, Vanilya"}
    ]
    # Kadın Parfümleri (50 Adet için temel liste)
    kadin = [
        {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "not": "Lavanta, Vanilya"},
        {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "not": "Badem, Kahve"},
        {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "not": "Gül, Liçi"},
        {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "not": "Safran, Amber"},
        {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.25317.jpg", "not": "Kahve, Vanilya"},
        {"ad": "L'Interdit Rouge", "fiyat": 95, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.68656.jpg", "not": "Zencefil, Portakal"},
        {"ad": "Chance Tendre", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.8069.jpg", "not": "Ayva, Greyfurt"},
        {"ad": "Crystal Noir", "fiyat": 85, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.631.jpg", "not": "Zencefil, Amber"},
        {"ad": "La Vie Est Belle", "fiyat": 80, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.14973.jpg", "not": "Pralin, Vanilya"},
        {"ad": "Lost Cherry", "fiyat": 135, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.51411.jpg", "not": "Vişne, Badem"}
    ]
    return erkek, kadin

# --- SESSION STATE ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'sayfa' not in st.session_state: st.session_state.sayfa = "GİRİŞ"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- CSS TASARIM ---
st.markdown("""
<style>
    .parfum-kart { 
        background: white; border-radius: 20px; padding: 15px; text-align: center; 
        box-shadow: 0 5px 15px rgba(0,0,0,0.05); border: 1px solid #eee; margin-bottom: 20px;
    }
    img { border-radius: 15px; max-height: 250px; width: 100%; object-fit: contain; }
    .stButton>button { border-radius: 12px; font-weight: bold; background: #007bff !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
c_logo, c_sepet = st.columns([4, 1])
with c_logo:
    if st.button("🛡 ALİY DEKANT"): st.session_state.sayfa = "GİRİŞ"; st.rerun()
with c_sepet:
    if st.button(f"🛒 ({len(st.session_state.sepet)})"): st.session_state.sayfa = "SEPET"; st.rerun()

erkek_list, kadin_list = get_data()

# --- SAYFALAR ---
if st.session_state.sayfa == "GİRİŞ":
    st.title("Hoş Geldiniz")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👔 ERKEK"): st.session_state.sayfa = "Erkek"; st.rerun()
    with c2:
        if st.button("👗 KADIN"): st.session_state.sayfa = "Kadın"; st.rerun()

elif st.session_state.sayfa == "SEPET":
    st.subheader("🛒 Sepetiniz")
    if not st.session_state.sepet:
        st.write("Sepetiniz boş.")
    else:
        toplam = 0
        for item in st.session_state.sepet:
            st.write(f"✅ {item['ad']} ({item['ml']}ml) - {item['fiyat']} TL")
            toplam += item['fiyat']
        st.divider()
        st.subheader(f"Toplam: {toplam} TL")
        if st.button("SİPARİŞİ TAMAMLA", use_container_width=True):
            st.success("Talebiniz alındı!")

else: # VİTRİN (ERKEK/KADIN)
    st.subheader(f"✨ {st.session_state.sayfa} Koleksiyonu")
    
    # Arama ve Sıralama
    ara = st.text_input("🔍 Parfüm Ara...")
    sirala = st.selectbox("💲 Fiyat Sırala", ["Varsayılan", "Artan", "Azalan"])
    
    liste = erkek_list if st.session_state.sayfa == "Erkek" else kadin_list
    if ara:
        liste = [p for p in liste if ara.lower() in p['ad'].lower()]
    
    if sirala == "Artan": liste = sorted(liste, key=lambda x: x['fiyat'])
    elif sirala == "Azalan": liste = sorted(liste, key=lambda x: x['fiyat'], reverse=True)

    for p in liste:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <img src="{p["img"]}">
                <h3>{p["ad"]}</h3>
                <p>⭐ 4.9 | {p["not"]}</p>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut ({p['ad']})", options=[3, 5, 10], value=5, key=f"s_{p['ad']}")
            fiyat = int(ml * p['fiyat'])
            if st.button(f"SEPETE EKLE - {fiyat} TL", key=f"b_{p['ad']}", use_container_width=True):
                st.session_state.sepet.append({"ad": p['ad'], "ml": ml, "fiyat": fiyat})
                st.toast(f"{p['ad']} sepete eklendi!")
                st.rerun()
