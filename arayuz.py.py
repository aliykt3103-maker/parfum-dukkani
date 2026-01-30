import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER ---
envanter = [
    {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "notalar": "Lavanta, Tarçın", "tip": "Erkek", "puan": 4.9, "yorum": "Efsane bir yayılımı var."},
    {"ad": "Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Misk", "tip": "Erkek", "puan": 4.8, "yorum": "Gerçek bir beyefendi kokusu."},
    {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "notalar": "Lavanta, Vanilya", "tip": "Kadın", "puan": 5.0, "yorum": "Kalıcılığı inanılmaz."},
    {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "notalar": "Safran, Amber", "tip": "Kadın", "puan": 4.7, "yorum": "Çok lüks hissettiriyor."}
    # Diğer 96 parfüm bu yapıya göre devam eder...
]

# --- SESSION STATE (SEPET VE SAYFA YÖNETİMİ) ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'sayfa' not in st.session_state: st.session_state.sayfa = "GİRİŞ"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- CSS ---
st.markdown("""
<style>
    .parfum-kart { 
        background: white; border-radius: 20px; padding: 15px; text-align: center; 
        box-shadow: 0 5px 15px rgba(0,0,0,0.05); border: 1px solid #eee; margin-bottom: 20px;
    }
    .puan-yıldız { color: #f1c40f; font-weight: bold; }
    .yorum-kutusu { font-style: italic; color: #666; font-size: 12px; background: #f9f9f9; padding: 10px; border-radius: 10px; }
    .sepet-sayaci { background: #e74c3c; color: white; padding: 2px 8px; border-radius: 50%; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# --- ÜST MENÜ (NAVBAR) ---
col_logo, col_sepet = st.columns([4, 1])
with col_logo:
    if st.button("🛡 ALİY DEKANT"): st.session_state.sayfa = "GİRİŞ"; st.rerun()
with col_sepet:
    sepet_metni = f"🛒 Sepet ({len(st.session_state.sepet)})"
    if st.button(sepet_metni): st.session_state.sayfa = "SEPET"; st.rerun()

# --- SAYFA: GİRİŞ ---
if st.session_state.sayfa == "GİRİŞ":
    st.title("Hoş Geldiniz")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👔 ERKEK"): st.session_state.sayfa = "Erkek"; st.rerun()
    with c2:
        if st.button("👗 KADIN"): st.session_state.sayfa = "Kadın"; st.rerun()

# --- SAYFA: SEPET ---
elif st.session_state.sayfa == "SEPET":
    st.subheader("🛒 Sepetiniz")
    if not st.session_state.sepet:
        st.info("Sepetiniz boş.")
    else:
        toplam_tutar = 0
        for i, urun in enumerate(st.session_state.sepet):
            col_u, col_f = st.columns([3, 1])
            with col_u: st.write(f"**{urun['ad']}** ({urun['ml']}ml)")
            with col_f: st.write(f"{urun['fiyat']} TL")
            toplam_tutar += urun['fiyat']
        st.write("---")
        st.subheader(f"Toplam: {toplam_tutar} TL")
        if st.button("ÖDEMEYE GEÇ / SATIN AL", use_container_width=True):
            st.warning("⚠️ Ödeme sistemi yakında aktif edilecektir!")
    if st.button("Alışverişe Devam Et"): st.session_state.sayfa = "GİRİŞ"; st.rerun()

# --- SAYFA: VİTRİN ---
else:
    st.subheader(f"✨ {st.session_state.sayfa} Koleksiyonu")
    arama = st.text_input("🔍 Aradığınız parfümü yazın...")
    
    goster = [p for p in envanter if p['tip'] == st.session_state.sayfa]
    if arama:
        goster = [p for p in goster if arama.lower() in p['ad'].lower()]

    for p in goster:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <img src="{p["img"]}" width="100%">
                <h3>{p["ad"]}</h3>
                <div class="puan-yıldız">⭐ {p["puan"]} / 5.0</div>
                <div class="yorum-kutusu">"{p["yorum"]}"</div>
            </div>
            ''', unsafe_allow_html=True)
            
            ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], value=5, key=f"ml_{p['ad']}")
            fiyat = int(ml * p['fiyat'])
            
            if st.button(f"SEPETE EKLE - {fiyat} TL", key=f"btn_{p['ad']}", use_container_width=True):
                st.session_state.sepet.append({"ad": p['ad'], "ml": ml, "fiyat": fiyat})
                st.success(f"{p['ad']} sepete eklendi!")
                st.rerun()
