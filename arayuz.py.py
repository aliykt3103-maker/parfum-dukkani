import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ ---
def get_perfumes():
    # ERKEK PARFÜMLERİ (Örnek liste - Önceki listedeki 100 ürünün yapısını korur)
    m = [
        ("Sauvage Elixir", 95, "68415"), ("Aventus", 130, "9828"), ("Eros Parfum", 80, "63731"),
        ("Hacivat", 115, "44174"), ("Ganimede", 120, "54734"), ("Bleu Chanel", 90, "25967")
    ]
    # KADIN PARFÜMLERİ
    w = [
        ("Libre Intense", 95, "62318"), ("Good Girl", 85, "39683"), ("Delina Excl", 140, "46661"),
        ("Baccarat 540", 150, "33351"), ("Black Opium", 85, "25317")
    ]
    res = []
    for x in m: res.append({"ad":x[0],"f":x[1],"i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg","t":"Erkek"})
    for x in w: res.append({"ad":x[0],"f":x[1],"i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg","t":"Kadın"})
    return res

# --- SESSION STATE ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'sayfa' not in st.session_state: st.session_state.sayfa = "GİRİŞ"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- NAVBAR ---
c1, c2 = st.columns([4,1])
with c1: 
    if st.button("🛡 ALİY DEKANT"): st.session_state.sayfa = "GİRİŞ"; st.rerun()
with c2: 
    if st.button(f"🛒({len(st.session_state.sepet)})"): st.session_state.sayfa = "SEPET"; st.rerun()

data = get_perfumes()

# --- SAYFA: GİRİŞ ---
if st.session_state.sayfa == "GİRİŞ":
    st.title("Hoş Geldiniz")
    b1, b2 = st.columns(2)
    if b1.button("👔 ERKEK"): st.session_state.sayfa="Erkek"; st.rerun()
    if b2.button("👗 KADIN"): st.session_state.sayfa="Kadın"; st.rerun()

# --- SAYFA: SEPET (SİLME VE WHATSAPP) ---
elif st.session_state.sayfa == "SEPET":
    st.header("🛒 Sepetim")
    
    if not st.session_state.sepet:
        st.warning("Sepetiniz şu an boş.")
        if st.button("Alışverişe Başla"): st.session_state.sayfa = "GİRİŞ"; st.rerun()
    else:
        toplam_tutar = 0
        sepet_metni = "Merhaba Aliy Dekant! Siparişim şudur:\n\n"
        
        # Ürünleri Listele ve Silme Butonları
        yeni_sepet = []
        for index, item in enumerate(st.session_state.sepet):
            col_ad, col_fiyat, col_sil = st.columns([3, 1, 1])
            with col_ad: st.write(f"**{item['ad']}** ({item['ml']}ml)")
            with col_fiyat: st.write(f"{item['f']} TL")
            with col_sil:
                if st.button("❌", key=f"sil_{index}"):
                    st.session_state.sepet.pop(index)
                    st.rerun()
            
            toplam_tutar += item['f']
            sepet_metni += f"- {item['ad']} ({item['ml']}ml): {item['f']} TL\n"
        
        st.divider()
        st.subheader(f"Toplam: {toplam_tutar} TL")
        sepet_metni += f"\n*Toplam Tutar: {toplam_tutar} TL*"

        # WhatsApp Sipariş Butonu
        encoded_text = urllib.parse.quote(sepet_metni)
        whatsapp_url = f"https://wa.me/{NUMARA}?text={encoded_text}"
        
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px;">
                    🟢 WHATSAPP İLE SİPARİŞ VER
                </div>
            </a>
        ''', unsafe_allow_html=True)
        
        if st.button("Sepeti Temizle"):
            st.session_state.sepet = []
            st.rerun()

# --- SAYFA: VİTRİN ---
else:
    st.subheader(f"✨ {st.session_state.sayfa} Vitrini")
    ara = st.text_input("🔍 Ara...")
    
    listele = [i for i in data if i['t'] == st.session_state.sayfa]
    if ara: listele = [i for i in listele if ara.lower() in i['ad'].lower()]

    for i in listele:
        with st.container():
            st.markdown(f'''
                <div style="background:white; border-radius:15px; padding:15px; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:20px;">
                    <img src="{i["i"]}" style="max-height:180px;"><br>
                    <b>{i["ad"]}</b>
                </div>
            ''', unsafe_allow_html=True)
            
            ml = st.select_slider(f"Boyut ({i['ad']})", [3, 5, 10], 5, key="ml"+i['ad'])
            f_birim = int(ml * i['f'])
            
            if st.button(f"SEPETE EKLE - {f_birim} TL", key="bt"+i['ad'], use_container_width=True):
                st.session_state.sepet.append({"ad": i['ad'], "f": f_birim, "ml": ml})
                st.toast(f"{i['ad']} eklendi!")
                st.rerun()
