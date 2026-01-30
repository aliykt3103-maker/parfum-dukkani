import streamlit as st

# --- AYARLAR ---
NUMARA = "905461065331"

# --- TAM ENVANTER (HATASIZ VE EKSİKSİZ) ---
envanter = [
    {"ad": "Sauvage Elixir", "marka": "Dior", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155355_img-9714-dior-sauvage-elixir_720.jpg", "notalar": "Tarçın, Kakule, Lavanta, Meyan Kökü"},
    {"ad": "Aventus", "marka": "Creed", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/156321_img-6298-creed-aventus_720.jpg", "notalar": "Ananas, Huş Ağacı, Misk, Meşe Yosunu"},
    {"ad": "Eros Parfum", "marka": "Versace", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/155700_img-4171-versace-eros-parfum_720.jpg", "notalar": "Nane, Elma, Tonka Fasulyesi, Amber"},
    {"ad": "Layton", "marka": "PdM", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/80743_img-1965-parfums-de-marly-layton_720.jpg", "notalar": "Elma, Lavanta, Vanilya, Kakule"},
    {"ad": "Stronger With You Intensely", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/118314_img-3424-emporio-armani-stronger-with-you-intensely_720.jpg", "notalar": "Pembe Biber, Ardıç, Karamel, Tarçın"},
    {"ad": "Le Male Elixir", "marka": "JPG", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/215758_37f394c86e088d8b671a5332c0276686_le_male_elixir.jpg", "notalar": "Lavanta, Nane, Vanilya, Bal, Tütün"},
    {"ad": "Acqua di Gio Profumo", "marka": "Armani", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/47699_img-6566-giorgio-armani-acqua-di-gio-profumo_720.jpg", "notalar": "Deniz Notaları, Biberiye, Tütsü, Paçuli"},
    {"ad": "Terre d'Hermes", "marka": "Hermes", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/823_img-5561-hermes-terre-d-hermes-eau-de-toilette_720.jpg", "notalar": "Portakal, Greyfurt, Çakmaktaşı, Sedir"},
    {"ad": "Bleu de Chanel Parfum", "marka": "Chanel", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/104323_img-4127-chanel-bleu-de-chanel-parfum_720.jpg", "notalar": "Limon Kabuğu, Sandal Ağacı, Sedir, Kehribar"},
    {"ad": "Interlude Man", "marka": "Amouage", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/15460_img-5374-amouage-interlude-man_720.jpg", "notalar": "Kekik, Tütsü, Deri, Oud, Kehribar"},
    {"ad": "Spicebomb Extreme", "marka": "V&R", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/54655_img-4654-viktor-rolf-spicebomb-extreme_720.jpg", "notalar": "Karabiber, Kimyon, Tütün, Vanilya"},
    {"ad": "Prada L'Homme", "marka": "Prada", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/73385_img-5964-prada-l-homme_720.jpg", "notalar": "Neroli, İris, Menekşe, Mate, Paçuli"},
    {"ad": "Reflection Man", "marka": "Amouage", "fiyat": 100, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/920_img-7509-amouage-reflection-man_720.jpg", "notalar": "Biberiye, Yasemin, Neroli, Sandal Ağacı"},
    {"ad": "Valentino Uomo Born In Roma", "marka": "Valentino", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/124785_img-2350-valentino-uomo-born-in-roma_720.jpg", "notalar": "Mineral Notalar, Tuz, Zencefil, Odunsu Notalar"},
    {"ad": "L'Aventure", "marka": "Al Haramain", "fiyat": 75, "tip": "Erkek", "img": "https://pimages.parfumo.de/720/71871_img-5364-al-haramain-l-aventure_720.jpg", "notalar": "Limon, Bergamot, Elemi, Misk, Amber"},
    
    {"ad": "Libre Intense", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/141873_img-9169-ysl-libre-eau-de-parfum-intense_720.jpg", "notalar": "Lavanta, Portakal Çiçeği, Vanilya, Ambergris"},
    {"ad": "Delina Exclusif", "marka": "PdM", "fiyat": 100, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/103328_img-9831-parfums-de-marly-delina-exclusif_720.jpg", "notalar": "Liçi, Armut, Gül, Tütsü, Oud"},
    {"ad": "Good Girl", "marka": "C. Herrera", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/79361_img-6617-carolina-herrera-good-girl_720.jpg", "notalar": "Badem, Kahve, Yasemin, Zambak, Kakao"},
    {"ad": "Black Opium Le Parfum", "marka": "YSL", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/203954_img-8386-ysl-black-opium-le-parfum_720.jpg", "notalar": "Armut, Mandarin, Dört Çeşit Vanilya, Kahve"},
    {"ad": "La Vie Est Belle", "marka": "Lancome", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/14973_img-9791-lancome-la-vie-est-belle-eau-de-parfum_720.jpg", "notalar": "Siyah Frenk Üzümü, Armut, İris, Yasemin, Pralin"},
    {"ad": "Crystal Noir", "marka": "Versace", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/631_img-3914-versace-crystal-noir-eau-de-parfum_720.jpg", "notalar": "Biber, Zencefil, Hindistan Cevizi, Gardenya, Amber"},
    {"ad": "Alien", "marka": "Mugler", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/707_img-7019-mugler-alien-eau-de-parfum_720.jpg", "notalar": "Yasemin, Güneş Notaları, Beyaz Kehribar"},
    {"ad": "J'adore", "marka": "Dior", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/210_img-5645-dior-j-adore-eau-de-parfum_720.jpg", "notalar": "Armut, Kavun, Manolya, Yasemin, Orkide"},
    {"ad": "L'Interdit Rouge", "marka": "Givenchy", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/155694_img-5544-givenchy-l-interdit-eau-de-parfum-rouge_720.jpg", "notalar": "Kan Portakalı, Zencefil, Sümbülteber, Sandal Ağacı"},
    {"ad": "Coco Mademoiselle", "marka": "Chanel", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/611_img-2826-chanel-coco-mademoiselle-eau-de-parfum_720.jpg", "notalar": "Portakal, Gül, Yasemin, Paçuli, Misk"},
    {"ad": "Hypnotic Poison", "marka": "Dior", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/219_img-6246-dior-hypnotic-poison-eau-de-toilette_720.jpg", "notalar": "Hindistan Cevizi, Eriği, Kayısı, Sümbülteber, Vanilya"},
    {"ad": "La Nuit Tresor", "marka": "Lancome", "fiyat": 75, "tip": "Kadın", "img": "https://pimages.parfumo.de/720/51296_img-2475-lancome-la-nuit-tresor-eau-de-parfum_720.jpg", "notalar": "Armut, Siyah Gül, Vanilya Orkidesi, Tütsü, Pralin"},
    
    {"ad": "Baccarat Rouge 540", "marka": "MFK", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/63510_img-1313-maison-francis-kurkdjian-baccarat-rouge-540_720.jpg", "notalar": "Safran, Yasemin, Kehribar Odunu, Çam Reçinesi"},
    {"ad": "Naxos", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/52972_img-7546-xerjoff-1861-naxos_720.jpg", "notalar": "Lavanta, Bergamot, Bal, Tarçın, Tütün, Vanilya"},
    {"ad": "Hacivat", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/97792_img-6330-nishane-hacivat_720.jpg", "notalar": "Ananas, Greyfurt, Meşe Yosunu, Sedir"},
    {"ad": "Angels' Share", "marka": "Kilian", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/144675_img-2821-by-kilian-angels-share_720.jpg", "notalar": "Konyak, Tarçın, Meşe, Vanilya, Pralin"},
    {"ad": "Ganimede", "marka": "M.A. Barrois", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/120935_img-6140-marc-antoine-barrois-ganymede_720.jpg", "notalar": "Safran, Menekşe Yaprağı, Ölümsüz Çiçek, Süet"},
    {"ad": "Ani", "marka": "Nishane", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/121113_img-2325-nishane-ani_720.jpg", "notalar": "Zencefil, Bergamot, Gül, Vanilya, Benzoin"},
    {"ad": "Erba Pura", "marka": "Xerjoff", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/121285_img-5544-xerjoff-v-erba-pura_720.jpg", "notalar": "Sicilya Portakalı, Limon, Akdeniz Meyveleri, Beyaz Misk"},
    {"ad": "Tobacco Vanille", "marka": "Tom Ford", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/1825_img-5871-tom-ford-private-blend-tobacco-vanille-eau-de-parfum_720.jpg", "notalar": "Tütün Yaprağı, Baharatlar, Vanilya, Kakao"},
    {"ad": "Ombre Nomade", "marka": "Louis Vuitton", "fiyat": 100, "tip": "Uniseks", "img": "https://pimages.parfumo.de/720/105437_img-4054-louis-vuitton-ombre-nomade_720.jpg", "notalar": "Oud, Ahududu, Tütsü, Safran, Gül"},
    {"ad": "Side Effect", "marka": "Initio", "fiyat": 100, "tip": "Uniseks", "img": "
