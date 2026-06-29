@echo off
chcp 65001 >nul
title Telegram Bot Kurulum
color 0B

echo.
echo ========================================
echo    TELEGRAM BOT KURULUM REHBERI
echo ========================================
echo.
echo  Bu sihirbaz size Telegram botunuzu
echo  kurmanizda yardimci olacak.
echo.
echo ========================================
echo.

:: Python kontrolu
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo HATA: Python bulunamadi!
    echo.
    echo Python'u indirmek icin: https://www.python.org/downloads/
    echo Kurulum sirasinda "Add Python to PATH" secenegini isaretleyin!
    echo.
    pause
    exit /b 1
)

echo [1/6] Python kontrolu tamamlandi.
echo.

:: Kütüphane kontrolü
echo [2/6] Gerekli kütüphaneler kontrol ediliyor...
echo.

pip install requests >nul 2>&1
if %errorlevel% neq 0 (
    echo   requests kütüphanesi kuruluyor...
    pip install requests
)

echo   [OK] requests
echo.

:: .env dosyası oluştur
echo [3/6] .env dosyasi olusturuluyor...
echo.

if exist .env (
    echo   .env dosyasi mevcut, uzerine yazilsin mi? (E/H)
    set /p OVERWRITE=
    if /i not "%OVERWRITE%"=="E" (
        echo   Mevcut .env dosyasi korundu.
        goto SKIP_ENV
    )
)

echo # Telegram Bot Ayarlari > .env
echo # Bu dosyayi kendi degerlerinizle doldurun >> .env
echo. >> .env
echo # Bot token'unu BotFather'dan alin >> .env
echo # https://t.me/BotFather >> .env
echo TELEGRAM_BOT_TOKEN= >> .env
echo. >> .env
echo # Chat ID'nizi ogrenmek icin >> .env
echo # https://t.me/userinfobot >> .env
echo TELEGRAM_CHAT_ID= >> .env

echo   .env dosyasi olusturuldu!
echo.

:SKIP_ENV
echo [4/6] Bot bilgileri girisi...
echo.
echo ========================================
echo   ONCELIKLE TELEGRAM BOTUNUZU OLUSTURUN
echo ========================================
echo.
echo   Adim 1: Telegram'da @BotFather'a gidin
echo   Adim 2: /newbot komutunu yazin
echo   Adim 3: Bot adinizi girin
echo   Adim 4: Kullanici adinizi girin (_bot ile bitmeli)
echo   Adim 5: Token'i kopyalayin
echo.
echo   Chat ID icin:
echo   - @userinfobot'a gidin
echo   - /start yazin
echo   - Chat ID'nizi ogrenin
echo.
echo ========================================
echo.

set /p BOT_TOKEN="Bot Token'unuzu girin: "
set /p CHAT_ID="Chat ID'nizi girin: "

if "%BOT_TOKEN%"=="" (
    echo HATA: Bot Token gerekli!
    pause
    exit /b 1
)

if "%CHAT_ID%"=="" (
    echo HATA: Chat ID gerekli!
    pause
    exit /b 1
)

:: .env dosyasını güncelle
echo # Telegram Bot Ayarlari > .env
echo TELEGRAM_BOT_TOKEN=%BOT_TOKEN% >> .env
echo TELEGRAM_CHAT_ID=%CHAT_ID% >> .env

echo.
echo   [OK] Bot bilgileri kaydedildi!
echo.

:: Kütüphane kurulumu
echo [5/6] telegram-notify kütüphanesi kuruluyor...
echo.

pip install git+https://github.com/yasar-afk/telegram-notify.git >nul 2>&1
if %errorlevel% neq 0 (
    echo   Kurulum basarisiz! Manuel kurulum deneyin:
    echo   pip install git+https://github.com/yasar-afk/telegram-notify.git
) else (
    echo   [OK] telegram-notify kuruldu!
)

echo.

:: Test
echo [6/6] Test mesaji gonderiliyor...
echo.

python -c "
import os
from dotenv import load_dotenv
load_dotenv()

from telegram_notify import TelegramNotifier

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

if not token or not chat_id:
    print('HATA: Token veya Chat ID eksik!')
    exit(1)

notifier = TelegramNotifier(bot_token=token, chat_id=chat_id)

if notifier.send('🤖 Telegram Bot basariyla kuruldu!\n\nBu mesaj test amacli gonderilmistir.'):
    print('[OK] Test mesaji basariyla gonderildi!')
    print()
    print('Artik projelerinizde telegram-notify kullanabilirsiniz:')
    print()
    print('  from telegram_notify import TelegramNotifier')
    print('  notifier = TelegramNotifier()')
    print('  notifier.send(\"Merhaba Dunya!\")')
else:
    print('HATA: Test mesaji gonderilemedi!')
    print()
    print('Kontrol edin:')
    print('  1. Token dogru mu?')
    print('  2. Chat ID dogru mu?')
    print('  3. Bota ilk mesaji gonderdiniz mi?')
"

echo.
echo ========================================
echo    KURULUM TAMAMLANDI!
echo ========================================
echo.
echo  Sonraki adimlar:
echo  1. .env dosyasini kontrol edin
echo  2. Bot ile test mesaji gonderin
echo  3. Projenizde kullanmaya baslayin
echo.
echo  Dokumantasyon: README.md
echo  Ornekler: ornekler/ klasoru
echo.
echo ========================================
echo.
pause
