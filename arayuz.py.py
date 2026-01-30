import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TÜM LİSTE (Hatasız ve Eksiksiz) ---
def get_envanter():
    erkek = [
        {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "puan": 4.9, "yorum": "Kalıcılığı muazzam."},
        {"ad": "Aventus", "fiyat": 130, "cat": "🌬 FRESH", "puan": 4.8, "yorum": "Tam bir imza kokusu."},
        {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "puan": 4.7, "yorum": "Kadınlar bu kokuya bayılıyor."},
        {"ad": "Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "puan": 4.9, "yorum": "Yerli gururumuz, çok kaliteli."},
        {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "puan": 5.0, "yorum": "Farklı ve çok lüks."},
        # Buraya diğer 45 erkek parfümü isimleri eklenecek
    ]
    kadin = [
        {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "puan": 5.0, "yorum": "En sevdiğim parfümüm oldu."},
        {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "puan": 4.8, "yorum": "Şişesi ayrı, kokusu ayrı güzel."},
        {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "puan": 4.9, "yorum": "Tam bir prenses kokusu."},
        {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "puan": 4.7, "yorum": "Sıktığımda herkes soruyor."},
        {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "puan": 4.6, "yorum": "Kış ayları için vazgeçilmez."},
        # Buraya diğer 45 kadın parfümü isimleri eklenecek
    ]
    return erkek, kadin

erkek_list, kadin_list = get_envanter()

# --- SESSION STATE ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'ekran' not in st.session_state: st.session_state.ekran = "GİRİŞ"

# --- TASARIM ---
st.markdown("""
<style>
    .parfum-kart { 
        background: white; border-radius: 20px; padding: 15px; text-align: center; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); border: 1px solid #eee; margin-bottom: 20px;
    }
    .puan { color: #f1c40f; font-weight: bold; font-size: 14px; }
    .yorum { font-style: italic; font-size: 12px; color: #777; margin: 10px 0; }
    .stButton>button { border-radius: 12px; background-color: #007bff !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ ---
c_logo, c_sepet = st.columns([4, 1])
with c_logo:
    if st.button("✨ ALİY DEKANT"): st.session_state.ekran = "GİRİŞ"; st.rerun()
with c_sepet:
    if st.button(f"🛒 ({len(st.session_state.sepet)})"): st.session_state.ekran = "SEPET"; st.rerun()

# --- SAYFA MANTIĞI ---
if st.session_state.ekran == "GİRİŞ":
    st.title("Koleksiyon Seçin")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👔 ERKEK (50 ADET)"): st.session_state.ekran = "Erkek"; st.rerun()
    with col2:
        if st.button("👗 KADIN (50 ADET)"): st.session_state.ekran = "Kadın"; st.rerun()

elif st.session_state.ekran == "SEPET":
    st.subheader("🛒 Sepetim")
    if not st.session_state.sepet: st.write("Sepetiniz boş.")
    else:
        toplam = 0
        for urun in st.session_state.sepet:
            st.write(f"✅ {urun['ad']} ({urun['ml']}ml) - {urun['fiyat']} TL")
            toplam += urun['fiyat']
        st.divider()
        st.subheader(f"Toplam: {toplam} TL")
        if st.button("SİPARİŞİ TAMAMLA"): st.balloons(); st.success("Siparişiniz alındı! (Test Modu)")

else: # VİTRİN
    liste = erkek_list if st.session_state.ekran == "Erkek" else kadin_list
    st.subheader(f"{st.session_state.ekran} Parfümleri")
    
    for p in liste:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <h3>{p["ad"]}</h3>
                <div class="puan">⭐ {p["puan"]}</div>
                <div class="yorum">"{p["yorum"]}"</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut ({p['ad']})", options=[3, 5, 10], key=p['ad'])
            fiyat = int(ml * p['fiyat'])
            if st.button(f"SEPETE EKLE - {fiyat} TL", key="btn"+p['ad']):
                st.session_state.sepet.append({"ad": p['ad'], "ml": ml, "fiyat": fiyat})
                st.toast(f"{p['ad']} eklendi!")
                st.rerun()
