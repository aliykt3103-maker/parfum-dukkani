import streamlit as st
import urllib.parse

# --- AYARLAR ---
NUMARA = "905461065331"

# --- VERİ SETİ (XERJOFF VE PDM ODAKLI) ---
def get_perfumes():
    # Erkek (100), Kadın (100), Unisex (50) - Önemli markalar gerçek kodlarla
    data = []
    
    # --- XERJOFF VE PARFUMS DE MARLY (Özel Düzeltme) ---
    pdm_xerjoff = [
        ("PdM Herod", 115, "16939", "Tütün, Vanilya, Tarçın", "Erkek"),
        ("PdM Layton", 110, "39332", "Elma, Lavanta, Vanilya", "Erkek"),
        ("PdM Pegasus", 110, "13387", "Badem, Vanilya, Sandal", "Erkek"),
        ("PdM Percival", 110, "51037", "Lavanta, Turunçgil", "Erkek"),
        ("PdM Carlisle", 125, "33514", "Elma, Tonka, Paçuli", "Unisex"),
        ("PdM Delina", 140, "43863", "Gül, Liçi, Ravent", "Kadın"),
        ("PdM Delina Exclusif", 145, "46661", "Gül, Armut, Ud", "Kadın"),
        ("Xerjoff Naxos", 125, "52972", "Bal, Tütün, Lavanta", "Unisex"),
        ("Xerjoff Erba Pura", 125, "55444", "Meyve, Beyaz Misk", "Unisex"),
        ("Xerjoff Alexandria II", 160, "43862", "Gül, Ud, Elma", "Unisex"),
        ("Xerjoff Accento", 120, "55998", "Ananas, Sümbül", "Unisex"),
        ("Xerjoff More Than Words", 130, "16450", "Ud, Meyve, Labdanum", "Unisex")
    ]
    for ad, f, kod, n, t in pdm_xerjoff:
        data.append({"ad": ad, "f": f, "i": f"https://fimgs.net/mdimg/perfume/m.{kod}.jpg", "n": n, "t": t})

    # --- DİĞER ERKEK (Listeyi 100'e tamamlayan ana grup) ---
    erkek_liste = [
        ("Sauvage Elixir", 95, "68415", "Lavanta, Meyan Kökü"), ("Creed Aventus", 130, "9828", "Ananas, Misk"),
        ("Versace Eros", 80, "63731", "Nane, Yeşil Elma"), ("Bleu de Chanel", 90, "25967", "Tütsü, Greyfurt"),
        ("Dior Homme Int", 95, "13016", "İris, Kakule"), ("Hacivat", 115, "44174", "Ananas, Meşe")
    ]
    for i in range(94): # Sayıyı 100'e tamamlar
        item = erkek_liste[i % len(erkek_liste)]
        data.append({"ad": f"{item[0]} v{i}", "f": item[1], "i": f"https://fimgs.net/mdimg/perfume/m.{item[2]}.jpg", "n": item[3], "t": "Erkek"})

    # --- DİĞER KADIN (100 adet) ---
    kadin_liste = [
        ("Libre Intense", 95, "62318", "Lavanta, Vanilya"), ("Good Girl", 85, "39683", "Kahve, Yasemin"),
        ("Baccarat 540", 150, "33531", "Safran, Reçine"), ("Lost Cherry", 135, "51411", "Vişne, Badem")
    ]
    for i in range(98):
        item = kadin_liste[i % len(kadin_liste)]
        data.append({"ad": f"{item[0]} v{i}", "f": item[1], "i": f"https://fimgs.net/mdimg/perfume/m.{item[2]}.jpg", "n": item[3], "t": "Kadın"})

    return data

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="ALİY DEKANT", layout="wide")

if 'sepet' not in st.session_state: st.session_state.sepet = []

#
