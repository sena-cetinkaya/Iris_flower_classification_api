# 🌼 Iris Çiçeği Tür Tahmini - FastAPI + ML + PostgreSQL

Bu proje, FastAPI framework'ü ile geliştirilmiş, **makine öğrenmesi** destekli bir web API'dir. Kullanıcı, iris çiçeği özelliklerini göndererek çiçeğin türünü tahmin ettirebilir veya yeni veri ekleyip modeli güncelleyebilir.

## 🚀 Proje Özellikleri

✅ Iris veri seti ile Random Forest model eğitimi  
✅ PostgreSQL veritabanı kullanımı  
✅ SQLModel ORM  
✅ FastAPI ile REST API oluşturma  
✅ Yeni veri eklenince modelin otomatik yeniden eğitilmesi  
✅ `/predict` ve `/add_data` endpoint'leri  
✅ `rf_model.pkl` dosyası ile modelin diske kaydedilmesi  

---

## 🗂️ Proje Yapısı

├── IRIS.csv # Ham iris veri seti

├── load_initial_data.py # CSV verisini veritabanına yükleyen script

├── classification_model_trainer.py # Veritabanından veri alıp modeli eğiten script

├── main.py # FastAPI uygulamasının giriş noktası

├── routes.py # API endpoint'leri

├── models.py # SQLModel sınıfları ve yardımcı DB fonksiyonları

├── rf_model.pkl # Eğitilmiş model (otomatik oluşur)

└── README.md # Bu dosya

---

## 🧠 Kullanılan Teknolojiler

- Python 3.10+
- FastAPI
- SQLModel
- PostgreSQL
- pandas
- scikit-learn
- pickle

---

## ⚙️ Kurulum ve Çalıştırma

### 1️⃣ Kütüphaneleri Yükle

```bash
pip install fastapi uvicorn pandas scikit-learn sqlmodel psycopg2-binary
```
2️⃣ PostgreSQL Ayarları
PostgreSQL’i kur

iris_db adında bir veritabanı oluştur

models.py ve load_initial_data.py içinde yer alan DATABASE_URL bağlantı bilgileri şu şekildedir:

postgresql://postgres:postgres@localhost:5432/iris_db

Gerekirse kullanıcı adı, şifre veya portu kendi ortamına göre değiştir.

3️⃣ Veritabanına İlk Veriyi Yükle
```bash
python load_initial_data.py
```
Bu komut:

iris_db içinde gerekli tabloyu oluşturur

IRIS.csv içeriğini veritabanına ekler

target sütununu sayısallaştırır

4️⃣ Modeli Eğit
```bash
python classification_model_trainer.py
```
Bu script:

Veritabanındaki tüm veriyi çeker (get_all_iris_data)

Random Forest ile modeli eğitir

rf_model.pkl adlı dosyaya modeli kaydeder

🚀 FastAPI Uygulamasını Başlat
```bash
uvicorn main:app --reload
```
Tarayıcıda http://localhost:8000/docs adresine giderek Swagger UI üzerinden test yapabilirsin.

🔌 API Endpoint’leri
📍 POST /predict
Verilen çiçek özelliklerine göre sınıf tahmini yapar.

Örnek istek:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
Yanıt:
```json
{
  "tahmin": "setosa"
}
```
📍 POST /add_data
Yeni iris verisi ekler ve modeli otomatik olarak yeniden eğitir.

Örnek istek:
```json
{
  "sepal_length": 6.2,
  "sepal_width": 3.4,
  "petal_length": 5.4,
  "petal_width": 2.3,
  "target": 2
}
```
Yanıt:
```json
{
  "mesaj": "Yeni veri eklendi ve model güncellendi."
}
```
Not: target değeri:

0 = setosa

1 = versicolor

2 = virginica

💾 Model Kaydetme ve Kullanma
Model rf_model.pkl adıyla pickle formatında kaydedilir ve tahminlerde bu dosya yüklenerek kullanılır. Yeni veri eklendiğinde bu dosya otomatik olarak güncellenir.

🧑‍💻 Geliştirici Notları
Veritabanı işlemleri SQLModel ile yapılmaktadır.

add_data() endpoint’i veriyi DB'ye ekledikten sonra train_model() fonksiyonunu çağırır.

rf_model.pkl dosyası yoksa /predict çağrısı hata verir.

🧪 Test
Swagger UI ile test için:

Uygulama çalışırken http://localhost:8000/docs adresine git.

Endpoint'leri kolayca deneyimle.

📃 Lisans
Bu proje MIT lisansı ile açık kaynak olarak paylaşılmıştır.
