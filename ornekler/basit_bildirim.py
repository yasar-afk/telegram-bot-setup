"""
Ornek 1: Basit Bildirim
"""

from telegram_notify import TelegramNotifier

# Notifier olustur
notifier = TelegramNotifier()

# Mesaj gonder
notifier.send("Merhaba Dunya! Bu bir test mesajidir.")
