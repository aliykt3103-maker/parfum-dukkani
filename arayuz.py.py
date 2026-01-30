import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ (HATAYI ÖNLEMEK İÇİN SIKIŞTIRILMIŞ YAPI) ---
def get_perfumes():
    # ERKEK PARFÜMLERİ (50 ADET)
    m = [
        ("Sauvage Elixir", 95, "🟦 BLUE", "68415", "Lavanta"), ("Aventus", 130, "🌬 FRESH", "9828", "Ananas"),
        ("Eros Parfum", 80, "🟥 RED", "63731", "Nane"), ("Hacivat", 115, "🟩 GREEN", "44174", "Ananas"),
        ("Ganimede", 120, "✨ MYSTERY", "54734", "Safran"), ("Bleu Chanel", 90, "🟦 BLUE", "25967", "Tütsü"),
        ("Dior Homme Int", 95, "✨ MYSTERY", "13016", "İris"), ("Layton", 110, "🟥 RED", "39332", "Elma"),
        ("Xerjoff Naxos", 120, "🍯 GOURMAND", "52972", "Tütün"), ("SWY Intense", 85, "🟥 RED", "44587", "Kestane"),
        ("Spicebomb Ext", 85, "🟥 RED", "30447", "Tütün"), ("Terre Hermes", 80, "🟩 GREEN", "823", "Sedir"),
        ("Oud Wood", 130, "✨ MYSTERY", "1826", "Ud"), ("YSL Y EDP", 90, "🟦 BLUE", "47506", "Adaçayı"),
        ("Invictus Vict", 80, "🟥 RED", "65061", "Vanilya"), ("Explorer", 75, "🟦 BLUE", "52002", "Bergamot"),
        ("Born In Roma", 85, "🌬 FRESH", "56615", "Tuz"), ("Gio Profondo", 85, "🟦 BLUE", "59532", "Deniz"),
        ("Bleecker St", 115, "🟩 GREEN", "1444", "Yaban Mersini"), ("Side Effect", 130, "🟥 RED", "42260", "Rom"),
        ("Most Wanted", 85, "🍯 GOURMAND", "66826", "Karamel"), ("Ombre Nomade", 150, "✨ MYSTERY", "49751", "Oud"),
        ("Ani Nishane", 115, "🍯 GOURMAND", "54785", "Zencefil"), ("Luna Rossa", 80, "🟦 BLUE", "43402", "Lavanta"),
        ("Le Male Elixir", 90, "🍯 GOURMAND", "81643", "Bal"), ("Tobacco Vanille", 130, "🍯 GOURMAND", "1825", "Vanilya"),
        ("Megamare", 125, "🟦 BLUE", "54057", "Tuz"), ("Reflection", 130, "🌬 FRESH", "920", "Yasemin"),
        ("Prada Amber", 85, "✨ MYSTERY", "834", "Deri"), ("Allure Sport", 90, "🌬 FRESH", "614", "Deniz"),
        ("Wood Sage", 100, "🌬 FRESH", "27044", "Tuz"), ("Fahrenheit", 85, "🟥 RED", "218", "Deri"),
        ("Santal 33", 140, "🟩 GREEN", "12201", "Sandal"), ("Black Phantom", 145, "🍯 GOURMAND", "43632", "Kahve"),
        ("Sauvage Parfum", 95, "🟦 BLUE", "56405", "Sandal"), ("Dylan Blue", 80, "🟦 BLUE", "39348", "İncir"),
        ("Polo Green", 75, "🟩 GREEN", "829", "Çam"), ("Jazz Club", 95, "🍯 GOURMAND", "20541", "Rom"),
        ("By Fireplace", 95, "🟥 RED", "31623", "Kestane"), ("Silver Mountain", 125, "🌬 FRESH", "472", "Yeşil Çay"),
        ("Gentleman Priv", 90, "✨ MYSTERY", "71883", "Viski"), ("Viking", 130, "🌬 FRESH", "41620", "Nane"),
        ("L'Aventure", 75, "🌬 FRESH", "38318", "Limon"), ("The One", 80, "✨ MYSTERY", "2056", "Tütün"),
        ("Code Parfum", 90, "🟦 BLUE", "75333", "İris"), ("Night Vision", 85, "🟩 GREEN", "58410", "Elma"),
        ("Pegasus", 110, "🍯 GOURMAND", "13387", "Badem"), ("Toy Boy", 75, "🌸 FLORAL", "55858", "Gül"),
        ("Light Blue Int", 80, "🟦 BLUE", "44034", "Greyfurt"), ("Pure Malt", 100, "🍯 GOURMAND", "6103", "Viski")
    ]
    # KADIN PARFÜMLERİ (50 ADET)
    w = [
        ("Libre Intense", 95, "🌸 FLORAL", "62318", "Vanilya"), ("Good Girl", 85, "🍯 GOURMAND", "39683", "Kahve"),
        ("Delina Excl", 140, "🌸 FLORAL", "46661", "Gül"), ("Baccarat 540", 150, "✨ MYSTERY", "33531", "Safran"),
        ("Black Opium", 85, "🍯 GOURMAND", "25317", "Kahve"), ("L'Interdit", 95, "🟥 RED", "68656", "Zencefil"),
        ("Chance Tendre", 100, "🌬 FRESH", "8069", "Ayva"), ("Crystal Noir", 85, "✨ MYSTERY", "631", "Amber"),
        ("Vie Est Belle", 80, "🍯 GOURMAND", "14973", "Pralin"), ("Lost Cherry", 135, "🍯 GOURMAND", "51411", "Vişne"),
        ("Alien", 85, "✨ MYSTERY", "707", "Yasemin"), ("J'adore", 95, "🌸 FLORAL", "210", "Armut"),
        ("Scandal", 90, "🍯 GOURMAND", "45065", "Bal"), ("Chloe EDP", 85, "🌬 FRESH", "1550", "Gül"),
        ("Mon Guerlain", 90, "🌸 FLORAL", "43263", "Lavanta"), ("Si Passione", 90, "🟥 RED", "47700", "Armut"),
        ("Erba Pura", 125, "🌬 FRESH", "55444", "Meyve"), ("Bright Crystal", 80, "🌸 FLORAL", "632", "Şakayık"),
        ("Hypnotic Poison", 85, "🍯 GOURMAND", "219", "Vanilya"), ("Miss Dior", 95, "🌸 FLORAL", "68652", "Gül"),
        ("Lady Million", 80, "🍯 GOURMAND", "9045", "Bal"), ("Nomade", 85, "🌬 FRESH", "48404", "Erik"),
        ("Angel", 90, "🍯 GOURMAND", "704", "Çikolata"), ("Paradoxe", 95, "🌸 FLORAL", "75338", "Amber"),
        ("Burberry Her", 85, "🌬 FRESH", "51697", "Çilek"), ("Light Blue W", 80, "🌬 FRESH", "485", "Elma"),
        ("Olympéa", 85, "🌬 FRESH", "31661", "Tuz"), ("Flowerbomb", 95, "🌸 FLORAL", "1460", "Çay"),
        ("Baccarat Ext", 175, "✨ MYSTERY", "46066", "Badem"), ("Atomic Rose", 135, "🌸 FLORAL", "56456", "Gül"),
        ("Kirke", 110, "🌬 FRESH", "32172", "Şeftali"), ("Satin Mood", 150, "✨ MYSTERY", "30947", "Ud"),
        ("Delina Rosee", 135, "🌸 FLORAL", "64257", "Armut"), ("Devotion", 90, "🍯 GOURMAND", "84457", "Limon"),
        ("My Way", 85, "🌸 FLORAL", "62036", "Sümbülteber"), ("Idole", 85, "🌸 FLORAL", "55342", "Gül"),
        ("Mademoiselle", 105, "🌸 FLORAL", "611", "Gül"), ("Very Good Girl", 90, "🌸 FLORAL", "65584", "Gül"),
        ("Angels Share", 140, "🍯 GOURMAND", "62615", "Tarçın"), ("Eau d'Issey", 80, "🌬 FRESH", "720", "Nilüfer"),
        ("Narciso Her", 85, "✨ MYSTERY", "605", "Misk"), ("Gucci Bamboo", 80, "🟩 GREEN", "31481", "Zambak"),
        ("Twilly", 85, "🌬 FRESH", "46145", "Zencefil"), ("Bitter Peach", 140, "🍯 GOURMAND", "63060", "Şeftali"),
        ("Soleil Blanc", 130, "🌬 FRESH", "37609", "Hindistan Cevizi"), ("Nuit Tresor", 90, "🍯 GOURMAND", "29157", "Karamel"),
        ("Gris Dior", 135, "✨ MYSTERY", "17387", "Meşe Yosunu"), ("Guilty W", 90, "🌸 FLORAL", "52924", "Leylak"),
        ("Pure Musc", 90, "✨ MYSTERY", "53594", "Misk"), ("Hibiscus", 155, "✨ MYSTERY", "68853", "Vanilya")
    ]
    
    # Veriyi modele dönüştür
    res = []
    for x in m: res.append({"ad":x[0],"f":x[1],"c":x[2],"i":f"https://fimgs.net/mdimg/perfume/m.{x[3]}.jpg","n":x[4],"t":"Erkek"})
    for x in w: res.append({"ad":x[0],"f":x[1],"c":x[2],"i":f"https://fimgs.net/mdimg/perfume/m.{x[3]}.jpg","n":x[4],"t":"Kadın"})
    return res

# --- APP ---
if 'sepet' not in st.session_state: st.session_state.sepet = []
if 'p' not in st.session_state: st.session_state.p = "G"

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- CSS ---
st.markdown("<style>.card{background:white; border-radius:15px; padding:15px; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:20px;} img{border-radius:10px; max-height:200px;}</style>", unsafe_allow_html=True)

# --- NAV ---
c1, c2 = st.columns([4,1])
with c1: 
    if st.button("🛡 ALİY DEKANT"): st.session_state.p = "G"; st.rerun()
with c2: 
    if st.button(f"🛒({len(st.session_state.sepet)})"): st.session_state.p = "S"; st.rerun()

data = get_perfumes()

if st.session_state.p == "G":
    st.title("Hoş Geldiniz")
    b1, b2 = st.columns(2)
    if b1.button("👔 ERKEK"): st.session_state.p="Erkek"; st.rerun()
    if b2.button("👗 KADIN"): st.session_state.p="Kadın"; st.rerun()

elif st.session_state.p == "S":
    st.subheader("🛒 Sepetim")
    toplam = sum(i['f'] for i in st.session_state.sepet)
    for i in st.session_state.sepet: st.write(f"✅ {i['ad']} - {i['f']} TL")
    st.subheader(f"Toplam: {toplam} TL")
    if st.button("SİPARİŞİ TAMAMLA"): st.success("Alındı!")

else:
    st.subheader(f"✨ {st.session_state.p} Vitrini")
    ara = st.text_input("🔍 Ara...")
    sirala = st.selectbox("💲 Fiyat", ["Sırala", "Ucuz", "Pahalı"])
    
    listele = [i for i in data if i['t'] == st.session_state.p]
    if ara: listele = [i for i in listele if ara.lower() in i['ad'].lower()]
    if sirala == "Ucuz": listele = sorted(listele, key=lambda x: x['f'])
    elif sirala == "Pahalı": listele = sorted(listele, key=lambda x: x['f'], reverse=True)

    for i in listele:
        with st.container():
            st.markdown(f'<div class="card"><img src="{i["i"]}"><br><b>{i["ad"]}</b><br><small>{i["c"]} | {i["n"]}</small></div>', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut ({i['ad']})", [3,5,10], 5, key="ml"+i['ad'])
            f = int(ml * i['f'])
            if st.button(f"EKLE - {f} TL", key="bt"+i['ad'], use_container_width=True):
                st.session_state.sepet.append({"ad":i['ad'], "f":f})
                st.toast("Eklendi!")
                st.rerun()
