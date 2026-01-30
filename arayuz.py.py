import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ ---
@st.cache_data
def get_perfumes():
    # Moodlar: "Ofis", "Randevu", "Yazlık", "Kışlık", "Lüks"
    # Önemli: PdM ve Xerjoff resimleri güncellendi
    data = []
    
    # --- ÖZEL KOLEKSİYON (Mood ve Doğru Resimler) ---
    ozel = [
        ("Xerjoff Naxos", 125, "52972", "Bal, Tütün, Lavanta", "Unisex", "Lüks"),
        ("Xerjoff Erba Pura", 125, "55444", "Meyve, Beyaz Misk", "Unisex", "Randevu"),
        ("Xerjoff Alexandria II", 160, "43862", "Gül, Ud, Elma", "Unisex", "Lüks"),
        ("PdM Herod", 115, "16939", "Tütün, Vanilya, Tarçın", "Erkek", "Kışlık"),
        ("PdM Layton", 110, "39332", "Elma, Lavanta, Vanilya", "Erkek", "Ofis"),
        ("PdM Pegasus", 110, "13387", "Badem, Vanilya", "Erkek", "Ofis"),
        ("PdM Delina", 140, "43863", "Gül, Liçi, Ravent", "Kadın", "Lüks"),
        ("PdM Delina Exclusif", 145, "46661", "Gül, Armut, Ud", "Kadın", "Randevu"),
        ("Ganimede", 125, "54734", "Mineral, Süet, Safran", "Unisex", "Ofis"),
        ("Baccarat Rouge 540", 150, "33531", "Safran, Amber, Sedir", "Unisex", "Lüks"),
        ("Sauvage Elixir", 95, "68415", "Lavanta, Meyan Kökü", "Erkek", "Randevu"),
        ("Creed Aventus", 130, "9828", "Ananas, Misk, Huş", "Erkek", "Ofis")
    ]
    
    for ad, f, kod, n, t, m in ozel:
        data.append({"ad": ad, "f": f, "i": f"https://fimgs.net/mdimg/perfume/m.{kod}.jpg", "n": n, "t": t, "mood": m})

    # Listeyi 100'e tamamlayanlar
    for i in range(1, 91):
        data.append({"ad": f"Erkek Parfüm No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "n": "Odunsu, Baharatlı", "t": "Erkek", "mood": "Ofis"})
    for i in range(1, 91):
        data.append({"ad": f"Kadın Parfüm No:{i}", "f": 85, "i": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "n": "Çiçeksi, Tatlı", "t": "Kadın", "mood": "Yazlık"})
        
    return data

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="ALİY DEKANT", layout="wide")

if 'sepet' not in st.session_state: st.session_state.sepet = []

# --- SIDEBAR (YAN MENÜ) ---
with st.sidebar:
    st.title("🛡️ ALİY DEKANT")
    st.markdown("---")
    secim = st.radio("MENÜ", ["ANA SAYFA", "TANIŞMA SETLERİ 🎁", "ERKEK", "KADIN", "UNISEX", "SEPETİM"])
    st.markdown("---")
    st.success(f"📞 WP: {NUMARA}")

perfumes = get_perfumes()

# --- 1. ÖZELLİK: TANIŞMA SETLERİ ---
if secim == "TANIŞMA SETLERİ 🎁":
    st.title("Özel Tanışma Paketleri")
    st.info("Koku dünyasını keşfetmeniz için en popüler kokuları set haline getirdik.")
    
    setler = [
        {"ad": "👑 Kraliyet Seti (3x5ml)", "f": 350, "icerik": "Naxos, Aventus, Baccarat 540", "desc": "En lüks ve en sevilen 3 dev isim bir arada."},
        {"ad": "💼 Ofis Şıklığı Seti (3x5ml)", "f": 280, "icerik": "Ganimede, Layton, PdM Pegasus", "desc": "Gün boyu temiz ve profesyonel hissetmek isteyenlere."},
        {"ad": "🔥 Randevu Seti (3x5ml)", "f": 320, "icerik": "Herod, Erba Pura, Sauvage Elixir", "desc": "Dikkat çekici ve etkileyici bir akşam için."}
    ]
    
    c1, c2, c3 = st.columns(3)
    for i, s in enumerate([c1, c2, c3]):
        with s:
            st.subheader(setler[i]["ad"])
            st.write(f"**İçerik:** {setler[i]['icerik']}")
            st.caption(setler[i]["desc"])
            st.subheader(f"{setler[i]['f']} TL")
            if st.button(f"Seti Sepete Ekle", key=f"set_{i}"):
                st.session_state.sepet.append({"ad": setler[i]["ad"], "f": setler[i]["f"], "ml": "Set"})
                st.toast("Set sepete eklendi!")

# --- ANA SAYFA ---
elif secim == "ANA SAYFA":
    st.title("Trend Kokular")
    trend = [p for p in perfumes if p['ad'] in ["Xerjoff Naxos", "Ganimede", "PdM Layton", "Baccarat Rouge 540"]]
    cols = st.columns(4)
    for i, p in enumerate(trend):
        with cols[i]:
            st.image(p['i'], use_container_width=True)
            st.write(f"**{p['ad']}**")
    st.divider()
    st.image("https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=1200", use_container_width=True)

# --- SEPET ---
elif secim == "SEPETİM":
    st.title("🛒 Sepetiniz")
    if not st.session_state.sepet:
        st.warning("Sepetiniz boş.")
    else:
        toplam = 0
        sip_notu = ""
        for idx, item in enumerate(st.session_state.sepet):
            c1, c2, c3 = st.columns([3,1,1])
            ml_text = f"({item['ml']}ml)" if item['ml'] != "Set" else ""
            c1.write(f"**{item['ad']}** {ml_text}")
            c2.write(f"{item['f']} TL")
            if c3.button("Sil", key=f"del_{idx}"):
                st.session_state.sepet.pop(idx)
                st.rerun()
            toplam += item['f']
            sip_notu += f"- {item['ad']} {ml_text}\n"
        st.divider()
        st.subheader(f"Toplam: {toplam} TL")
        encoded = urllib.parse.quote(f"Merhaba Aliy Dekant, Siparişim:\n{sip_notu}\nToplam: {toplam} TL")
        st.markdown(f'<a href="https://wa.me/{NUMARA}?text={encoded}" target="_blank" style="text-decoration:none;"><div style="background:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">SİPARİŞİ WHATSAPP\'TAN TAMAMLA</div></a>', unsafe_allow_html=True)

# --- VİTRİN ---
else:
    st.title(f"{secim} Koleksiyonu")
    
    # 2. ÖZELLİK: KARAKTER FİLTRESİ
    col_ara, col_mood = st.columns([2, 1])
    ara = col_ara.text_input("🔍 Parfüm Ara...")
    mood_secimi = col_mood.selectbox("🎭 Koku Karakteri (Mood)", ["Hepsi", "Ofis", "Randevu", "Yazlık", "Kışlık", "Lüks"])
    
    # Filtreleme Mantığı
    ekran_listesi = [p for p in perfumes if p['t'].upper() == secim]
    
    if ara:
        ekran_listesi = [p for p in ekran_listesi if ara.lower() in p['ad'].lower()]
    if mood_secimi != "Hepsi":
        ekran_listesi = [p for p in ekran_listesi if p.get('mood') == mood_secimi]

    # Koku Çarkı Bilgisi (Opsiyonel Görsel Destek)
    

    # Grid Görüntüsü (Yan yana 4'lü)
    rows = [ekran_listesi[i:i+4] for i in range(0, len(ekran_listesi), 4)]
    for row in rows:
        cols = st.columns(4)
        for i, p in enumerate(row):
            with cols[i]:
                st.image(p['i'], use_container_width=True)
                st.markdown(f"**{p['ad']}**")
                st.caption(f"🎶 {p['n']}")
                if 'mood' in p:
                    st.markdown(f"<span style='background-color: #f0f2f6; padding: 2px 8px; border-radius: 10px; font-size: 12px;'>✨ {p['mood']}</span>", unsafe_allow_html=True)
                
                ml = st.select_slider("Boyut", [3, 5, 10], 5, key=f"ml_{p['ad']}_{i}")
                
                # Fiyat Hesaplama
                if ml == 3: fiyat = int(p['f'] * 0.7)
                elif ml == 10: fiyat = int(p['f'] * 1.8)
                else: fiyat = p['f']
                
                if st.button(f"Sepete Ekle - {fiyat} TL", key=f"btn_{p['ad']}_{i}", use_container_width=True):
                    st.session_state.sepet.append({"ad": p['ad'], "f": fiyat, "ml": ml})
                    st.toast(f"{p['ad']} Sepete Eklendi!")
                    st.rerun()
