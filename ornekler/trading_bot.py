"""
Ornek 4: Trading Bot Entegrasyonu
"""

from telegram_notify import TelegramNotifier
import time

class TradingBot:
    """Ornek Trading Bot"""
    
    def __init__(self):
        self.notifier = TelegramNotifier()
        self.portfoy = 10000  # Baslangic sermayesi
    
    def baslat(self):
        """Botu baslat"""
        self.notifier.send_alert(
            "Bot Baslatildi",
            f"Trading botu calismaya basladi.\nBakiye: ${self.portfoy:,.2f}",
            level="success"
        )
    
    def pozisyon_ac(self, coin, miktar, fiyat):
        """Pozisyon ac"""
        mesaj = f"""🟢 <b>Yeni Pozisyon</b>

Coin: {coin}
Miktar: {miktar}
Fiyat: ${fiyat:,.2f}
Toplam: ${miktar * fiyat:,.2f}"""
        
        self.notifier.send_html(mesaj)
    
    def pozisyon_kapat(self, coin, kar):
        """Pozisyon kapat"""
        emoji = "🟢" if kar > 0 else "🔴"
        durum = "KAR" if kar > 0 else "ZARAR"
        
        mesaj = f"""{emoji} <b>Pozisyon Kapatildi</b>

Coin: {coin}
{durum}: ${abs(kar):,.2f}
Guncel Bakiye: ${self.portfoy + kar:,.2f}"""
        
        self.portfoy += kar
        self.notifier.send_html(mesaj)
    
    def hata_olustu(self, hata_mesaji):
        """Hata bildir"""
        self.notifier.send_alert("Hata!", hata_mesaji, level="error")
    
    def gunluk_rapor(self):
        """Gunluk rapor gonder"""
        mesaj = f"""📊 <b>Gunluk Rapor</b>

Tarih: {time.strftime('%d.%m.%Y')}
Bakiye: ${self.portfoy:,.2f}
Durum: Aktif"""
        
        self.notifier.send_html(mesaj)


# Kullanim
if __name__ == "__main__":
    bot = TradingBot()
    
    # Botu baslat
    bot.baslat()
    
    # Ornek islemler
    time.sleep(1)
    bot.pozisyon_ac("BTC/USDT", 0.1, 45000)
    
    time.sleep(2)
    bot.pozisyon_kapat("BTC/USDT", 150.50)
    
    time.sleep(1)
    bot.gunluk_rapor()
