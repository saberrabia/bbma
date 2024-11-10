import ccxt
import pandas as pd
import asyncio
from telegram import Bot, ParseMode
from telegram.ext import ApplicationBuilder
from datetime import datetime, timedelta

# إعداد اتصال مع بينانس
binance = ccxt.binance({
    'enableRateLimit': True  # لتجنب التكرار الزائد في الاستعلامات
})

# إعداد بيانات الاتصال بالبوت
telegram_token = '7881688707:AAEHc_15-NzaGuGtwT51ZvmFOt5PKhQ0dwI'
chat_id = '7039034340'
bot = Bot(token=telegram_token)

# العملات التي سيتم مراقبتها
symbols = [
    'BTC/USDT', 'ETH/USDT', 'NEIRO/USDT', 'SOL/USDT', '1000PEPE/USDT',
    'WIF/USDT', '1MBABYDOGE/USDT', 'ENA/USDT', 'WLD/USDT', 'POPCAT/USDT',
    'EIGEN/USDT', 'DOGE/USDT', 'DOGS/USDT', 'SAGA/USDT', 'TAO/USDT', 'TIA/USDT',
    'SEI/USDT', 'SXP/USDT', 'REEF/USDT', 'TURBO/USDT', 'BNB/USDT', '1000SHIB/USDT',
    'ORDI/USDT', 'FTM/USDT', 'AVAX/USDT', 'XRP/USDT', 'PEOPLE/USDT', 'MEW/USDT',
    'APT/USDT', 'UNI/USDT', 'AXL/USDT', 'BANANA/USDT', 'CATI/USDT', 'ARKM/USDT',
    'FET/USDT', 'NOT/USDT', 'NEAR/USDT', '1000SATS/USDT', 'BOME/USDT', 'CELO/USDT',
    'DIA/USDT', '1000BONK/USDT', 'MYRO/USDT', '1000FLOKI/USDT', 'ARK/USDT', 'HMSTR/USDT',
]

# متغير لحفظ الحالة السابقة (شراء أو بيع) لكل رمز
previous_signals = {symbol: None for symbol in symbols}

# Semaphore لتحكم في عدد الرسائل المرسلة في وقت واحد
semaphore = asyncio.Semaphore(10)

# دالة غير متزامنة لإرسال الرسالة عبر تلغرام
async def send_message_to_telegram(message):
    async with semaphore:
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(f"فشل في إرسال الرسالة: {e}")

# دالة لتحميل البيانات وتحليلها
async def fetch_and_analyze(symbol):
    global previous_signals

    # تحميل البيانات التاريخية من بينانس
    ohlcv = binance.fetch_ohlcv(symbol, '1m', limit=100)

    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # حساب مستويات الدعم والمقاومة
    lookback_period = 20
    df['highest_high'] = df['high'].rolling(window=lookback_period).max()
    df['lowest_low'] = df['low'].rolling(window=lookback_period).min()

    # تحديد الإشارة الحالية
    latest_row = df.iloc[-1]
    current_signal = None

    if latest_row['high'] >= latest_row['highest_high']:
        current_signal = "BUY"
    elif latest_row['low'] <= latest_row['lowest_low']:
        current_signal = "SELL"

    # تحقق من تغيير الحالة
    if current_signal != previous_signals[symbol]:
        if current_signal == "BUY":
            message = f"إشارة شراء للرمز {symbol}: القمة الحالية تلامس أو تتجاوز مستوى المقاومة"
            print(message)
            await send_message_to_telegram(message)
        elif current_signal == "SELL":
            message = f"إشارة بيع للرمز {symbol}: القاع الحالي تلامس أو تتجاوز مستوى الدعم"
            print(message)
            await send_message_to_telegram(message)

        # تحديث الحالة السابقة
        previous_signals[symbol] = current_signal

# دالة غير متزامنة لتشغيل التحليل على كل الرموز
async def main():
    while True:
        tasks = [fetch_and_analyze(symbol) for symbol in symbols]
        await asyncio.gather(*tasks)  # تنفيذ جميع المهام بشكل غير متزامن
        await asyncio.sleep(60)  # الانتظار لمدة 60 ثانية قبل التحليل التالي

# تشغيل الحلقة غير المتزامنة باستخدام asyncio
if __name__ == "__main__":
    asyncio.run(main())
