import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- DEV ENVANTER (50 ERKEK + 50 KADIN) ---
envanter = [
    # --- ERKEK KOLEKSİYONU (50 ADET) ---
    {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "notalar": "Lavanta, Tarçın", "tip": "Erkek"},
    {"ad": "Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Misk", "tip": "Erkek"},
    {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "notalar": "Nane, Elma", "tip": "Erkek"},
    {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "notalar": "Greyfurt, Tütsü", "tip": "Erkek"},
    {"ad": "Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "notalar": "Ananas, Meşe Yosunu", "tip": "Erkek"},
    {"ad": "Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "notalar": "Elma, Vanilya", "tip": "Erkek"},
    {"ad": "Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "notalar": "Bal, Tütün", "tip": "Erkek"},
    {"ad": "Green Irish Tweed", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.474.jpg", "notalar": "Limon Otu, Menekşe", "tip": "Erkek"},
    {"ad": "Y EDP", "fiyat": 85, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.47506.jpg", "notalar": "Elma, Adaçayı", "tip": "Erkek"},
    {"ad": "Stronger With You", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "notalar": "Kestane, Vanilya", "tip": "Erkek"},
    {"ad": "Prada L'Homme", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.39029.jpg", "notalar": "İris, Neroli", "tip": "Erkek"},
    {"ad": "Spicebomb Extreme", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.30447.jpg", "notalar": "Tütün, Vanilya", "tip": "Erkek"},
    {"ad": "Terre d'Hermes", "fiyat": 80, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.823.jpg", "notalar": "Portakal, Sedir", "tip": "Erkek"},
    {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "notalar": "Safran, Menekşe", "tip": "Erkek"},
    {"ad": "Oud Wood", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.1826.jpg", "notalar": "Ud, Sandal Ağacı", "tip": "Erkek"},
    {"ad": "Explorer", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.52002.jpg", "notalar": "Bergamot, Vetiver", "tip": "Erkek"},
    {"ad": "Silver Mountain Water", "fiyat": 115, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.472.jpg", "notalar": "Yeşil Çay, Misk", "tip": "Erkek"},
    {"ad": "Ani", "fiyat": 115, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.54785.jpg", "notalar": "Vanilya, Zencefil", "tip": "Erkek"},
    {"ad": "Side Effect", "fiyat": 130, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.42260.jpg", "notalar": "Rom, Tütün", "tip": "Erkek"},
    {"ad": "Dior Homme Intense", "fiyat": 90, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.13016.jpg", "notalar": "İris, Armut", "tip": "Erkek"},
    {"ad": "Ombre Nomade", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.49751.jpg", "notalar": "Oud, Ahududu", "tip": "Erkek"},
    {"ad": "Black Phantom", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.43632.jpg", "notalar": "Kahve, Rom", "tip": "Erkek"},
    {"ad": "Allure Homme Sport", "fiyat": 90, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.614.jpg", "notalar": "Deniz Notaları", "tip": "Erkek"},
    {"ad": "Invictus Victory", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.65061.jpg", "notalar": "Vanilya, Tonka", "tip": "Erkek"},
    {"ad": "Luna Rossa Carbon", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.43402.jpg", "notalar": "Lavanta, Kömür", "tip": "Erkek"},
    {"ad": "The Most Wanted", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.66826.jpg", "notalar": "Karamel, Amber", "tip": "Erkek"},
    {"ad": "Gentleman Privee", "fiyat": 85, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.71883.jpg", "notalar": "Viski, İris", "tip": "Erkek"},
    {"ad": "Bleecker Street", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.1444.jpg", "notalar": "Yaban Mersini, Meşe Yosunu", "tip": "Erkek"},
    {"ad": "Wood Sage & Sea Salt", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.27044.jpg", "notalar": "Adaçayı, Deniz Tuzu", "tip": "Erkek"},
    {"ad": "Jazz Club", "fiyat": 95, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.20541.jpg", "notalar": "Tütün, Rom, Vanilya", "tip": "Erkek"},
    {"ad": "By the Fireplace", "fiyat": 95, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.31623.jpg", "notalar": "Kestane, Odunsu", "tip": "Erkek"},
    {"ad": "Reflection Man", "fiyat": 130, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.920.jpg", "notalar": "Neroli, Yasemin", "tip": "Erkek"},
    {"ad": "Light Blue Intense", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.44034.jpg", "notalar": "Greyfurt, Deniz Suyu", "tip": "Erkek"},
    {"ad": "Toy Boy", "fiyat": 75, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.55858.jpg", "notalar": "Gül, Armut, Biber", "tip": "Erkek"},
    {"ad": "Interlude Man", "fiyat": 140, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.15294.jpg", "notalar": "Tütsü, Deri", "tip": "Erkek"},
    {"ad": "Alexandria II", "fiyat": 160, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.43862.jpg", "notalar": "Elma, Lavanta, Ud", "tip": "Erkek"},
    {"ad": "L'Eau d'Issey", "fiyat": 75, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.721.jpg", "notalar": "Yuzu, Limon", "tip": "Erkek"},
    {"ad": "Dylan Blue", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.39348.jpg", "notalar": "Su Notaları, İncir", "tip": "Erkek"},
    {"ad": "Fahrenheit", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.218.jpg", "notalar": "Deri, Menekşe", "tip": "Erkek"},
    {"ad": "Polo Green", "fiyat": 75, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.829.jpg", "notalar": "Çam, Tütün", "tip": "Erkek"},
    {"ad": "Pegasus", "fiyat": 110, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.13387.jpg", "notalar": "Badem, Vanilya", "tip": "Erkek"},
    {"ad": "Tobacco Vanille", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.1825.jpg", "notalar": "Tütün, Vanilya", "tip": "Erkek"},
    {"ad": "Pure Malt", "fiyat": 110, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.6103.jpg", "notalar": "Malt, Viski, Kahve", "tip": "Erkek"},
    {"ad": "Viking", "fiyat": 125, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.41620.jpg", "notalar": "Nane, Pembe Biber", "tip": "Erkek"},
    {"ad": "Haltane", "fiyat": 130, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.70776.jpg", "notalar": "Safran, Ud, Pralin", "tip": "Erkek"},
    {"ad": "Le Male Elixir", "fiyat": 90, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.81643.jpg", "notalar": "Bal, Tütün", "tip": "Erkek"},
    {"ad": "Acqua di Parma", "fiyat": 95, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.1555.jpg", "notalar": "Narenciye, Lavanta", "tip": "Erkek"},
    {"ad": "Grey Vetiver", "fiyat": 100, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.6634.jpg", "notalar": "Vetiver, Greyfurt", "tip": "Erkek"},
    {"ad": "Code Parfum", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.75333.jpg", "notalar": "İris, Bergamot", "tip": "Erkek"},
    {"ad": "L'Aventure", "fiyat": 70, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.38318.jpg", "notalar": "Limon, Misk", "tip": "Erkek"},

    # --- KADIN KOLEKSİYONU (50 ADET) ---
    {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "notalar": "Lavanta, Vanilya", "tip": "Kadın"},
    {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "notalar": "Kahve, Kakao", "tip": "Kadın"},
    {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "notalar": "Gül, Liçi", "tip": "Kadın"},
    {"ad": "Baccarat Rouge", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "notalar": "Safran, Amber", "tip": "Kadın"},
    {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.25317.jpg", "notalar": "Kahve, Vanilya", "tip": "Kadın"},
    {"ad": "Crystal Noir", "fiyat": 80, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.631.jpg", "notalar": "Hindistan Cevizi, Amber", "tip": "Kadın"},
    {"ad": "L'Interdit Rouge", "fiyat": 95, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.68656.jpg", "notalar": "Zencefil, Kan Portakalı", "tip": "Kadın"},
    {"ad": "Chance Tendre", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.8069.jpg", "notalar": "Ayva, Greyfurt", "tip": "Kadın"},
    {"ad": "La Vie Est Belle", "fiyat": 80, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.14973.jpg", "notalar": "Pralin, İris", "tip": "Kadın"},
    {"ad": "Alien", "fiyat": 85, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.707.jpg", "notalar": "Yasemin, Kaşmir", "tip": "Kadın"},
    {"ad": "J'adore", "fiyat": 90, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.210.jpg", "notalar": "Armut, Yasemin", "tip": "Kadın"},
    {"ad": "Burberry Her", "fiyat": 85, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.51697.jpg", "notalar": "Çilek, Ahududu", "tip": "Kadın"},
    {"ad": "Hypnotic Poison", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.219.jpg", "notalar": "Acı Badem, Vanilya", "tip": "Kadın"},
    {"ad": "Idole", "fiyat": 85, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.55342.jpg", "notalar": "Gül, Yasemin", "tip": "Kadın"},
    {"ad": "Chloe EDP", "fiyat": 85, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.1550.jpg", "notalar": "Şakayık, Gül", "tip": "Kadın"},
    {"ad": "Lost Cherry", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.51411.jpg", "notalar": "Vişne, Likör", "tip": "Kadın"},
    {"ad": "Nomade", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.48404.jpg", "notalar": "Mirabel Eriği", "tip": "Kadın"},
    {"ad": "Si Intense", "fiyat": 90, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.85419.jpg", "notalar": "Siyah Frenk Üzümü", "tip": "Kadın"},
    {"ad": "Angels Share", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.62615.jpg", "notalar": "Konyak, Tarçın", "tip": "Kadın"},
    {"ad": "Erba Pura", "fiyat": 120, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.55444.jpg", "notalar": "Akdeniz Meyveleri", "tip": "Kadın"},
    {"ad": "Coco Mademoiselle", "fiyat": 100, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.611.jpg", "notalar": "Portakal, Paçuli", "tip": "Kadın"},
    {"ad": "Mon Guerlain", "fiyat": 90, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.43263.jpg", "notalar": "Lavanta, Vanilya", "tip": "Kadın"},
    {"ad": "For Her", "fiyat": 85, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.605.jpg", "notalar": "Misk, Osmanthus", "tip": "Kadın"},
    {"ad": "Devotion", "fiyat": 90, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.84457.jpg", "notalar": "Limon, Portakal Çiçeği", "tip": "Kadın"},
    {"ad": "Olympéa", "fiyat": 85, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.31661.jpg", "notalar": "Tuzlu Vanilya", "tip": "Kadın"},
    {"ad": "Scandal", "fiyat": 90, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.45065.jpg", "notalar": "Bal, Gardenya", "tip": "Kadın"},
    {"ad": "Pure Musc", "fiyat": 90, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.53594.jpg", "notalar": "Misk, Çiçeksi", "tip": "Kadın"},
    {"ad": "Bamboo", "fiyat": 80, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.31481.jpg", "notalar": "Zambak, Portakal Çiçeği", "tip": "Kadın"},
    {"ad": "Twilly d'Hermès", "fiyat": 85, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.46145.jpg", "notalar": "Zencefil, Sümbülteber", "tip": "Kadın"},
    {"ad": "The One", "fiyat": 85, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.698.jpg", "notalar": "Şeftali, Vanilya", "tip": "Kadın"},
    {"ad": "Bright Crystal", "fiyat": 80, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.632.jpg", "notalar": "Yuzu, Şakayık", "tip": "Kadın"},
    {"ad": "Lady Million", "fiyat": 80, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.9045.jpg", "notalar": "Bal, Ahududu", "tip": "Kadın"},
    {"ad": "Paradoxe", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.75338.jpg", "notalar": "Neroli, Amber", "tip": "Kadın"},
    {"ad": "Light Blue", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.485.jpg", "notalar": "Limon, Elma", "tip": "Kadın"},
    {"ad": "Guilty Pour Femme", "fiyat": 90, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.52924.jpg", "notalar": "Menekşe, Leylak", "tip": "Kadın"},
    {"ad": "Miss Dior", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.68652.jpg", "notalar": "Gül, Zambak", "tip": "Kadın"},
    {"ad": "Flowerbomb", "fiyat": 90, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.1460.jpg", "notalar": "Orkide, Gül", "tip": "Kadın"},
    {"ad": "La Nuit Tresor", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.29157.jpg", "notalar": "Siyah Gül, Karamel", "tip": "Kadın"},
    {"ad": "Portrait of a Lady", "fiyat": 140, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.10464.jpg", "notalar": "Gül, Tütsü", "tip": "Kadın"},
    {"ad": "Oud Satin Mood", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.30947.jpg", "notalar": "Gül, Vanilya, Oud", "tip": "Kadın"},
    {"ad": "Love Don't Be Shy", "fiyat": 140, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.1016.jpg", "notalar": "Hatmi, Portakal Çiçeği", "tip": "Kadın"},
    {"ad": "Bitter Peach", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.63060.jpg", "notalar": "Şeftali, Kakule", "tip": "Kadın"},
    {"ad": "Soleil Blanc", "fiyat": 120, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.37609.jpg", "notalar": "Hindistan Cevizi", "tip": "Kadın"},
    {"ad": "Baccarat Extrait", "fiyat": 170, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.46066.jpg", "notalar": "Safran, Acı Badem", "tip": "Kadın"},
    {"ad": "Atomic Rose", "fiyat": 130, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.56456.jpg", "notalar": "Gül, Pembe Biber", "tip": "Kadın"},
    {"ad": "Delina", "fiyat": 120, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.43871.jpg", "notalar": "Liçi, Ravent", "tip": "Kadın"},
    {"ad": "Gris Dior", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.17387.jpg", "notalar": "Meşe Yosunu, Gül", "tip": "Kadın"},
    {"ad": "Very Good Girl", "fiyat": 90, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.65584.jpg", "notalar": "Kuş Üzümü, Gül", "tip": "Kadın"},
    {"ad": "Hibiscus Mahajad", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.68853.jpg", "notalar": "Ebegümeci, Deri", "tip": "Kadın"},
    {"ad": "Kirke", "fiyat": 100, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.32172.jpg", "notalar": "Çarkıfelek, Şeftali", "tip": "Kadın"}
]

st.set_page_config(page_title="ALİY DEKANT", layout="centered")

# --- PREMIUM TASARIM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #fdfdfd; }
    .parfum-kart { 
        background: white; border-radius: 25px; padding: 20px; text-align: center; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 1px solid #f0f0f0; margin-bottom: 25px;
    }
    img { border-radius: 20px; max-height: 280px; width: 100%; object-fit: contain; margin-bottom: 15px; }
    .notalar { color: white; font-size: 11px; background: #e74c3c; padding: 6px 12px; border-radius: 10px; display: inline-block; margin-bottom: 15px; }
    .cat-tag { background: #f0f2f6; color: #5f6368; padding: 5px 12px; border-radius: 12px; font-size: 11px; font-weight: bold; text-transform: uppercase; margin-bottom: 10px; display: inline-block; }
    .stButton>button { border-radius: 15px; height: 50px; font-weight: bold; background-color: #007bff !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

if 'ekran' not in st.session_state: st.session_state.ekran = "GİRİŞ"

if st.session_state.ekran == "GİRİŞ":
    st.markdown("<h1 style='text-align:center;'>✨ ALİY DEKANT</h1>", unsafe_allow_html=True)
    st.write("---")
    if st.button("👔 ERKEK KOLEKSİYONU (50 ADET)", use_container_width=True):
        st.session_state.ekran = "Erkek"; st.rerun()
    if st.button("👗 KADIN KOLEKSİYONU (50 ADET)", use_container_width=True):
        st.session_state.ekran = "Kadın"; st.rerun()
else:
    st.button("⬅️ ANA MENÜ", use_container_width=True, on_click=lambda: setattr(st.session_state, 'ekran', "GİRİŞ"))
    
    kats = ["TÜMÜ", "🟦 BLUE", "🟩 GREEN", "🌬 FRESH", "🟥 RED", "🌸 FLORAL", "🍯 GOURMAND", "✨ MYSTERY"]
    secilen = st.radio("Filtrele:", kats, horizontal=True)
    
    goster = [p for p in envanter if p['tip'] == st.session_state.ekran and (secilen == "TÜMÜ" or p['cat'] == secilen)]

    for p in goster:
        with st.container():
            st.markdown(f'''
            <div class="parfum-kart">
                <span class="cat-tag">{p["cat"]}</span>
                <img src="{p["img"]}">
                <h2 style="font-size:24px;">{p["ad"]}</h2>
                <div class="notalar">PİRAMİT: {p["notalar"]}</div>
            </div>
            ''', unsafe_allow_html=True)
            ml = st.select_slider(f"Boyut seç ({p['ad']})", options=[3, 5, 10], value=5, key=f"sl_{p['ad']}")
            if st.button(f"{int(ml * p['fiyat'])} TL - SATIN AL", key=f"bt_{p['ad']}", use_container_width=True):
                st.toast(f"⚠️ {p['ad']} yakında satışa sunulacaktır!", icon="🚀")
            st.write("---")
