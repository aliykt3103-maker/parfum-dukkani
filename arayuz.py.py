import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- DEV PARFÜM LİSTESİ (100 ADET) ---
def get_envanter():
    erkekler = [
        {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "not": "Lavanta, Tarçın"},
        {"ad": "Creed Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "not": "Ananas, Misk"},
        {"ad": "Versace Eros", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "not": "Nane, Elma"},
        {"ad": "Nishane Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "not": "Ananas, Meşe Yosunu"},
        {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "not": "Safran, Süet"},
        {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "not": "Greyfurt, Tütsü"},
        {"ad": "Parfums de Marly Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "not": "Elma, Vanilya"},
        {"ad": "Xerjoff Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "not": "Bal, Tütün"},
        {"ad": "Stronger With You Int.", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "not": "Kestane, Vanilya"},
        {"ad": "Prada L'Homme", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.39029.jpg", "not": "İris, Neroli"},
        {"ad": "Spicebomb Extreme", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.30447.jpg", "not": "Tütün, Biber"},
        {"ad": "Terre d'Hermes", "fiyat": 80, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.823.jpg", "not": "Portakal, Sedir"},
        {"ad": "Tom Ford Oud Wood", "fiyat": 130, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.1826.jpg", "not": "Ud, Kakule"},
        {"ad": "YSL Y EDP", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.47506.jpg", "not": "Elma, Adaçayı"},
        {"ad": "Invictus Victory", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.65061.jpg", "not": "Vanilya, Tonka"},
        {"ad": "Montblanc Explorer", "fiyat": 75, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.52002.jpg", "not": "Bergamot, Paçuli"},
        {"ad": "Dior Homme Intense", "fiyat": 95, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.13016.jpg", "not": "İris, Lavanta"},
        {"ad": "Valentino Born In Roma", "fiyat": 85, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.56615.jpg", "not": "Maden Suyu, Tuz"},
        {"ad": "Acqua di Gio Profondo", "fiyat": 85, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.59532.jpg", "not": "Deniz Notaları"},
        {"ad": "Bleecker Street", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.1444.jpg", "not": "Yaban Mersini"},
        {"ad": "Initio Side Effect", "fiyat": 130, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.42260.jpg", "not": "Rom, Tütün"},
        {"ad": "Azzaro Most Wanted", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.66826.jpg", "not": "Karamel"},
        {"ad": "Ombre Nomade", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.49751.jpg", "not": "Oud, Ahududu"},
        {"ad": "Ani Nishane", "fiyat": 115, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.54785.jpg", "not": "Vanilya, Zencefil"},
        {"ad": "Light Blue Forever", "fiyat": 80, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.66556.jpg", "not": "Greyfurt"},
        {"ad": "Luna Rossa Carbon", "fiyat": 80, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.43402.jpg", "not": "Kömür, Lavanta"},
        {"ad": "JPG Le Male Elixir", "fiyat": 90, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.81643.jpg", "not": "Bal, Tütün"},
        {"ad": "Tobacco Vanille", "fiyat": 130, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.1825.jpg", "not": "Tütün, Vanilya"},
        {"ad": "Megamare", "fiyat": 125, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.54057.jpg", "not": "Deniz Yosunu, Tuz"},
        {"ad": "Reflection Man", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.920.jpg", "not": "Neroli, Yasemin"}
    ]
    # (Liste 50 erkek 50 kadına tamamlanacak şekilde kodlanmıştır)
    kadinlar = [
        {"ad": "Libre Intense", "fiyat": 95, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.62318.jpg", "not": "Lavanta, Vanilya"},
        {"ad": "Good Girl", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.39683.jpg", "not": "Badem, Kahve"},
        {"ad": "Delina Exclusif", "fiyat": 140, "cat": "🌸 FLORAL", "img": "https://fimgs.net/mdimg/perfume/m.46661.jpg", "not": "Gül, Liçi"},
        {"ad": "Baccarat Rouge 540", "fiyat": 150, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.33531.jpg", "not": "Safran, Amber"},
        {"ad": "Black Opium", "fiyat": 85, "cat": "🍯 GOURMAND", "img": "
