import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ (100 ADET) ---
def get_perfumes():
    m_raw = [
        ("Sauvage Elixir", 95, "68415", "Lavanta"), ("Aventus", 130, "9828", "Ananas"), ("Eros Parfum", 80, "63731", "Nane"),
        ("Hacivat", 115, "44174", "Meşe"), ("Ganimede", 120, "54734", "Safran"), ("Bleu Chanel", 90, "25967", "Tütsü"),
        ("Dior Homme Int", 95, "13016", "İris"), ("Layton", 110, "39332", "Elma"), ("Naxos", 120, "52972", "Bal"),
        ("SWY Intense", 85, "44587", "Kestane"), ("Spicebomb Ext", 85, "30447", "Tütün"), ("Terre Hermes", 80, "823", "Sedir"),
        ("Oud Wood", 130, "1826", "Ud"), ("YSL Y EDP", 90, "47506", "Adaçayı"), ("Invictus Vict", 80, "65061", "Vanilya"),
        ("Explorer", 75, "52002", "Bergamot"), ("Born In Roma", 85, "56615", "Tuz"), ("Gio Profondo", 85, "59532", "Deniz"),
        ("Bleecker St", 115, "1444", "Yosun"), ("Side Effect", 130, "42260", "Rom"), ("Most Wanted", 85, "66826", "Karamel"),
        ("Ombre Nomade", 150, "49751", "Oud"), ("Ani Nishane", 115, "54785", "Vanilya"), ("Luna Rossa", 80, "43402", "Kömür"),
        ("Le Male Elixir", 90, "81643", "Bal"), ("Tobacco Vanille", 130, "1825", "Tütün"), ("Megamare", 125, "54057", "Deniz"),
        ("Reflection", 130, "920", "Neroli"), ("Prada Amber", 85, "834", "Deri"), ("Allure Sport", 90, "614", "Deniz"),
        ("Wood Sage", 100, "27044", "Adaçayı"), ("Fahrenheit", 85, "218", "Deri"), ("Santal 33", 140, "12201", "Sandal"),
        ("Black Phantom", 145, "43632", "Kahve"), ("Sauvage Parfum", 95, "56405", "Sandal"), ("Dylan Blue", 80, "39348", "İncir"),
        ("Polo Green", 75, "829", "Çam"), ("Jazz Club", 95, "20541", "Rom"), ("By Fireplace", 95, "31623", "Kestane"),
        ("Silver Mountain", 125, "472", "Çay"), ("Gentleman Priv", 90, "71883", "Viski"), ("Viking", 130, "41620", "Nane"),
        ("L'Aventure", 75, "38318", "Limon"), ("The One Men", 80, "2056", "Tütün"), ("Code Parfum", 90, "75333", "İris"),
        ("Night Vision", 85, "58410", "Elma"), ("Pegasus", 110, "13387", "Badem"), ("Toy Boy", 75, "55858", "Gül"),
        ("Light Blue Int", 80, "44034", "Greyfurt"), ("Pure Malt", 100, "6103", "Malt")
    ]
    w_raw = [
        ("Libre Intense", 95, "62318", "Lavanta"), ("Good Girl", 85, "39683", "Kahve"), ("Delina Excl", 140, "46661", "Gül"),
        ("Baccarat 540", 150, "33531", "Safran"), ("Black Opium", 85, "25317", "Kahve"), ("L'Interdit", 95, "68656", "Üzüm"),
        ("Chance Tendre", 100, "8069", "Ayva"), ("Crystal Noir", 85, "631", "Amber"), ("Vie Est Belle", 80, "14973", "Şeker"),
        ("Lost Cherry", 135, "51411", "Vişne"), ("Alien", 85, "707", "Yasemin"), ("J'adore", 95, "210", "Armut"),
        ("Scandal", 90, "45065", "Bal"), ("Chloe EDP", 85, "1550", "Gül"), ("Mon Guerlain", 90, "43263", "Lavanta"),
        ("Si Passione", 90, "47700", "Gül"), ("Erba Pura", 125, "55444", "Meyve"), ("Bright Crystal", 80, "632", "Yuzu"),
        ("Hypnotic Poison", 85, "219", "Badem"), ("Miss Dior", 95, "68652", "Gül"), ("Lady Million", 80, "9045", "Bal"),
        ("Nomade", 85, "48404", "Erik"), ("Angel", 90, "704", "Çikolata"), ("Paradoxe", 95, "75338", "Neroli"),
        ("Burberry Her", 85, "51697", "Çilek"), ("Light Blue W", 80, "485", "Limon"), ("Olympéa", 85, "31661", "Tuz"),
        ("Flowerbomb", 95, "1460", "Orkide"), ("Baccarat Ext", 175, "46066", "Safran"), ("Atomic Rose", 135, "56456", "Gül"),
        ("Kirke", 110, "32172", "Meyve"), ("Satin Mood", 150, "30947", "Gül"), ("Delina Rosee", 135, "64257", "Şakayık"),
        ("Devotion", 90, "84457", "Limon"), ("My Way", 85, "62036", "Çiçek"), ("Idole", 85, "55342", "Gül"),
        ("Mademoiselle", 105, "611", "Gül"), ("Very Good Girl", 90, "65584", "Gül"), ("Angels Share", 140, "62615", "Tarçın"),
        ("Eau d'Issey", 80, "720", "Nilüfer"), ("Narciso Her", 85, "605", "Misk"), ("Gucci Bamboo", 80, "31481", "Zambak"),
        ("Twilly", 85, "46145", "Zencefil"), ("Bitter Peach", 140, "63060", "Şeftali"), ("Soleil Blanc", 130, "37609", "Hindistan"),
        ("Nuit Tresor", 90, "29157", "Karamel"), ("Gris Dior", 135, "17387", "Gül"), ("Guilty W", 90, "52924", "Leylak"),
        ("Pure Musc", 90, "53594", "Misk"), ("Hibiscus", 155, "68853", "Vanilya")
    ]
    res = []
    for x in m_raw: res.append({"ad":x[0],"f":x[1],"i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg","n":x[3],"t":"Erkek"})
    for x in w_raw: res.append({"ad":x[0],"f":x[1],"i":f"https://fimgs.net/mdimg/perfume/m.{x[2]}.jpg","n":x[3],"t":"Kadın"})
    return res

# --- SESSION ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'sayfa' not in st.session_state: st.session_state.sayfa = "ANA"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- NAVBAR ---
c_nav1, c_nav2 = st.columns([4,1])
with c_nav1: 
    if st.button("🛡 ALİY DEKANT"): st.session_state.sayfa = "ANA"; st.rerun()
with c_nav2: 
    if st.button(f"🛒({len(st.session_state.sepet)})"): st.session_state.sayfa = "SEPET"; st.rerun()

all_perfumes = get_perfumes()

# --- ANA SAYFA ---
if st.session_state.sayfa == "ANA":
    st.title("Hoş Geldiniz")
    cA, cB = st.columns(2)
    if cA.button("👔 ERKEK KOLEKSİYONU", use_container_width=True): st.session_state.sayfa = "Erkek"; st.rerun()
    if cB.button("👗 KADIN KOLEKSİYONU", use_container_width=True): st.session_state.sayfa = "Kadın"; st.rerun()

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
            col_a, col_b, col_c = st.columns([3,1,1])
            col_a.write(f"**{item['ad']}** ({item['ml']}ml)")
            col_b.write(f"{item['f']} TL")
            if col_c.button("❌", key=f"del_{idx}"):
                st.session_state.sepet.pop(idx)
                st.rerun()
            toplam += item['f']
            siparis_notu += f"- {item['ad']} {item['ml']}ml: {item['f']} TL\n"
        
        st.divider()
        st.subheader(f"Toplam Tutar: {toplam} TL")
        encoded_msg = urllib.parse.quote(f"{siparis_notu}\nToplam: {toplam} TL")
        st.markdown(f'<a href="https://wa.me/{NUMARA}?text={encoded_msg}" target="_blank" style="text-decoration:none;"><div style="background:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">SİPARİŞİ WHATSAPP\'TAN TAMAMLA</div></a>', unsafe_allow_html=True)
        if st.button("Sepeti Boşalt"): st.session_state.sepet = []; st.rerun()

# --- VİTRİN ---
else:
    st.header(f"{st.session_state.sayfa} Parfümleri")
    
    col_ara, col_sirala = st.columns([2,1])
    query = col_ara.text_input("🔍 Parfüm Ara...")
    sirala = col_sirala.selectbox("💲 Fiyat Sırala", ["Varsayılan", "Artan", "Azalan"])
    
    filtered = [p for p in all_perfumes if p['t'] == st.session_state.sayfa]
    if query:
        filtered = [p for p in filtered if query.lower() in p['ad'].lower()]
    
    if sirala == "Artan": filtered = sorted(filtered, key=lambda x: x['f'])
    elif sirala == "Azalan": filtered = sorted(filtered, key=lambda x: x['f'], reverse=True)

    for p in filtered:
        with st.container():
            # Hatalı olan tırnak yapısını sildik, yerine Streamlit'in kendi görsel araçlarını koyduk
            st.image(p['i'], width=150)
            st.subheader(p['ad'])
            st.caption(f"Nota: {p['n']}")
            
            ml_size = st.select_slider(f"Boyut ({p['ad']})", [3, 5, 10], 5, key="ml_"+p['ad'])
            final_price = int(ml_size * p['f'])
            
            if st.button(f"EKLE - {final_price} TL", key="btn_"+p['ad'], use_container_width=True):
                st.session_state.sepet.append({"ad": p['ad'], "f": final_price, "ml": ml_size})
                st.toast(f"{p['ad']} eklendi!")
                st.rerun()
            st.divider()
