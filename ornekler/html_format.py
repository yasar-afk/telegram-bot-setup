"""
Ornek 3: HTML Formatinda Mesaj
"""

from telegram_notify import TelegramNotifier

notifier = TelegramNotifier()

html_mesaj = """
<b>📊 Gunluk Rapor</b>

<i>Durum Ozeti:</i>
• Toplam Islem: <b>25</b>
• Basarili: <b>22</b>
• Basarisiz: <b>3</b>

<b>Kar/Zarar: +$1,250.50</b>

<i>Son guncelleme: 15:30</i>
"""

notifier.send_html(html_mesaj)
