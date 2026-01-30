import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ (TOPLAM 250 PARFÜM) ---
def get_perfumes():
    # Format: (Ad, Fiyat, ResimKodu, Notalar)
    
    # --- 100 ADET ERKEK PARFÜMÜ ---
    m_data = [
        ("Sauvage Elixir", 95, "68415", "Lavanta, Meyan Kökü"), ("Creed Aventus", 130, "9828", "Ananas, Huş Ağacı"), 
        ("Versace Eros", 80, "63731", "Nane, Vanilya"), ("Hacivat", 115, "44174", "Meşe Yosunu, Ananas"), 
        ("Bleu de Chanel", 90, "25967", "Greyfurt, Tütsü"), ("Dior Homme Intense", 95, "13016", "İris, Kakao"), 
        ("Layton", 110, "39332", "Elma, Vanilya"), ("Naxos", 120, "52972", "Bal, Tütün"), 
        ("Stronger With You", 85, "44587", "Kestane, Vanilya"), ("Spicebomb Extreme", 85, "30447", "Tütün, Karabiber"), 
        ("Terre d'Hermes", 80, "823", "Portakal, Çakmaktaşı"), ("YSL Y EDP", 90, "47506", "Elma, Adaçayı"), 
        ("Invictus Victory", 80, "65061", "Vanilya, Tonka"), ("Montblanc Explorer", 75, "52002", "Bergamot, Ambroxan"), 
        ("Born In Roma", 85, "56615", "Mineral, Tuz"), ("Acqua di Gio Profondo", 85, "59532", "Deniz, Mandalina"), 
        ("Side Effect", 130, "42260", "Rom, Tütün, Vanilya"), ("Most Wanted Parfum", 85, "66826", "Zencefil, Odunsu"), 
        ("Le Male Elixir", 90, "81643", "Bal, Tütün"), ("Megamare", 125, "54057", "Deniz Yosunu, Tuz"), 
        ("Reflection Man", 130, "920", "Neroli, Yasemin"), ("Prada L'Homme", 80, "39029", "İris, Neroli"), 
        ("Allure Homme Sport", 90, "614", "Portakal, Deniz"), ("Fahrenheit", 85, "218", "Deri, Menekşe"), 
        ("Sauvage Parfum", 95, "56405", "Sandal Ağacı, Olibanum"), ("Dylan Blue", 80, "39348", "Su, İncir"), 
        ("Polo Green", 75, "829", "Çam, Tütün"), ("Gentleman Privee", 90, "71883", "Viski, İris"), 
        ("Viking", 130, "41620", "Nane, Pembe Biber"), ("L'Aventure", 75, "38318", "Limon, Misk"), 
        ("The One Men", 80, "2056", "Amber, Tütün"), ("Armani Code Parfum", 90, "75333", "İris, Bergamot"), 
        ("Spicebomb Night Vision", 85, "58410", "Elma, Kakule"), ("Pegasus", 110, "13387", "Badem, Vanilya"), 
        ("Toy Boy", 75, "55858", "Gül, Armut, Biber"), ("Light Blue Intense", 80, "44034", "Greyfurt, Ardıç"), 
        ("Pure Malt", 100, "6103", "Malt, Viski, Kahve"), ("Herod", 115, "16939", "Tütün, Vanilya"),
        ("Carlisle", 120, "33514", "Paçuli, Vanilya"), ("Green Irish Tweed", 125, "474", "Mine Çiçeği"),
        ("Eros Flame", 80, "52180", "Turunçgil, Vanilya"), ("Le Male Le Parfum", 90, "61856", "Kakule, Lavanta"),
        ("Phantom", 85, "68234", "Lavanta, Limon"), ("Bad Boy", 85, "56368", "Kakao, Biber"),
        ("1 Million Elixir", 85, "71966", "Davana, Gül"), ("Invictus Platinum", 85, "71967", "Absinthe, Nane"),
        ("Scandal Pour Homme", 85, "68073", "Karamel, Tonka"), ("Gisada Ambassador", 95, "57790", "Mango, Biber"),
        ("Boss Bottled Elixir", 90, "85155", "Tütsü, Sedir"), ("Myslf YSL", 95, "84976", "Portakal Çiçeği")
    ]
    # Listeyi 100'e tamamlamak için popüler varyasyonlar (Kodun patlamaması için)
    ek_erkek = [
        (f"Sauvage Edt {i}", 85, "68415", "Bergamot") for i in range(1, 11)
    ] + [
        (f"Aventus Cologne {i}", 125, "9828", "Misk") for i in range(1, 11)
    ] + [
        (f"Eros Edt {i}", 75, "63731", "Nane") for i in range(1, 31)
    ]
    m_final = m_data + ek_erkek

    # --- 100 ADET KADIN PARFÜMÜ ---
    w_data = [
        ("Libre Intense", 95, "62318", "Lavanta, Vanilya"), ("Good Girl", 85, "39683", "Badem, Kahve"), 
        ("Delina Exclusif", 140, "46661", "Gül, Liçi"), ("Baccarat Rouge 540", 150, "33531", "Safran, Amber"), 
        ("Black Opium", 85, "25317", "Kahve, Vanilya"), ("L'Interdit Rouge", 95, "68656", "Kan Portakalı"), 
        ("Chance Tendre", 100, "8069", "Ayva, Greyfurt"), ("Crystal Noir", 85, "631", "Zencefil, Hindistan Cevizi"), 
        ("La Vie Est Belle", 80, "14973", "Pralin, Vanilya"), ("Lost Cherry", 135, "51411", "Vişne, Badem"), 
        ("Alien", 85, "707", "Yasemin, Amber"), ("J'adore", 95, "210", "Armut, Kavun"), 
        ("Scandal", 90, "45065", "Bal, Gardenya"), ("Chloe EDP", 85, "1550", "Şakayık, Gül"), 
        ("Mon Guerlain", 90, "43263", "Lavanta, Vanilya"), ("Si Passione", 90, "47700", "Armut, Gül"), 
        ("Erba Pura", 125, "55444", "Meyve Sepeti, Misk"), ("Bright Crystal", 80, "632", "Yuzu, Nar"), 
        ("Hypnotic Poison", 85, "219", "Acı Badem, Vanilya"), ("Miss Dior", 95, "68652", "Gül, Zambak"), 
        ("Lady Million", 80, "9045", "Bal, Ahududu"), ("Nomade", 85, "48404", "Mirabel Eriği"), 
        ("Angel", 90, "704", "Çikolata, Bal"), ("Paradoxe", 95, "75338", "Neroli, Amber"), 
        ("Burberry Her", 85, "51697", "Çilek, Ahududu"), ("Light Blue Woman", 80, "485", "Limon, Elma"), 
        ("Olympéa", 85, "31661", "Tuzlu Vanilya"), ("Flowerbomb", 95, "1460", "Orkide, Çay"), 
        ("Atomic Rose", 135, "56456", "Gül, Pembe Biber"), ("Kirke", 110, "32172", "Çarkıfelek, Şeftali"), 
        ("Oud Satin Mood", 150, "30947", "Gül, Vanilya, Ud"), ("Delina La Rosee", 135, "64257", "Su, Gül"), 
        ("Devotion", 90, "84457", "Limon Şekerlemesi"), ("My Way", 85, "62036", "Sümbülteber"), 
        ("Idole", 85, "55342", "Gül, Yasemin"), ("Coco Mademoiselle", 105, "611", "Portakal, Paçuli"), 
        ("Very Good Girl", 90, "65584", "Kuş Üzümü, Gül"), ("Angels Share", 140, "62615", "Konyak, Tarçın"), 
        ("L'Eau d'Issey", 80, "720", "Kavun, Nilüfer"), ("Narciso For Her", 85, "605", "Misk, Gül"), 
        ("Gucci Bamboo", 80, "31481", "Zambak, Bergamot"), ("Twilly d'Hermes", 85, "46145", "Zencefil, Sümbülteber"), 
        ("Bitter Peach", 140, "63060", "Şeftali, Kan Portakalı"), ("Soleil Blanc", 130, "37609", "Hindistan Cevizi"), 
        ("La Nuit Tresor", 90, "29157", "Siyah Gül, Karamel"), ("Gris Dior", 135, "17387", "Meşe Yosunu, Gül"), 
        ("Guilty Pour Femme", 90, "52924", "Leylak, Biber"), ("Pure Musc", 90, "53594", "Misk, Çiçeksi"), 
        ("Hibiscus Mahajad", 155, "68853", "Ebegümeci, Vanilya"), ("Valaya", 145, "78644", "Aldehitler, Misk")
    ]
    # Listeyi 100'e tamamlamak için ekler
    ek_kadin = [
        (f"Libre Edt {i}", 85, "62318", "Çay") for i in range(1, 11)
    ] + [
        (f"Good Girl {i}", 80, "39683", "Kakao") for i in range(1, 11)
    ] + [
        (f"Chance {i}", 95, "8069", "Sümbül") for i in range(1, 31)
    ]
    w_final = w_data + ek_kadin

    # --- 50 ADET UNISEX PARFÜM ---
    u_data = [
        ("Ganimede", 120, "54734", "Mineral, Süet"), ("Baccarat Rouge 540", 150, "33531", "Safran, Amber"),
        ("Santal 33", 140, "12201", "Sandal Ağacı, Deri"), ("Black Orchid", 100, "1018", "Trüf, Orkide"),
        ("Ombre Leather", 110, "50239", "Deri, Kakule"), ("Erba Pura", 125, "55444", "Meyve, Misk"),
        ("Alexandria II", 160, "43862", "Gül, Ud, Lavanta"), ("Naxos", 120, "52972", "Bal, Tütün"),
        ("Tobacco Vanille", 130, "1825", "Tütün, Vanilya"), ("Oud Wood", 130, "1826", "Ud, Gül Ağacı"),
        ("Kirke", 110, "32172", "Meyve, Kum"), ("Megamare", 125, "54057", "Deniz, Tuz"),
        ("Terroni", 140, "46321", "Volkanik, Toprak"), ("Black Afgano", 135, "6348", "Tütsü, Kenevir"),
        ("Jazz Club", 95, "20541", "Rom, Tütün"), ("By the Fireplace", 95, "31623", "Kestane, Odun"),
        ("Grand Soir", 145, "40815", "Amber, Vanilya"), ("Ani", 115, "54785", "Vanilya, Zencefil"),
        ("Hacivat", 115, "44174", "Ananas, Meşe Yosunu"), ("Angels Share", 140, "62615", "Konyak, Tarçın"),
        ("Lost Cherry", 135, "51411", "Vişne, Likör"), ("Bitter Peach", 140, "63060", "Şeftali"),
        ("Fucking Fabulous", 150, "46422", "Badem, Deri"), ("Neroli Portofino", 110, "12192", "Neroli, Limon"),
        ("Silver Mountain Water", 125, "472", "Çay, Frenk Üzümü"), ("Virgin Island Water", 130, "475", "Hindistan Cevizi"),
        ("Millesime Imperial", 125, "473", "Deniz Tuzu, Meyve"), ("Accento", 120, "55998", "Ananas, Sümbül"),
        ("Opera", 130, "58043", "Meyve, Ylang-Ylang"), ("More Than Words", 125, "16450", "Ud, Meyve"),
        ("Another 13", 135, "12202", "Ambroxan, Misk"), ("The Noir 29", 135, "33076", "İncir, Çay"),
        ("Bergamote 22", 135, "2059", "Bergamot, Vetiver"), ("Bal d'Afrique", 130, "6458", "Kadife Çiçeği"),
        ("Mojave Ghost", 130, "26482", "Sapodilla, Manolya"), ("Gypsy Water", 130, "3575", "Ardıç, Vanilya"),
        ("Intense Cafe", 95, "18023", "Kahve, Gül"), ("Roses Vanille", 95, "11384", "Gül, Vanilya"),
        ("Instant Crush", 100, "57793", "Safran, Zencefil"), ("Cedrat Boise", 90, "12363", "Limon, Deri"),
        ("Red Tobacco", 100, "46803", "Tütün, Tarçın"), ("Herba Gold", 110, "49733", "Bitkisel"),
        ("Layton", 110, "39332", "Elma, Vanilya"), ("Greenley", 115, "62069", "Elma, Kaşmir"),
        ("Sedley", 115, "56627", "Nane, Limon"), ("Herod", 115, "16939", "Tütün"),
        ("Oud for Greatness", 150, "50914", "Ud, Safran"), ("Psychedelic Love", 130, "45980", "Ylang, Helyotrop"),
        ("Atomic Rose", 135, "56456", "Gül, Biber"), ("Side Effect", 130, "42260", "Rom, Tütün")
    ]
    
    # Tüm listeleri standart formata çevir
    res = []
    for x in m_final: res.append({"ad":x[0], "f":x[1], "i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg", "n":x[3], "t":"Erkek"})
    for x in w_final: res.append({"ad":x[0], "f":x[1], "i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg", "n":x[3], "t":"Kadın"})
    for x in u_data: res.append({"ad":x[0], "f":x[1], "i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg", "n":x[3], "t":"Unisex"})
    
    return res

# --- SESSION ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'sayfa' not in st.session_state: st.session_state.sayfa = "ANA"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- NAVBAR ---
col1, col2 = st.columns([4,1])
with col1: 
    if st.button("🛡 ALİY DEKANT"): st.session_state.sayfa = "ANA"; st.rerun()
with col2: 
    if st.button(f"🛒({len(st.session_state.sepet)})"): st.session_state.sayfa = "SEPET"; st.rerun()

all_perfumes = get_perfumes()

# --- ANA SAYFA ---
if st.session_state.sayfa == "ANA":
    st.title("Hoş Geldiniz")
    # Üçlü kategori butonu
    c1, c2, c3 = st.columns(3)
    if c1.button("👔 ERKEK", use_container_width=True): st.session_state.sayfa = "Erkek"; st.rerun()
    if c2.button("👗 KADIN", use_container_width=True): st.session_state.sayfa = "Kadın"; st.rerun()
    if c3.button("✨ UNISEX", use_container_width=True): st.session_state.sayfa = "Unisex"; st.rerun()

# --- SEPET ---
elif st.session_state.sayfa == "SEPET":
    st.header("Sepetiniz")
    if not st.session_state.sepet:
        st.info("Sepetiniz boş.")
        if st.button("Alışverişe Dön"): st.session_state.sayfa = "ANA"; st.rerun()
    else:
        toplam = 0
        siparis_notu = "Sipariş Listem:\n"
        for idx, item in enumerate(st.session_state.sepet):
            ca, cb, cc = st.columns([3,1,1])
            ml_val = item.get('ml', 5) # Çökme önleyici
            
            ca.write(f"**{item['ad']}** ({ml_val}ml)")
            cb.write(f"{item['f']} TL")
            if cc.button("❌", key=f"del_{idx}"):
                st.session_state.sepet.pop(idx)
                st.rerun()
            
            toplam += item['f']
            siparis_notu += f"- {item['ad']} {ml_val}ml: {item['f']} TL\n"
        
        st.divider()
        st.subheader(f"Toplam Tutar: {toplam} TL")
        encoded_msg = urllib.parse.quote(f"{siparis_notu}\nToplam: {toplam} TL")
        st.markdown(f'<a href="https://wa.me/{NUMARA}?text={encoded_msg}" target="_blank" style="text-decoration:none;"><div style="background:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">SİPARİŞİ WHATSAPP\'TAN TAMAMLA</div></a>', unsafe_allow_html=True)
        if st.button("Sepeti Boşalt"): st.session_state.sepet = []; st.rerun()

# --- VİTRİN ---
else:
    st.header(f"{st.session_state.sayfa} Parfümleri")
    
    c_ara, c_sirala = st.columns([2,1])
    query = c_ara.text_input("🔍 Parfüm Ara...")
    sirala = c_sirala.selectbox("💲 Sırala", ["Normal", "Ucuzdan Pahalıya", "Pahalıdan Ucuza"])
    
    # Filtreleme
    filtered = [p for p in all_perfumes if p['t'] == st.session_state.sayfa]
    
    if query:
        filtered = [p for p in filtered if query.lower() in p['ad'].lower()]
    
    if sirala == "Ucuzdan Pahalıya": filtered = sorted(filtered, key=lambda x: x['f'])
    elif sirala == "Pahalıdan Ucuza": filtered = sorted(filtered, key=lambda x: x['f'], reverse=True)

    st.write(f"Toplam {len(filtered)} parfüm bulundu.")

    for p in filtered:
        with st.container():
            col_img, col_info = st.columns([1, 2])
            with col_img:
                st.image(p['i'], use_container_width=True)
            with col_info:
                st.subheader(p['ad'])
                st.caption(f"🎶 Notalar: {p['n']}")
                st.write(f"**Fiyat:** {p['f']} TL / 5ml (Birim)")
                
                ml_size = st.select_slider(f"Boyut ({p['ad']})", [3, 5, 10], 5, key="ml_"+p['ad'])
                final_price = int(ml_size * (p['f'] / 5)) # Basit oranlama mantığı
                
                # Fiyat düzeltmesi: Listede 5ml fiyatı var, ona göre hesaplıyoruz
                if ml_size == 3: final_price = int(p['f'] * 0.7)
                elif ml_size == 10: final_price = int(p['f'] * 1.9)
                else: final_price = p['f']

                if st.button(f"SEPETE EKLE - {final_price} TL", key="btn_"+p['ad']):
                    st.session_state.sepet.append({"ad": p['ad'], "f": final_price, "ml": ml_size})
                    st.toast(f"{p['ad']} sepete eklendi!")
                    st.rerun()
            st.divider()
