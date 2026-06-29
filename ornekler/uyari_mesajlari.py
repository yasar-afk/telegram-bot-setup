"""
Ornek 2: Uyari Mesajlari
"""

from telegram_notify import TelegramNotifier

notifier = TelegramNotifier()

# Farkli seviyelerde uyari mesajlari
notifier.send_alert("Basarili", "Islem basariyla tamamlandi!", level="success")
notifier.send_alert("Dikkat", "Bakiyeniz dusuk!", level="warning")
notifier.send_alert("Hata", "Baglanti hatasi olustu!", level="error")
notifier.send_alert("Bilgi", "Sistem guncellendi", level="info")
