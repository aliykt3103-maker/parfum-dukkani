import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- ENVANTER (50 ERKEK + 50 KADIN) ---
def get_data():
    erkek = [
        {"ad": "Sauvage Elixir", "fiyat": 95, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.68415.jpg", "not": "Lavanta, Tarçın"},
        {"ad": "Creed Aventus", "fiyat": 130, "cat": "🌬 FRESH", "img": "https://fimgs.net/mdimg/perfume/m.9828.jpg", "not": "Ananas, Misk"},
        {"ad": "Versace Eros", "fiyat": 80, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.63731.jpg", "not": "Nane, Elma"},
        {"ad": "Nishane Hacivat", "fiyat": 115, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.44174.jpg", "not": "Ananas, Meşe Yosunu"},
        {"ad": "Ganimede", "fiyat": 120, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.54734.jpg", "not": "Safran, Süet"},
        {"ad": "Bleu de Chanel", "fiyat": 90, "cat": "🟦 BLUE", "img": "https://fimgs.net/mdimg/perfume/m.25967.jpg", "not": "Tütsü, Greyfurt"},
        {"ad": "Dior Homme Intense", "fiyat": 95, "cat": "✨ MYSTERY", "img": "https://fimgs.net/mdimg/perfume/m.13016.jpg", "not": "İris, Lavanta"},
        {"ad": "Marly Layton", "fiyat": 110, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.39332.jpg", "not": "Vanilya, Elma"},
        {"ad": "Xerjoff Naxos", "fiyat": 120, "cat": "🍯 GOURMAND", "img": "https://fimgs.net/mdimg/perfume/m.52972.jpg", "not": "Bal, Tütün"},
        {"ad": "Stronger With You", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.44587.jpg", "not": "Kestane, Vanilya"},
        {"ad": "Spicebomb Extreme", "fiyat": 85, "cat": "🟥 RED", "img": "https://fimgs.net/mdimg/perfume/m.30447.jpg", "not": "Tütün, Biber"},
        {"ad": "Terre d'Hermes", "fiyat": 80, "cat": "🟩 GREEN", "img": "https://fimgs.net/mdimg/perfume/m.823.jpg", "not": "Portakal, Sedir"},
        {"ad": "Tom Ford Oud Wood", "fiyat": 130, "cat": "✨ MYSTERY", "img": "
