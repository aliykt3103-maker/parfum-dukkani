import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ ---
@st.cache_data
def get_perfumes():
    data = []
    # ÖZEL KOLEKSİYON (Görseldekiler ve İsteklerin)
    ozel = [
        ("Xerjoff Naxos", 125, "52972", "Bal, Tütün, Lavanta", "Unisex"),
        ("Xerjoff Erba Pura", 125, "55444", "Meyve, Beyaz Misk", "Unisex"),
        ("Xerjoff Alexandria II", 160, "43862", "Gül, Ud, Elma", "Unisex"),
        ("PdM Herod", 115, "16939", "Tütün, Vanilya, Tarçın", "Erkek"),
        ("PdM Layton", 110, "39332", "Elma, Lavanta, Vanilya", "Erkek"),
        ("PdM Delina", 140, "43863", "Gül, Liçi, Ravent", "Kadın"),
        ("PdM Delina Exclusif", 145, "46661", "Gül, Armut, Ud", "Kadın"),
        ("Ganimede", 125, "54734", "Mineral, Süet, Safran", "Unisex"),
        ("Baccarat Rouge 540", 150, "33531", "Safran, Amber, Sedir", "Unisex"),
        ("Sauvage Elixir", 95, "68415", "Lavanta, Meyan Kökü", "Erkek"),
        ("Creed Aventus", 130, "9828", "Ananas, Misk, Huş", "Erkek"),
        ("Libre Intense", 95, "62318", "Lavanta, Vanilya", "Kadın")
    ]
    
    for ad, f, kod, n, t in ozel:
        data.append({"ad": ad, "f": f, "i": f"https://fimgs.net/mdimg/perfume/m.{kod}.jpg", "n": n, "t": t})

    # Sayıları 100'e tamamlamak için otomatik liste
    for i in range(1, 91):
        data.append({"ad": f"Erkek Parfüm No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "n": "Odunsu, Baharatlı", "t": "Erkek"})
    for i in range(1, 91):
        data.append({"ad": f"Kadın Parfüm No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "n": "Çiçeksi, Tatlı", "t": "Kadın"})
    for i in range(1, 41):
        data.append({"ad": f"Unisex Parfüm No:{i}", "f": 110, "i": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "n": "Amber, Misk", "t": "Unisex"})
        
    return data

# --- SAYFA YAPISI ---
st.set_page_config(page_title="ALİY DEKANT", layout="wide")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ ALİY DEKANT")
    st.markdown("---")
    # Kategori isimlerini temizledik (Beyaz ekranı çözen kısım)
    secim = st.radio("MENÜ", ["ANA SAYFA", "ERKEK", "KADIN", "UNISEX", "SEPETİM"])
    st.markdown("---")
    st.success(f"📞 İletişim: {NUMARA}")

perfumes = get_perfumes()

# --- MANTIK ---
if secim == "ANA SAYFA":
    st.title("Hoş Geldiniz")
    st.image("https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=1200", use_container_width=True)
    st.info("Lütfen soldaki menüden bir kategori seçin.")

elif secim == "SEPETİM":
    st.title("🛒 Sepetiniz")
    if not st.session_state.sepet:
        st.warning("Sepetiniz şu an boş.")
    else:
        toplam = 0
        sip_notu = ""
        for idx, item in enumerate(st.session_state.sepet):
            c1, c2, c3 = st.columns([3,1,1])
            c1.write(f"**{item['ad']}** ({item['ml']}ml)")
            c2.write(f"{item['f']} TL")
            if c3.button("Sil", key=f"del_{idx}"):
                st.session_state.sepet.pop(idx)
                st.rerun()
            toplam += item['f']
            sip_notu += f"- {item['ad']} {item['ml']}ml\n"
        
        st.divider()
        st.subheader(f"Toplam: {toplam} TL")
        encoded = urllib.parse.quote(f"Merhaba Aliy Dekant, Siparişim:\n{sip_notu}\nToplam: {toplam} TL")
        st.markdown(f'<a href="https://wa.me/{NUMARA}?text={encoded}" target="_blank" style="text-decoration:none;"><div style="background:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold; font-size:20px;">WHATSAPP İLE SİPARİŞ VER</div></a>', unsafe_allow_html=True)

else:
    # KATEGORİ GÖSTERİMİ
    st.title(f"{secim} KOLEKSİYONU")
    
    # Arama ve Sıralama
    c_ara, c_sirala = st.columns([3,1])
    ara_kelime = c_ara.text_input("🔍 Parfüm ismine göre ara...")
    siralama = c_sirala.selectbox("💲 Fiyat", ["Sıralama", "Artan", "Azalan"])
    
    # Filtrele
    ekran_listesi = [p for p in perfumes if p['t'].upper() == secim]
    
    if ara_kelime:
        ekran_listesi = [p for p in ekran_listesi if ara_kelime.lower() in p['ad'].lower()]
    
    if siralama == "Artan": ekran_listesi = sorted(ekran_listesi, key=lambda x: x['f'])
    elif siralama == "Azalan": ekran_listesi = sorted(ekran_listesi, key=lambda x: x['f'], reverse=True)

    # Grid (Yan yana 4'lü)
    st.write(f"**{len(ekran_listesi)}** ürün listeleniyor.")
    rows = [ekran_listesi[i:i+4] for i in range(0, len(ekran_listesi), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for i, p in enumerate(row):
            with cols[i]:
                st.image(p['i'], use_container_width=True)
                st.subheader(p['ad'])
                st.caption(f"🎶 {p['n']}")
                
                ml = st.select_slider("Boyut Seç", [3, 5, 10], 5, key=f"ml_{p['ad']}_{i}")
                # Fiyatlandırma mantığı
                if ml == 3: fiyat = int(p['f'] * 0.7)
                elif ml == 10: fiyat = int(p['f'] * 1.8)
                else: fiyat = p['f']
                
                if st.button(f"Ekle - {fiyat} TL", key=f"btn_{p['ad']}_{i}", use_container_width=True):
                    st.session_state.sepet.append({"ad": p['ad'], "f": fiyat, "ml": ml})
                    st.toast(f"{p['ad']} eklendi!")
