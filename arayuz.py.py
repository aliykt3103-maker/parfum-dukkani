import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- DEV ENVANTER (45 PARFÜM) ---
envanter = [
    # --- ERKEK (15 ADET) ---
    {"ad": "Sauvage Elixir", "marka": "Dior", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155355_img-9714-dior-sauvage-elixir_720.jpg", "notalar": "Tarçın, Kakule, Lavanta"},
    {"ad": "Aventus", "marka": "Creed", "fiyat": 100, "tip": "Erkek", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Huş Ağacı, Misk"},
    {"ad": "Eros Parfum", "marka": "Versace", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155700_img-4171-versace-eros-parfum_720.jpg", "notalar": "Nane, Elma, Kehribar"},
    {"ad": "Layton", "marka": "PdM", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/80743_img-1965-parfums-de-marly-layton_720.jpg", "notalar": "Elma, Lavanta, Vanilya"},
    {"ad": "Le Male Elixir", "marka": "JPG", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/215758_le_male_elixir.jpg", "notalar": "Bal, Tütün, Lavanta"},
    {"ad": "Stronger With You", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/118314_stronger_with_you.jpg", "notalar": "Kestane, Adaçayı, Vanilya"},
    {"ad": "Bleu de Chanel", "marka": "Chanel", "fiyat": 80, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/104323_bleu_de_chanel.jpg", "notalar": "Sandal Ağacı, Sedir, Greyfurt"},
    {"ad": "Spicebomb Extreme", "marka": "V&R", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/54655_spicebomb.jpg", "notalar": "Tütün, Vanilya, Karabiber"},
    {"ad": "Acqua di Gio", "marka": "Armani", "fiyat": 70, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/47699_acqua_di_gio.jpg", "notalar": "Deniz Notaları, Biberiye"},
    {"ad": "Prada L'Homme", "marka": "Prada", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/73385_prada.jpg", "notalar": "İris, Neroli, Sardunya"},
    {"ad": "Terre d'Hermes", "marka": "Hermes", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/823_terre.jpg", "notalar": "Portakal, Çakmaktaşı, Sedir"},
    {"ad": "The Most Wanted", "marka": "Azzaro", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/151603_wanted.jpg", "notalar": "Kakule, Karamel, Amberwood"},
    {"ad": "Y EDP", "marka": "YSL", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/103975_ysl_y.jpg", "notalar": "Zencefil, Elma, Adaçayı"},
    {"ad": "L'Aventure", "marka": "Al Haramain", "fiyat": 60, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/71871_laventure.jpg", "notalar": "Limon, Bergamot, Yasemin"},
    {"ad": "Gentleman Privee", "marka": "Givenchy", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/165561_gentleman.jpg", "notalar": "Viski, Kestane, İris"},

    # --- KADIN (15 ADET) ---
    {"ad": "Libre Intense", "marka": "YSL", "fiyat": 80, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/141873_libre.jpg", "notalar": "Lavanta, Portakal Çiçeği, Vanilya"},
    {"ad": "Good Girl", "marka": "C. Herrera", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/79361_good_girl.jpg", "notalar": "Badem, Kahve, Yasemin"},
    {"ad": "Delina Exclusif", "marka": "PdM", "fiyat": 110, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/103328_delina.jpg", "notalar": "Gül, Liçi, Armut, Tütsü"},
    {"ad": "Black Opium", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/43734_black_opium.jpg", "notalar": "Kahve, Vanilya, Beyaz Çiçekler"},
    {"ad": "Alien", "marka": "Mugler", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/707_alien.jpg", "notalar": "Yasemin, Amber, Kaşmir"},
    {"ad": "J'adore", "marka": "Dior", "fiyat": 80, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/210_jadore.jpg", "notalar": "Armut, Kavun, Yasemin"},
    {"ad": "Crystal Noir", "marka": "Versace", "fiyat": 70, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/631_crystal.jpg", "notalar": "Hindistan Cevizi, Biber, Gardenya"},
    {"ad": "La Vie Est Belle", "marka": "Lancome", "fiyat": 70, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/14973_lavie.jpg", "notalar": "Pralin, Vanilya, İris"},
    {"ad": "Hypnotic Poison", "marka": "Dior", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/219_hypnotic.jpg", "notalar": "Acı Badem, Kimyon, Vanilya"},
    {"ad": "L'Interdit Rouge", "marka": "Givenchy", "fiyat": 80, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/155694_interdit.jpg", "notalar": "Kan Portakalı, Zencefil, Sümbülteber"},
    {"ad": "Idole", "marka": "Lancome", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/124707_idole.jpg", "notalar": "Gül, Yasemin, Beyaz Misk"},
    {"ad": "Chloe EDP", "marka": "Chloe", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/1550_chloe.jpg", "notalar": "Şakayık, Gül, Manolya"},
    {"ad": "Burberry Her", "marka": "Burberry", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/109001_her.jpg", "notalar": "Çilek, Ahududu, Böğürtlen"},
    {"ad": "Baccarat Rouge (K)", "marka": "MFK", "fiyat": 100, "tip": "Kadın", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "notalar": "Safran, Yasemin, Amber"},
    {"ad": "Coco Mademoiselle", "marka": "Chanel", "fiyat": 85, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/611_coco.jpg", "notalar": "Portakal, Gül, Paçuli"},

    # --- UNİSEKS / NİŞ (15 ADET) ---
    {"ad": "Naxos", "marka": "Xerjoff", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/52972_naxos.jpg", "notalar": "Bal, Tütün, Lavanta, Tarçın"},
    {"ad": "Angels' Share", "marka": "Kilian", "fiyat": 110, "tip": "Uniseks", "img": "https://fimgs.net/mdimg/perfume/m.62615.jpg", "notalar": "Konyak, Tarçın, Meşe, Vanilya"},
    {"ad": "Hacivat", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/97792_hacivat.jpg", "notalar": "Ananas, Greyfurt, Meşe Yosunu"},
    {"ad": "Ani", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/121113_ani.jpg", "notalar": "Vanilya, Zencefil, Bergamot"},
    {"ad": "Erba Pura", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/121285_erba.jpg", "notalar": "Meyve Notaları, Beyaz Misk, Kehribar"},
    {"ad": "Tobacco Vanille", "marka": "Tom Ford", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/1825_tobacco.jpg", "notalar": "Tütün, Vanilya, Baharatlar"},
    {"ad": "Oud Wood", "marka": "Tom Ford", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/1826_oud.jpg", "notalar": "Ud, Kakule, Sandal Ağacı"},
    {"ad": "Ganimede", "marka": "M.A. Barrois", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/120935_ganymede.jpg", "notalar": "Mandalina, Safran, Süet"},
    {"ad": "Side Effect", "marka": "Initio", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/82405_side.jpg", "notalar": "Rom, Tütün, Tarçın"},
    {"ad": "Lost Cherry", "marka": "Tom Ford", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/111823_cherry.jpg", "notalar": "Vişne, Acı Badem, Likör"},
    {"ad": "Ombre Nomade", "marka": "LV", "fiyat": 120, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/105437_nomade.jpg", "notalar": "Oud, Ahududu, Tütsü"},
    {"ad": "Black Phantom", "marka": "Kilian", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/86121_phantom.jpg", "notalar": "Çikolata, Kahve, Karamel"},
    {"ad": "Alexandria II", "marka": "Xerjoff", "fiyat": 120, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/43862_alex.jpg", "notalar": "Elma, Lavanta, Oud, Tarçın"},
    {"ad": "Silver Mountain", "marka": "Creed", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/9830_silver.jpg", "notalar": "Yeşil Çay, Siyah Frenk Üzümü, Misk"},
    {"ad": "Portrait of a Lady", "marka": "F. Malle", "fiyat": 110, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/10464_portrait.jpg", "notalar": "Gül, Tütsü, Karanfil, Paçuli"}
]

st.set_page_config(page_title="DEKANT VİTRİNİ", layout="centered")

# --- TASARIM ---
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    .parfum-kart { 
        background: white; 
        border: 1px solid #f0f0f0; 
        border-radius: 20px; 
        padding: 20px; 
        text-align: center; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .notalar { color: #d32f2f; font-size: 13px; font-weight: 600; background: #fff5f5; padding: 8px; border-radius: 10px; margin: 10px 0; }
    img { border-radius: 15px; margin-bottom: 10px; }
    .fiyat-tag { color: #111; font-size: 18px; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

if 'secim' not in st.session_state:
    st.session_state.secim = None

# --- MENÜ ---
if st.session_state.secim is None:
    st.title("⭐️ ALİY DEKANT")
    st.write("Hoş geldiniz, vitrin seçerek keşfetmeye başlayın.")
    if st.button("👔 ERKEK KOLEKSİYONU", use_container_width=True): st.session_state.secim = "Erkek"; st.rerun()
    if st.button("👗 KADIN KOLEKSİYONU", use_container_width=True): st.session_state.secim = "Kadın"; st.rerun()
    if st.button("✨ NİŞ & UNİSEKS", use_container_width=True): st.session_state.secim = "Uniseks"; st.rerun()
    st.stop()

st.button("⬅️ ANA MENÜYE DÖN", on_click=lambda: setattr(st.session_state, 'secim', None))

# --- LİSTELEME ---
filtreli = [p for p in envanter if p['tip'] == st.session_state.secim]

for p in filtreli:
    with st.container():
        st.markdown(f'''
        <div class="parfum-kart">
            <p style="color:#999; font-size:12px; text-transform:uppercase;">{p["marka"]}</p>
            <img src="{p["img"]}" width="100%" style="max-height:300px; object-fit:contain;">
            <h2 style="margin:5px 0;">{p["ad"]}</h2>
            <div class="notalar">KOKU PİRAMİDİ: {p["notalar"]}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        ml = st.select_slider(f"Boyut Seç ({p['ad']})", options=[3, 5, 10], key=f"ml_{p['ad']}")
        toplam = int(ml * p['fiyat'])
        st.button(f"{toplam} TL - SİPARİŞ VER (WhatsApp)", use_container_width=True, disabled=True, key=f"btn_{p['ad']}")
        st.write("---")
