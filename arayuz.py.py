import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER ---
envanter = [
    {"ad": "Sauvage Elixir", "marka": "Dior", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155355_img-9714-dior-sauvage-elixir_720.jpg", "notalar": "Tarçın, Kakule, Lavanta"},
    {"ad": "Aventus", "marka": "Creed", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/156321_img-6298-creed-aventus_720.jpg", "notalar": "Ananas, Huş Ağacı, Misk"},
    {"ad": "Eros Parfum", "marka": "Versace", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155700_img-4171-versace-eros-parfum_720.jpg", "notalar": "Nane, Elma, Amber"},
    {"ad": "Layton", "marka": "PdM", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/80743_img-1965-parfums-de-marly-layton_720.jpg", "notalar": "Elma, Lavanta, Vanilya"},
    {"ad": "Stronger With You", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/118314_img-3424-emporio-armani-stronger-with-you-intensely_720.jpg", "notalar": "Karamel, Tarçın"},
    {"ad": "Le Male Elixir", "marka": "JPG", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/215758_37f394c86e088d8b671a5332c0276686_le_male_elixir.jpg", "notalar": "Lavanta, Bal, Tütün"},
    {"ad": "Bleu de Chanel", "marka": "Chanel", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/104323_img-4127-chanel-bleu-de-chanel-parfum_720.jpg", "notalar": "Limon, Sandal Ağacı"},
    {"ad": "Libre Intense", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/141873_img-9169-ysl-libre-eau-de-parfum-intense_720.jpg", "notalar": "Lavanta, Vanilya"},
    {"ad": "Good Girl", "marka": "C. Herrera", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/79361_img-6617-carolina-herrera-good-girl_720.jpg", "notalar": "Badem, Kahve, Kakao"},
    {"ad": "Baccarat Rouge 540", "marka": "MFK", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/63510_img-1313-maison-francis-kurkdjian-baccarat-rouge-540_720.jpg", "notalar": "Safran, Yasemin, Amber"},
    {"ad": "Naxos", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/52972_img-7546-xerjoff-1861-naxos_720.jpg", "notalar": "Bal, Tarçın, Tütün"},
    {"ad": "Angels' Share", "marka": "Kilian", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/144675_img-2821-by-kilian-angels-share_720.jpg", "notalar": "Konyak, Tarçın, Vanilya"},
    {"ad": "Oud Wood", "marka": "Tom Ford", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/1826_img-2101-tom-ford-private-blend-oud-wood-eau-de-parfum_720.jpg", "notalar": "Ud Ağacı, Sandal Ağacı"}
]

st.set_page_config(page_title="DEKANT VİTRİNİ")

# --- CSS ---
st.markdown("<style>.parfum-kart { background: white; border-radius: 20px; padding: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px; }</style>", unsafe_allow_html=True)

if 'secim' not in st.session_state: st.session_state.secim = None

# --- EKRANLAR ---
if st.session_state.secim is None:
    st.header("HOŞ GELDİNİZ")
    if st.button("👔 ERKEK"): st.session_state.secim = "Erkek"; st.rerun()
    if st.button("👗 KADIN"): st.session_state.secim = "Kadın"; st.rerun()
    if st.button("✨ UNİSEKS"): st.session_state.secim = "Uniseks"; st.rerun()
    st.stop()

st.button("⬅️ GERİ", on_click=lambda: setattr(st.session_state, 'secim', None))
filtreli = [p for p in envanter if p['tip'] == st.session_state.secim]

for p in filtreli:
    st.markdown(f'<div class="parfum-kart"><img src="{p["img"]}" style="width:100%; max-height:300px; object-fit:contain;"><h3>{p["ad"]}</h3><p>{p["notalar"]}</p></div>', unsafe_allow_html=True)
    ml = st.select_slider(f"Miktar ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
    st.button(f"{int(ml * p['fiyat'])} TL - SEPETE EKLE", use_container_width=True, disabled=True, key=f"btn_{p['ad']}")
