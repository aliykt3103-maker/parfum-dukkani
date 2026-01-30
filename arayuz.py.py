import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER ---
def get_envanter():
    # Erkek ve Kadın Parfümleri - En Sağlam Linkler
    data = [
        {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "tip": "Erkek", "puan": 4.9, "yorum": "Kalıcılığı muazzam."},
        {"ad": "Creed Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "tip": "Erkek", "puan": 4.8, "yorum": "Gerçek bir klasik."},
        {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "tip": "Erkek", "puan": 4.7, "yorum": "Enerjik ve dikkat çekici."},
        {"ad": "Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "tip": "Erkek", "puan": 4.9, "yorum": "Ananas ve meşe yosunu uyumu efsane."},
        {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "tip": "Erkek", "puan": 5.0, "yorum": "Benzersiz, metalik ve lüks."},
        {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "tip": "Kadın", "puan": 5.0, "yorum": "Sıktığımda herkes soruyor."},
        {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "tip": "Kadın", "puan": 4.8, "yorum": "Seksi ve çekici bir koku."},
        {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "tip": "Kadın", "puan": 4.9, "yorum": "Gül ve liçinin mükemmel birleşimi."},
        {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "tip": "Kadın", "puan": 4.7, "yorum": "Lüksün tanımı bu şişede."},
        {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.25317.jpg", "tip": "Kadın", "puan": 4.6, "yorum": "Kahve notası çok enerjik."}
    ]
    return data

# --- SESSION STATE ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'ekran' not in st.session_state: st.session_state.ekran = "GİRİŞ"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- TASARIM (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .parfum-kart { 
        background: white; border-radius: 25px; padding: 20px; text-align: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 25px;
    }
    img { border-radius: 20px; max-height: 250px; width: 100%; object-fit: contain; margin-bottom: 15px; }
    .notalar { color: white; font-size: 11px; background: #ff4d4d; padding: 5px 12px; border-radius: 10px; display: inline-block; margin-bottom: 15px; }
    .puan { color: #f1c40f; font-weight: bold; margin-bottom: 5px; }
    .yorum { font-style: italic; color: #777; font-size: 12px; margin-bottom: 15px; }
    .stButton>button { border-radius: 15px; height: 50px; font-weight: bold; background-color: #007bff !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ ---
col_l, col_s = st.columns([4, 1])
with col_l:
    if st.button("🛡 ALİY DEKANT"): st.session_state.ekran = "GİRİŞ"; st.rerun()
with col_s:
    if st.button(f"🛒 ({len(st.session_state.sepet)})"): st.session_state.ekran = "SEPET"; st.rerun()

# --- SAYFA MANTIĞI ---
envanter = get_envanter()

if st.session_state.ekran == "GİRİŞ":
    st.markdown("<h1 style='text-align:center;'>Hoş Geldiniz</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👔 ERKEK KOLEKSİYONU"): st.session_state.ekran = "Erkek"; st.rerun()
    with c2:
        if st.button("👗 KADIN KOLEKSİYONU"): st.session_state.ekran = "Kadın"; st.rerun()

elif st.session_state.ekran == "SEPET":
    st.subheader("🛒 Sepetiniz")
    if not st.session_state.sepet:
        st.info("Sepetiniz boş.")
    else:
        toplam = 0
        for i, urun in enumerate(st.session_state.sepet):
            st.write(f"🔹 {urun['ad']} ({urun['ml']}ml) - {urun['fiyat']} TL")
            toplam += urun['fiyat']
        st.divider()
        st.subheader(f"Toplam: {toplam} TL")
        if st.button("SİPARİŞİ TAMAMLA", use_container_width=True):
            st.success("Sipariş talebiniz alındı!")

else:
    st.subheader(f"✨ {st.session_state.ekran} Vitrini")
    goster = [p for p in envanter if p['tip'] == st.session_state.ekran]
    
    for p in goster:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <img src="{p["img"]}">
                <h3 style="margin:0;">{p["ad"]}</h3>
                <div class="puan">⭐ {p["puan"]}</div>
                <div class="yorum">"{p["yorum"]}"</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], value=5, key=p['ad'])
            fiyat = int(ml * p['fiyat'])
            if st.button(f"SEPETE EKLE - {fiyat} TL", key="btn_"+p['ad'], use_container_width=True):
                st.session_state.sepet.append({"ad": p['ad'], "ml": ml, "fiyat": fiyat})
                st.toast(f"{p['ad']} eklendi!")
                st.rerun()
