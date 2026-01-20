import pandas as pd
import numpy as np
import joblib
import os
import asyncio
from twikit import Client
from googleapiclient.discovery import build
import feedparser
import requests
from datetime import datetime, timedelta, timezone

# ==============================================================================
# 🔑 1. GİZLİ ANAHTARLAR (SENİN ATTIĞIN BİLGİLER GİRİLDİ)
# ==============================================================================

# YOUTUBE API KEY
YOUTUBE_API_KEY = "AIzaSyB39rbGDxH-7hq4VZTZWWW-A5lIRR7DSqM"

# TWITTER HESAPLARI (Attığın 3 hesap bilgisi)
TWITTER_HESAPLARI = [
    {
        "id": "Hesap 1",
        "auth_token": "f6b8409278028a0733e7c75d497bf57e7ec56dc0",
        "ct0": "b11fd768ac6e0cbc4cd5a479d18dd90005c801370b18871389e605b246e13f56f9e0eeb00bd7d53b634703a31c1b07687a2fa6fb948851e76634373c4905ed12d397e0d2f4d9606652d709b620a9bc79"
    },
    {
        "id": "Hesap 2",
        "auth_token": "5c3d36bac608e687e752060001492ad10c2b6eb1",
        "ct0": "da9f22e1907758f5120099184bd712d94cc5cb8bd8b5b7bc92b7fb2fa33d3971587f8177862ef6fd5b339b2fae008fb12d18ec762f8b1c6501e2718674f9a20935c613663531fe93791501c56fdbf48d"
    },
    {
        "id": "Hesap 3",
        "auth_token": "bc325f4da46bc0a023b04ce1acaf6aab52e98d37",
        "ct0": "a3744100182e4bb39ec197178080a6c7e6503644864a18652acd6e608503ba4a4f5b8a25698d52884a17e890671f1229e7f74ab18ed6d9a10f110d95f870d8dab97fb7d204c8c7dcf3a080d1ca13dbfd"
    }
]

# ==============================================================================
# ⚙️ AYARLAR VE DOSYA YOLLARI
# ==============================================================================
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
MODEL_DOSYASI = os.path.join(desktop_path, "KRIPTO_AI_BEYNI.pkl")
VEKTOR_DOSYASI = os.path.join(desktop_path, "KELIME_VEKTORU.pkl")

# 
# DÜZELTME: Artık Yıllar Değil, "Piyasa Döngüleri" (Cycles) Var.
# 1 aylık veri, bu döngülerden hangisine benziyorsa onu seçecek.
PIYASA_DONGULERI = {
    "MEGA_BOGA_KOSU": {
        "Firsat": 85, "Risk": 15, 
        "Aciklama": "Parabolik yükseliş evresi. Herkesin kazandığı, FOMO'nun zirve yaptığı dönem."
    },
    "AYI_PIYASASI_DIP": {
        "Firsat": 10, "Risk": 90, 
        "Aciklama": "Umutların tükendiği, hacmin kuruduğu 'Kapitülasyon' evresi."
    },
    "SOK_DUSUS_TOPARLANMA": {
        "Firsat": 45, "Risk": 55, 
        "Aciklama": "Sert bir haber (Savaş/Pandemi vb.) sonrası V şeklinde hızlı toparlanma."
    },
    "HYPE_VE_ALTCOIN_PARTISI": {
        "Firsat": 75, "Risk": 25, 
        "Aciklama": "Bitcoin'in yataya bağlayıp paranın altcoinlere aktığı dönem."
    },
    "GUVEN_KRIZI_COKUS": {
        "Firsat": 5, "Risk": 95, 
        "Aciklama": "Borsa batışı veya hack gibi olaylarla güvenin sıfırlandığı kaos ortamı."
    },
    "AKUMULASYON_MAL_TOPLAMA": {
        "Firsat": 50, "Risk": 50, 
        "Aciklama": "Bezdirici yatay seyir. Balinaların sessizce mal topladığı dönem."
    },
    "KURUMSAL_GIRIS_TRENDI": {
        "Firsat": 65, "Risk": 35, 
        "Aciklama": "ETF/Şirket alımları ile gelen sağlıklı ve istikrarlı yükseliş."
    }
}

# ==============================================================================
# 📡 2. GERÇEK ZAMANLI VERİ MOTORLARI
# ==============================================================================

async def get_twitter_rotasyonlu():
    """Hesapları sırayla dener, biri çalışırsa veriyi çeker."""
    print("   🐦 Twitter (X) Bağlanıyor (Çoklu Hesap Modu)...")
    veriler = []
    
    for hesap in TWITTER_HESAPLARI:
        print(f"      🔄 {hesap['id']} deneniyor...")
        
        try:
            client = Client('en-US')
            
            # --- DÜZELTME 1: Twitter Kütüphanesi Güncellendiği için formatı düzelttim ---
            cookies = {
                'auth_token': hesap['auth_token'],
                'ct0': hesap['ct0']
            }
            client.set_cookies(cookies)
            # --------------------------------------------------------------------------
            
            # Popüler Kripto Tweetlerini Çek
            tweets = await client.search_tweet('Bitcoin OR Crypto OR Altseason', product='Top')
            
            if not tweets:
                print(f"      ❌ {hesap['id']} giriş yaptı ama tweet bulamadı.")
                continue

            for tweet in tweets:
                veriler.append(tweet.text)
            
            print(f"      ✅ BAŞARILI: {hesap['id']} üzerinden {len(veriler)} tweet çekildi.")
            return veriler # Veriyi aldık, döngüden çık
            
        except Exception as e:
            # Hata mesajını kısaltarak göster
            hata_mesaji = str(e).split('\n')[0][:100]
            print(f"      ❌ {hesap['id']} BAŞARISIZ. Hata: {hata_mesaji}...")
            print("      👉 Sıradaki hesaba geçiliyor...")
            continue
    
    print("   ❌❌ TÜM HESAPLAR DENENDİ, HİÇBİRİ VERİ ÇEKEMEDİ.")
    return []

def twitter_verisi_cek():
    """Asenkron fonksiyonu çalıştırır."""
    return asyncio.run(get_twitter_rotasyonlu())

def youtube_verisi_cek():
    """YouTube API ile SON 30 GÜNÜN popüler videolarını tarar."""
    print("   ▶️  YouTube API Bağlanıyor...")
    veriler = []
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        
        bir_ay_once = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
        bir_ay_once = bir_ay_once.replace("+00:00", "Z") 

        # --- DÜZELTME 2: 'part' parametresi eklendi (Hata veriyordu) ---
        search = youtube.search().list(
            part="snippet",
            q="Bitcoin Price Prediction", 
            type="video", 
            order="viewCount",
            publishedAfter=bir_ay_once,
            maxResults=5
        ).execute()
        # ---------------------------------------------------------------
        
        for item in search['items']:
            vid_id = item['id']['videoId']
            try:
                comments = youtube.commentThreads().list(
                    videoId=vid_id, part="snippet", maxResults=20, textFormat="plainText"
                ).execute()
                for comm in comments['items']:
                    veriler.append(comm['snippet']['topLevelComment']['snippet']['textDisplay'])
            except: continue 
                
        print(f"      ✅ {len(veriler)} adet YouTube Yorumu işlendi.")
        return veriler
    except Exception as e:
        print(f"      ❌ YouTube Hatası: {e}")
        return []

def haber_verisi_cek():
    print("   📰 Global Haber Akışı Taranıyor...")
    urls = ["https://cointelegraph.com/rss", "https://www.coindesk.com/arc/outboundfeeds/rss/"]
    basliklar = []
    for url in urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                basliklar.append(entry.title)
        except: continue
    print(f"      ✅ {len(basliklar)} adet Manşet incelendi.")
    return basliklar

def fiyat_verisi_cek():
    try:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=true"
        data = requests.get(url).json()
        change_30d = data['market_data']['price_change_percentage_30d']
        fiyat = data['market_data']['current_price']['usd']
        return fiyat, change_30d
    except:
        return 0, 0

# ==============================================================================
# 🧠 3. ANA ANALİZ MERKEZİ
# ==============================================================================
def baslat():
    print("\n" + "█"*70)
    print("       NEXUS AI: MULTI-ACCOUNT PİYASA PROJEKSİYONU")
    print("       (Yedekli Hesap Sistemi Devrede - V4 Final)")
    print("█"*70 + "\n")

    # 1. Beyni Yükle
    if not os.path.exists(MODEL_DOSYASI):
        print(f"❌ HATA: '{MODEL_DOSYASI}' bulunamadı! Önce eğitimi yap.")
        return

    model = joblib.load(MODEL_DOSYASI)
    vectorizer = joblib.load(VEKTOR_DOSYASI)
    print("🧠 Yapay Zeka Hafızası Yüklendi.")

    # 2. Veri Topla
    print("\n📡 VERİ TOPLAMA SÜRECİ BAŞLATILIYOR...")
    
    twitter_data = twitter_verisi_cek()
    youtube_data = youtube_verisi_cek()
    haber_data = haber_verisi_cek()
    btc_fiyat, btc_degisim = fiyat_verisi_cek()

    tum_veri = twitter_data + youtube_data + haber_data
    
    if len(tum_veri) == 0:
        print("\n⚠️ HATA: İnternetten hiçbir veri çekilemedi. Bağlantıları kontrol et.")
        return

    # 3. Analiz Et
    print(f"\n⚙️ Toplanan {len(tum_veri)} adet veri noktası AI süzgecinden geçiriliyor...")
    vektorler = vectorizer.transform(tum_veri)
    tahminler = model.predict(vektorler)

    firsat_sayisi = np.sum(tahminler == "FIRSAT_YUKSELIS")
    risk_sayisi = np.sum(tahminler == "RISK_DUSUS")
    toplam = len(tahminler)
    if toplam == 0: toplam = 1

    firsat_orani = (firsat_sayisi / toplam) * 100
    risk_orani = (risk_sayisi / toplam) * 100

    # 4. Döngü Eşleştirme (Cycle Matching)
    en_yakin_dongu = ""
    en_kucuk_fark = 1000
    for dongu, oranlar in PIYASA_DONGULERI.items():
        # Öklid mesafesi ile en yakın döngüyü bul
        fark = abs(firsat_orani - oranlar["Firsat"]) + abs(risk_orani - oranlar["Risk"])
        if fark < en_kucuk_fark:
            en_kucuk_fark = fark
            en_yakin_dongu = dongu

    # 5. FİNAL RAPORU
    print("\n" + "="*60)
    print(f"📊 PİYASA DURUM RAPORU ({datetime.now().strftime('%d-%m-%Y')})")
    print("="*60)
    
    yon_ikon = '🚀' if btc_degisim > 0 else '🔻'
    print(f"💰 Bitcoin Fiyatı: ${btc_fiyat:,.2f}")
    print(f"📈 30 Günlük Değişim: {yon_ikon} %{btc_degisim:.2f}")
    
    print("-" * 60)
    print(f"🧠 AI Sentiment Analizi:  %{firsat_orani:.1f} FIRSAT | %{risk_orani:.1f} RİSK")
    print("-" * 60)
    
    print("\n⏳ PİYASA DÖNGÜ ANALİZİ (Market Cycle Detection)")
    print(f"   Son 30 günlük veriler şu döngüye işaret ediyor:")
    print(f"   👉 [{en_yakin_dongu}]")
    print(f"   📝 {PIYASA_DONGULERI[en_yakin_dongu]['Aciklama']}")

    print("\n📢 GELECEK ÖNGÖRÜSÜ VE STRATEJİ")
    
    if firsat_orani > 65:
        print("   ✅ KARAR: BOĞA PİYASASI (STRONG BUY)")
        print("   • Toplulukta ciddi bir iştah var. Döngü yükselişi destekliyor.")
        print("   • STRATEJİ: Düşüşleri alım fırsatı olarak değerlendir.")
    elif risk_orani > 60:
        print("   🔻 KARAR: AYI PİYASASI (STRONG SELL/WAIT)")
        print("   • Verilerde korku hakim. Döngü düşüş yönünde.")
        print("   • STRATEJİ: Nakite geç, dip oluşumunu bekle.")
    else:
        print("   ⚖️ KARAR: TESTERE PİYASASI (HOLD)")
        print("   • Piyasa kararsız. Akümülasyon döngüsü olabilir.")
        print("   • STRATEJİ: Mevcut pozisyonlarını koru, ani hareket yapma.")

    print("\n" + "="*60)

if __name__ == "__main__":
    baslat()