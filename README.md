# 🤖 Telegram Bot Kurulum Rehberi

Telegram botunuzu adım adım oluşturun ve projelerinize entegre edin.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 📋 İçindekiler

1. [Telegram Bot Nasıl Oluşturulur?](#-telegram-bot-nasıl-oluşturulur)
2. [Bot Token Nasıl Alınır?](#-bot-token-nasıl-alınır)
3. [Chat ID Nasıl Öğrenilir?](#-chat-id-nasıl-öğrenilir)
4. [Hızlı Kurulum](#-hızlı-kurulum)
5. [Projenize Entegre Etme](#-projenize-entegre-etme)
6. [Örnek Kodlar](#-örnek-kodlar)
7. [Sıkça Sorulan Sorular](#-sıkça-sorulan-sorular)

---

## 🎯 Telegram Bot Nasıl Oluşturulur?

### Adım 1: BotFather'ı Bulun

1. Telegram'ı açın
2. Arama çubuğuna **@BotFather** yazın
3. BotFather'ı bulup tıklayın
4. **Start** butonuna basın

### Adım 2: Yeni Bot Oluşturun

```
/newbot
```

BotFather size şu soruları soracak:

1. **Bot adı**: `Benim Botum` (görünür ad)
2. **Kullanıcı adı**: `benim_botum_bot` (benzersiz olmalı, `_bot` ile bitmeli)

### Adım 3: Token'ınızı Alın

BotFather size bir token verecek:

```
8123456789:AAH3kx9Jd8KHG9asjkdf87654321abcde
```

⚠️ **Bu token'ı güvenli saklayın!** Kimseye vermeyin.

---

## 🔑 Bot Token Nasıl Alınır?

Zaten bir botunuz varsa:

1. **@BotFather**'a gidin
2. `/mybot` komutunu yazın
3. Botunuzu seçin
4. **API Token** butonuna basın

---

## 📍 Chat ID Nasıl Öğrenilir?

### Yöntem 1: Bot ile

1. Botunuza bir mesaj gönderin
2. Bu URL'yi tarayıcınıza yapıştırın:
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
3. `"chat":{"id":123456789}` kısmındaki sayı Chat ID'nizdir

### Yöntem 2: Kodsuz

1. **@userinfobot**'a gidin
2. `/start` yazın
3. Chat ID'niz gösterilecek

### Yöntem 3: Grup için

1. Botunuzu gruba ekleyin
2. Gruba bir mesaj gönderin
3. Yukarıdaki URL'yi kontrol edin
4. Negatif bir sayı göreceksiniz (örn: `-123456789`)

---

## ⚡ Hızlı Kurulum

### 1. Bu Proje İndirin

```bash
git clone https://github.com/yasar-afk/telegram-bot-setup.git
cd telegram-bot-setup
```

### 2. BAT Dosyasını Çalıştırın

Windows'ta:
```
setup.bat'a çift tıklayın
```

Veya komut satırından:
```bash
setup.bat
```

### 3. Bilgilerinizi Girin

BAT dosyası sizden şunları isteyecek:
- Bot Token
- Chat ID

### 4. Test Edin

```bash
python test_bot.py
```

---

## 🔧 Projenize Entegre Etme

### Yöntem 1: telegram-notify Kütüphanesi ile

```bash
pip install git+https://github.com/yasar-afk/telegram-notify.git
```

```python
from telegram_notify import TelegramNotifier

notifier = TelegramNotifier(
    bot_token="BOT_TOKENINIZ",
    chat_id="CHAT_IDNIZ"
)

notifier.send("Merhaba Dunya!")
```

### Yöntem 2: Ortam Değişkenleri ile

**.env dosyası:**
```
TELEGRAM_BOT_TOKEN=8123456789:AAH3kx9Jd8KHG9asjkdf87654321abcde
TELEGRAM_CHAT_ID=123456789
```

**Python kodu:**
```python
from telegram_notify import TelegramNotifier

# Otomatik .env'den okur
notifier = TelegramNotifier()
notifier.send("Otomatik mesaj!")
```

### Yöntem 3: Doğrudan API Kullanımı

```python
import urllib.request
import urllib.parse

def telegram_mesaj_gonder(mesaj, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": mesaj
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        return response.status == 200

# Kullanım
telegram_mesaj_gonder("Hello!", "BOT_TOKEN", "CHAT_ID")
```

---

## 📝 Örnek Kodlar

### Basit Bildirim

```python
from telegram_notify import send_notification

send_notification("Bot baslatildi!")
```

### Uyarı Mesajları

```python
from telegram_notify import TelegramNotifier

notifier = TelegramNotifier()

# Farklı seviyeler
notifier.send_alert("Basarili", "Islem tamamlandi!", level="success")
notifier.send_alert("Dikkat", "Bakiye dusuk!", level="warning")
notifier.send_alert("Hata", "Baglanti kopuk!", level="error")
```

### HTML Formatında

```python
from telegram_notify import TelegramNotifier

notifier = TelegramNotifier()

notifier.send_html("""
<b>📊 Trading Bot Raporu</b>

<i>Gunluk Ozet:</i>
• Toplam Islem: 15
• Basarili: 12
• Basarisiz: 3

<b>K/Z: +$450.25</b>
""")
```

### Trading Bot Entegrasyonu

```python
from telegram_notify import TelegramNotifier

class TradingBot:
    def __init__(self):
        self.notifier = TelegramNotifier()
    
    def baslat(self):
        self.notifier.send_alert("Bot Baslatildi", "Trading basladi!")
    
    def pozisyon_ac(self, coin, miktar):
        self.notifier.send(f"🟢 Yeni pozisyon: {coin} - {miktar} USDT")
    
    def pozisyon_kapat(self, coin, kar):
        emoji = "🟢" if kar > 0 else "🔴"
        self.notifier.send(f"{emoji} {coin} kapatildi - K/Z: {kar} USDT")
    
    def hata(self, mesaj):
        self.notifier.send_alert("Hata!", mesaj, level="error")

# Kullanım
bot = TradingBot()
bot.baslat()
bot.pozisyon_ac("BTC/USDT", 100)
```

### Cron Job / Zamanlanmış Görev

```python
#!/usr/bin/env python3
from telegram_notify import send_notification
import schedule
import time

def gunluk_rapor():
    send_notification("📊 Saatlik rapor: Sistem calisiyor")

schedule.every(1).hours.do(gunluk_rapor)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## ❓ Sıkça Sorulan Sorular

### Bot token'ı nerede saklanmalı?

`.env` dosyasında saklayın ve `.gitignore`'a ekleyin:

```
# .gitignore
.env
```

### Bot çalışmıyor ne yapmalıyım?

1. Token'ın doğru olduğundan emin olun
2. Chat ID'nin doğru olduğundan emin olun
3. Botunuza ilk mesajı gönderdiğinizden emin olun
4. `python test_bot.py` ile test edin

### Gruba bot nasıl eklenir?

1. Gruba gidin
2. Grup ayarlarına tıklayın
3. "Üye Ekle" deyin
4. Botunuzu arayın ve ekleyin

### Birden fazla kişiye nasıl mesaj gönderilir?

Her kişi için ayrı Chat ID gerekir. Gruplar için negatif Chat ID kullanılır.

### Bot ne kadar hızlı mesaj gönderir?

Telegram API'si saniyede yaklaşık 30 mesaja izin verir. Toplu gönderimde gecikme olabilir.

---

## 🛠️ Sorun Giderme

### "HATA: Token gerekli" hatası

```python
# Yanlış
notifier = TelegramNotifier()

# Doğru
notifier = TelegramNotifier(
    bot_token="8123456789:AAH...",
    chat_id="123456789"
)
```

### "Chat not found" hatası

1. Botunuza ilk mesajı gönderin
2. Chat ID'nin doğru olduğunu kontrol edin
3. Botun grupta yetkisi olduğunu kontrol edin

### "Unauthorized" hatası

Token'ın doğru olduğundan emin olun. BotFather'dan yeni token alabilirsiniz.

---

## 📚 Faydalı Linkler

- [Telegram Bot API Dokümantasyonu](https://core.telegram.org/bots/api)
- [BotFather](https://t.me/BotFather)
- [Telegram Notify Kütüphanesi](https://github.com/yasar-afk/telegram-notify)

---

## 📝 Lisans

MIT License

---

**Telegram Bot Setup** — MiMoCode tarafından geliştirildi 🤖
