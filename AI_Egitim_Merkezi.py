import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==============================================================================
# AYARLAR (Okunacak Excel Dosyası)
# ==============================================================================
# Masaüstündeki en son oluşturduğumuz dosyanın tam adını buraya yazıyoruz
VERI_DOSYASI = "KRIPTO_FINAL_RAPOR_VE_KONULAR.xlsx" 

MODEL_DOSYASI = "KRIPTO_AI_BEYNI.pkl"
VEKTOR_DOSYASI = "KELIME_VEKTORU.pkl"

def egitimi_baslat():
    print("🧠 YAPAY ZEKA EĞİTİM MODÜLÜ BAŞLATILIYOR...")
    
    # Masaüstü yolunu bul
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    dosya_yolu = os.path.join(desktop_path, VERI_DOSYASI)
    
    # 1. Veriyi Yükle
    print(f"📂 Veri seti aranıyor: {dosya_yolu}")
    if not os.path.exists(dosya_yolu):
        # Belki dosya masaüstünde değildir, direkt olduğu yerde arayalım
        if os.path.exists(VERI_DOSYASI):
            dosya_yolu = VERI_DOSYASI
        else:
            print(f"❌ HATA: '{VERI_DOSYASI}' dosyası bulunamadı! Önceki 'Final_Bitirici.py' kodunu çalıştırıp Excel'i ürettin mi?")
            return

    # Excel'i oku
    try:
        df = pd.read_excel(dosya_yolu, sheet_name=0) # İlk sayfayı oku
    except:
        print("❌ Excel dosyası okunamadı. Dosya bozuk veya açık olabilir.")
        return
        
    # Veri temizliği
    df = df.dropna(subset=['Content']) # İçeriği boş olanları at
    
    print(f"📊 Toplam {len(df)} satır veri işleme alındı.")

    # --- ETİKETLEME (LABELING) ---
    # Makineye neyin ne olduğunu öğretiyoruz
    print("🏷️ Veriler sınıflandırılıyor (Risk vs Fırsat)...")
    
    def etiketle(row):
        # Eğer kolon isimleri büyük/küçük harf farklıysa diye önlem alıyoruz
        risk = row.get('RISK_Score', row.get('Risk_Skor', 0))
        opp = row.get('OPP_Score', row.get('Firsat_Skor', 0))
        
        if risk > opp and risk >= 1:
            return "RISK_DUSUS"
        elif opp > risk and opp >= 1:
            return "FIRSAT_YUKSELIS"
        else:
            return "NOTR_BELIRSIZ"

    df['SINIF'] = df.apply(etiketle, axis=1)
    
    # Sınıf dağılımını göster
    print(df['SINIF'].value_counts())

    # 2. Vektörleştirme (Yazıyı Sayıya Çevirme)
    print("🔢 Metinler matematiğe çevriliyor (TF-IDF)...")
    
    # Bilgisayarı kasmaması için max 5000 kelime özelliği kullanıyoruz
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X = vectorizer.fit_transform(df['Content'].astype(str))
    y = df['SINIF']

    # 3. Eğitim
    print("🤖 Model eğitiliyor (Bu işlem 1-2 dakika sürebilir)...")
    # Random Forest algoritması kullanıyoruz
    classifier = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
    classifier.fit(X, y)

    # 4. Kaydet
    print("💾 Beyin dosyaları masaüstüne kaydediliyor...")
    
    # Dosyaları masaüstüne kaydedelim ki diğer kod bulabilsin
    model_yolu = os.path.join(desktop_path, MODEL_DOSYASI)
    vektor_yolu = os.path.join(desktop_path, VEKTOR_DOSYASI)
    
    joblib.dump(classifier, model_yolu)
    joblib.dump(vectorizer, vektor_yolu)
    
    print("\n" + "="*60)
    print("✅ EĞİTİM TAMAMLANDI!")
    print(f"🧠 Beyin Dosyası: {model_yolu}")
    print(f"📖 Kelime Dosyası: {vektor_yolu}")
    print("👉 ŞİMDİ 'a.py' (Strateji Uzmanı) KODUNU ÇALIŞTIRABİLİRSİN.")
    print("="*60)

if __name__ == "__main__":
    egitimi_baslat()