import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ (HER ŞEY DAHİL) ---
def get_all_data():
    # Format: (Ad, Fiyat, ResimKodu, Notalar, Kategori, Mood)
    items = [
        # XERJOFF
        ("Xerjoff Naxos", 125, "52972", "Bal, Tütün, Lavanta", "UNISEX", "Lüks"),
        ("Xerjoff Erba Pura", 125, "55444", "Meyve, Beyaz Misk", "UNISEX", "Randevu"),
        ("Xerjoff Alexandria II", 160, "43862", "Gül, Ud, Elma", "UNISEX", "Lüks"),
        # PARFUMS DE MARLY
        ("PdM Herod", 115, "16939", "Tütün, Vanilya", "ERKEK", "Kışlık"),
        ("PdM Layton", 110, "39332", "Elma, Lavanta", "ERKEK", "Ofis"),
        ("PdM Delina", 140, "43863", "Gül, Liçi", "KADIN", "Lüks"),
        ("PdM Pegasus", 110, "13387", "Badem, Vanilya", "ERKEK", "Ofis"),
        # DİĞER POPÜLERLER
        ("Ganimede", 125, "54734", "Mineral, Süet", "UNISEX", "Ofis"),
        ("Baccarat Rouge 540", 150, "33531", "Safran, Amber", "UNISEX", "Lüks"),
        ("Sauvage Elixir", 95, "68415", "Lavanta, Baharat", "ERKEK", "Randevu"),
        ("Creed Aventus", 130, "9828", "Ananas, Misk", "ERKEK", "Ofis"),
        ("Libre Intense", 95, "62318", "Lavanta, Vanilya", "KADIN", "Ofis"),
        ("Lost Cherry", 135, "51411", "Vişne, Badem", "UNISEX", "Randevu")
    ]
    
    # Listeyi 100'er taneye tamamla (Hata vermemesi için kopyalar oluşturur)
    final_list = []
    for ad, f, kod, n, k, m in items:
        final_list.append({"ad": ad, "f": f, "i": f"https://fimgs.net/mdimg/perfume/m.{kod}.jpg", "n": n, "t": k, "mood": m})
    
    for i in range(1, 90):
        final_list.append({"ad": f"Erkek No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "n": "Odunsu", "t": "ERKEK", "mood": "Ofis"})
        final_list.append({"ad": f"Kadın No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "n": "Çiçeksi", "t": "KADIN", "mood": "Yazlık"})
    
    return final_list

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="ALİY DEKANT", layout="wide")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ ALİY DEKANT")
    st.markdown("---")
    menu = st.radio("MENÜ", ["ANA SAYFA", "TANIŞMA SETLERİ 🎁", "ERKEK", "KADIN", "UNISEX", "SEPETİM"])
    st.markdown("---")
    st.write(f"📞 WP: {NUMARA}")

all_perfumes = get_all_data()

# --- MANTIK ---
if menu == "ANA SAYFA":
    st.title("Trend Kokular")
    # Trendleri göster
    cols = st.columns(4)
    trend_list = all_perfumes[:4]
    for i, p in enumerate(trend_list):
        with cols[i]:
            st.image(p['i'], use_container_width=True)
            st.write(f"**{p['ad']}**")
    st.divider()
    st.image("https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=1200", use_container_width=True)

elif menu == "TANIŞMA SETLERİ 🎁":
    st.title("🎁 Özel Tanışma Setleri")
    c1, c2, c3 = st.columns(3)
    set_verisi = [
        ("Kraliyet Seti", 350, "Naxos, Aventus, Baccarat"),
        ("Ofis Seti", 280, "Ganimede, Layton, Libre"),
        ("Randevu Seti", 320, "Herod, Erba Pura, Sauvage")
    ]
    for i, (ad, f, icerik) in enumerate(set_verisi):
        with [c1, c2, c3][i]:
            st.subheader(ad)
            st.write(f"İçerik: {icerik}")
            st.write(f"**{f} TL**")
            if st.button("Seti Ekle", key=f"set_{i}"):
                st.session_state.sepet.append({"ad": ad, "f": f, "ml": "Set"})
                st.toast(f"{ad} sepete eklendi!")

elif menu == "SEPETİM":
    st.title("🛒 Sepetim")
    toplam = 0
    sip_txt = ""
    for idx, item in enumerate(st.session_state.sepet):
        c1, c2, c3 = st.columns([3,1,1])
        c1.write(f"{item['ad']} ({item['ml']}ml)")
        c2.write(f"{item['f']} TL")
        if c3.button("Sil", key=f"s_{idx}"):
            st.session_state.sepet.pop(idx)
            st.rerun()
        toplam += item['f']
        sip_txt += f"- {item['ad']} {item['ml']}ml\n"
    
    st.subheader(f"Toplam: {toplam} TL")
    if st.button("WhatsApp'tan Sipariş Ver"):
        link = f"https://wa.me/{NUMARA}?text=" + urllib.parse.quote(f"Siparişim:\n{sip_txt}\nToplam: {toplam} TL")
        st.markdown(f'<meta http-equiv="refresh" content="0; url={link}">', unsafe_allow_html=True)

else:
    # VİTRİN (ERKEK, KADIN, UNISEX)
    st.title(f"{menu} Koleksiyonu")
    
    # Karakter Filtresi
    mood_sec = st.selectbox("🎭 Koku Karakteri", ["Hepsi", "Ofis", "Randevu", "Lüks", "Yazlık", "Kışlık"])
    
    # Filtrele
    ekran = [p for p in all_perfumes if p['t'] == menu]
    if mood_sec != "Hepsi":
        ekran = [p for p in ekran if p['mood'] == mood_sec]
    
    # Grid
    for i in range(0, len(ekran), 4):
        cols = st.columns(4)
        for j, p in enumerate(ekran[i:i+4]):
            with cols[j]:
                st.image(p['i'], use_container_width=True)
                st.markdown(f"**{p['ad']}**")
                st.caption(f"🎶 {p['n']}")
                st.write(f"✨ {p['mood']}")
                
                ml = st.select_slider("ml", [3, 5, 10], 5, key=f"ml_{p['ad']}_{i+j}")
                fiyat = int(p['f'] * 0.7) if ml == 3 else (int(p['f'] * 1.8) if ml == 10 else p['f'])
                
                if st.button(f"Ekle - {fiyat} TL", key=f"b_{p['ad']}_{i+j}"):
                    st.session_state.sepet.append({"ad": p['ad'], "f": fiyat, "ml": ml})
                    st.toast("Eklendi!")
