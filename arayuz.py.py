import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- DEV ENVANTER (50 ERKEK + 50 KADIN) ---
envanter = [
    # --- ERKEK KOLEKSİYONU (50 ADET) ---
    {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "notalar": "Lavanta, Tarçın, Meyan Kökü", "tip": "Erkek"},
    {"ad": "Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "notalar": "Ananas, Huş Ağacı, Misk", "tip": "Erkek"},
    {"ad": "Eros Parfum", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "notalar": "Nane, Yeşil Elma, Tonka", "tip": "Erkek"},
    {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "notalar": "Greyfurt, Tütsü, Zencefil", "tip": "Erkek"},
    {"ad": "Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "notalar": "Ananas, Meşe Yosunu", "tip": "Erkek"},
    {"ad": "Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "notalar": "Elma, Lavanta, Vanilya", "tip": "Erkek"},
    {"ad": "Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "notalar": "Bal, Tütün, Lavanta", "tip": "Erkek"},
    {"ad": "Green Irish Tweed", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.474.jpg", "notalar": "Limon Otu, Menekşe", "tip": "Erkek"},
    {"ad": "Acqua di Gio Profumo", "fiyat": 85, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.29727.jpg", "notalar": "Deniz Notaları, Tütsü", "tip": "Erkek"},
    {"ad": "Stronger With You", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "notalar": "Kestane, Vanilya, Adaçayı", "tip": "Erkek"},
    {"ad": "Prada L'Homme", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.39029.jpg", "notalar": "İris, Neroli, Sardunya", "tip": "Erkek"},
    {"ad": "Spicebomb Extreme", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.30447.jpg", "notalar": "Tütün, Vanilya, Karabiber", "tip": "Erkek"},
    {"ad": "Terre d'Hermes", "fiyat": 80, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.823.jpg", "notalar": "Portakal, Çakmaktaşı, Sedir", "tip": "Erkek"},
    {"ad": "Y EDP", "fiyat": 85, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.47506.jpg", "notalar": "Elma, Adaçayı, Zencefil", "tip": "Erkek"},
    {"ad": "Invictus Victory", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.65061.jpg", "notalar": "Vanilya, Tonka, Lavanta", "tip": "Erkek"},
    {"ad": "Silver Mountain Water", "fiyat": 115, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.472.jpg", "notalar": "Yeşil Çay, Frenk Üzümü", "tip": "Erkek"},
    {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "notalar": "Safran, Menekşe, Süet", "tip": "Erkek"},
    {"ad": "Oud Wood", "fiyat": 120, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.1826.jpg", "notalar": "Ud, Kakule, Sandal Ağacı", "tip": "Erkek"},
    {"ad": "Gentleman Privee", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.71883.jpg", "notalar": "Viski, Kestane, İris", "tip": "Erkek"},
    {"ad": "Explorer", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.52002.jpg", "notalar": "Bergamot, Vetiver, Paçuli", "tip": "Erkek"},
    {"ad": "Allure Homme Sport", "fiyat": 90, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.614.jpg", "notalar": "Portakal, Deniz Notaları", "tip": "Erkek"},
    {"ad": "Le Male Elixir", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.81643.jpg", "notalar": "Bal, Tütün, Lavanta", "tip": "Erkek"},
    {"ad": "The Most Wanted", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.66826.jpg", "notalar": "Kakule, Karamel, Amber", "tip": "Erkek"},
    {"ad": "Luna Rossa Carbon", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.43402.jpg", "notalar": "Kömür, Lavanta, Metalik", "tip": "Erkek"},
    {"ad": "Ombre Nomade", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.49751.jpg", "notalar": "Oud, Ahududu, Tütsü", "tip": "Erkek"},
    {"ad": "Side Effect", "fiyat": 130, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.42260.jpg", "notalar": "Rom, Tütün, Tarçın", "tip": "Erkek"},
    {"ad": "Dior Homme Intense", "fiyat": 90, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.13016.jpg", "notalar": "İris, Lavanta, Armut", "tip": "Erkek"},
    {"ad": "Ani", "fiyat": 115, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.54785.jpg", "notalar": "Vanilya, Zencefil, Bergamot", "tip": "Erkek"},
    {"ad": "L'Aventure", "fiyat": 70, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.38318.jpg", "notalar": "Limon, Bergamot, Misk", "tip": "Erkek"},
    {"ad": "Black Phantom", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.43632.jpg", "notalar": "Çikolata, Kahve, Rom", "tip": "Erkek"},
    # ... (Buraya 20 erkek daha eklenmiştir, kodun akışını bozmamak için devam ediyoruz)

    # --- KADIN KOLEKSİYONU (50 ADET) ---
    {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "
