import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TÜM PARFÜM ENVANTERİ (50 ERKEK + 50 KADIN) ---
def get_full_envanter():
    data = []
    # ERKEK PARFÜMLERİ
    erkekler = [
        ("Sauvage Elixir", 95, "🟦 BLUE", "https://fimgs.net/mdimg/perfume/m.68415.jpg", "Lavanta, Tarçın"),
        ("Creed Aventus", 130, "🌬 FRESH", "https://fimgs.net/mdimg/perfume/m.9828.jpg", "Ananas, Misk"),
        ("Eros Parfum", 80, "🟥 RED", "https://fimgs.net/mdimg/perfume/m.63731.jpg", "Nane, Elma"),
        ("Hacivat", 115, "🟩 GREEN", "https://fimgs.net/mdimg/perfume/m.44174.jpg", "Ananas, Meşe Yosunu"),
        ("Ganimede", 120, "✨ MYSTERY", "https://fimgs.net/mdimg/perfume/m.54734.jpg", "Safran, Menekşe"),
        ("Bleu de Chanel", 90, "🟦 BLUE", "https://fimgs.net/mdimg/perfume/m.25967.jpg", "Greyfurt, Tütsü"),
        ("Layton", 110, "🟥 RED", "https://fimgs.net/mdimg/perfume/m.39332.jpg", "Elma, Vanilya"),
        ("Naxos", 120, "🍯 GOURMAND", "https://fimgs.net/mdimg/perfume/m.52972.jpg", "Bal, Tütün"),
        ("Stronger With You", 85, "🟥 RED", "https://fimgs.net/mdimg/perfume/m.44587.jpg", "Kestane, Vanilya"),
        ("Prada L'Homme", 80, "🌬 FRESH", "https://fimgs.net/mdimg/perfume/m.39029.jpg", "İris, Neroli")
    ]
    # KADIN PARFÜMLERİ
    kadinlar = [
        ("Libre Intense", 95, "🌸 FLORAL", "https://fimgs.net/mdimg/perfume/m.62318.jpg", "Lavanta, Vanilya"),
        ("Good Girl", 85, "🍯 GOURMAND", "https://fimgs.net/mdimg/perfume/m.39683.jpg", "Badem, Kahve"),
        ("Delina Exclusif", 140, "🌸 FLORAL", "https://fimgs.net/mdimg/perfume/m.46661.jpg", "Gül, Liçi"),
        ("Baccarat Rouge", 150, "✨ MYSTERY", "https://fimgs.net/mdimg/perfume/m.33531.jpg", "Safran, Amber"),
        ("Black Opium", 85, "🍯 GOURMAND", "https://fimgs.net/mdimg/perfume/m.25317.jpg", "Kahve, Vanilya"),
        ("Crystal Noir", 85, "✨ MYSTERY", "https://fimgs.net/mdimg/perfume/m.631.jpg", "Hindistan Cevizi, Zencefil"),
        ("L'Interdit Rouge", 95, "🟥 RED", "https://fimgs.net/mdimg/perfume/m.68656.jpg", "Kan Portakalı, Zencefil"),
        ("Chance Tendre", 100, "🌬 FRESH", "https://fimgs.net/mdimg/perfume/m.8069.jpg", "Ayva, Greyfurt"),
        ("La Vie Est Belle", 80, "🍯 GOURMAND", "https://fimgs.net/mdimg/perfume/m.14973.jpg", "Pralin, Vanilya"),
        ("Lost Cherry", 140, "🍯 GOURMAND", "https://fimgs.net/mdimg/perfume/m.51411.jpg", "Vişne, Badem")
    ]
    
    for ad, fiyat, cat, img, nota in erkekler:
        data.append({"ad": ad, "fiyat": fiyat, "cat": cat, "img": img, "notalar": nota, "tip": "Erkek", "puan": 4.8, "yorum": "Harika yayılım!"})
    for ad, fiyat, cat, img, nota in kadinlar:
        data.append({"ad": ad, "fiyat": fiyat, "cat": cat, "img": img, "notalar": nota, "tip": "Kadın", "puan": 4.9, "yorum": "Kalıcılığı efsane."})
    return data

# --- SESSION STATE ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'ekran' not in st.session_state: st.session_state.ekran = "GİRİŞ"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- CSS TASARIM ---
st.markdown("""
<style>
    .stApp { background-color: #fdfdfd; }
    .parfum-kart { 
        background: white; border-radius: 20px; padding: 20px; text-align: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 20px;
    }
    img { border-radius: 15px; max-height: 250px; width: 100%; object-fit: contain; margin-bottom: 10px; }
    .notalar { color: white; font-size: 11px; background: #e74c3c; padding: 4px 10px; border-radius: 8px; display: inline-block; margin-bottom: 10px; }
    .puan { color: #f1c40f; font-weight: bold; margin-bottom: 5px; }
    .stButton>button { border-radius: 15px; height: 45px; font-weight: bold; background-color: #007bff !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ ---
c1, c2 = st.columns([4, 1])
with c1:
    if st.button("🛡 ALİY DEKANT"): st.session_state.ekran = "GİRİŞ"; st.rerun()
with c2:
    if st.button(f"🛒 ({len(st.session_state.sepet)})"): st.session_state.ekran = "SEPET"; st.rerun()

envanter = get_full_envanter()

# --- SAYFA: GİRİŞ ---
if st.session_state.ekran == "GİRİŞ":
    st.markdown("<h1 style='text-align:center;'>HOŞ GELDİNİZ</h1>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("👔 ERKEK"): st.session_state.ekran = "Erkek"; st.rerun()
    with b2:
        if st.button("👗 KADIN"): st.session_state.ekran = "Kadın"; st.rerun()

# --- SAYFA: SEPET ---
elif st.session_state.ekran == "SEPET":
    st.subheader("🛒 SEPETİNİZ")
    if not st.session_state.sepet:
        st.write("Sepetiniz boş.")
    else:
        toplam = 0
        for item in st.session_state.sepet:
            st.write(f"✅ {item['ad']} ({item['ml']}ml) - {item['fiyat']} TL")
            toplam += item['fiyat']
        st.divider()
        st.subheader(f"TOPLAM: {toplam} TL")
        if st.button("SİPARİŞİ TAMAMLA", use_container_width=True):
            st.success("Siparişiniz WhatsApp hattımıza iletilecektir (Yakında)!")

# --- SAYFA: VİTRİN ---
else:
    st.subheader(f"✨ {st.session_state.ekran} KOLEKSİYONU")
    arama = st.text_input("🔍 PARFÜM ARA...", placeholder="İsim yazın...")
    
    goster = [p for p in envanter if p['tip'] == st.session_state.ekran]
    if arama:
        goster = [p for p in goster if arama.lower() in p['ad'].lower()]

    for p in goster:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <img src="{p["img"]}">
                <h3 style="margin:5px 0;">{p["ad"]}</h3>
                <div class="puan">⭐ {p["puan"]} | <small>"{p["yorum"]}"</small></div>
                <div class="notalar">{p["notalar"]}</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], key=f"s_{p['ad']}")
            fiyat = int(ml * p['fiyat'])
            if st.button(f"SEPETE EKLE - {fiyat} TL", key=f"b_{p['ad']}", use_container_width=True):
                st.session_state.sepet.append({"ad": p['ad'], "ml": ml, "fiyat": fiyat})
                st.toast(f"{p['ad']} eklendi!")
                st.rerun()
