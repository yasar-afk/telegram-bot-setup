"""
Telegram Bot Test Dosyasi
"""

import os
import sys
from dotenv import load_dotenv

# .env dosyasini yukle
load_dotenv()

def test_telegram():
    """Telegram botunu test eder"""
    print("=" * 50)
    print("  TELEGRAM BOT TEST")
    print("=" * 50)
    print()

    # Token kontrolu
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token:
        print("HATA: TELEGRAM_BOT_TOKEN ayarlanmamis!")
        print()
        print("Cozum:")
        print("1. .env dosyasini acin")
        print("2. TELEGRAM_BOT_TOKEN=BOT_TOKENINIZ seklinde yazin")
        print("3. BotFather'dan token alin: https://t.me/BotFather")
        return False

    if not chat_id:
        print("HATA: TELEGRAM_CHAT_ID ayarlanmamis!")
        print()
        print("Cozum:")
        print("1. .env dosyasini acin")
        print("2. TELEGRAM_CHAT_ID=CHAT_IDNIZ seklinde yazin")
        print("3. Chat ID'nizi ogrenin: https://t.me/userinfobot")
        return False

    print(f"Bot Token: {token[:10]}...{token[-5:]}")
    print(f"Chat ID: {chat_id}")
    print()

    # Kutuphane kontrolu
    try:
        from telegram_notify import TelegramNotifier
        print("[OK] telegram-notify kütüphanesi yüklü")
    except ImportError:
        print("HATA: telegram-notify kütüphanesi yüklü degil!")
        print()
        print("Kurulum:")
        print("pip install git+https://github.com/yasar-afk/telegram-notify.git")
        return False

    # Test mesaji
    print()
    print("Test mesaji gonderiliyor...")

    notifier = TelegramNotifier(bot_token=token, chat_id=chat_id)

    test_message = """🤖 <b>Telegram Bot Test</b>

Bu bir test mesajidir.

✅ Bot basariyla calisiyor!
📅 Tarih: Test zamani

<i>Bu mesaj test_bot.py ile gonderilmistir.</i>"""

    if notifier.send_html(test_message):
        print()
        print("=" * 50)
        print("  TEST BASARILI!")
        print("=" * 50)
        print()
        print("Telegram'iniza test mesaji gonderildi!")
        print()
        print("Artik projelerinizde kullanabilirsiniz:")
        print()
        print('  from telegram_notify import TelegramNotifier')
        print('  notifier = TelegramNotifier()')
        print('  notifier.send("Merhaba!")')
        return True
    else:
        print()
        print("HATA: Test mesaji gonderilemedi!")
        print()
        print("Muhtemel nedenler:")
        print("1. Token hatali")
        print("2. Chat ID hatali")
        print("3. Bota ilk mesaji gondermediniz")
        print("4. Internet baglantisi yok")
        return False

if __name__ == "__main__":
    success = test_telegram()
    sys.exit(0 if success else 1)
