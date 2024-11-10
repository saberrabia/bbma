import ccxt
import pandas as pd
import asyncio
from telegram import Bot

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
     'WIF/USDT', '1MBABYDOGE/USDT', 'ENA/USDT', 'WLD/USDT',
    'POPCAT/USDT', 'EIGEN/USDT', 'DOGE/USDT', 'DOGS/USDT', 'SAGA/USDT',
    'TAO/USDT', 'TIA/USDT', 'SEI/USDT', 'SXP/USDT', 'REEF/USDT',
    'TURBO/USDT', 'BNB/USDT', '1000SHIB/USDT', 'ORDI/USDT', 'FTM/USDT',
    'AVAX/USDT', 'XRP/USDT', 'PEOPLE/USDT', 'MEW/USDT', 'APT/USDT',
    'UNI/USDT', 'AXL/USDT', 'BANANA/USDT', 'CATI/USDT', 'ARKM/USDT',
    'FET/USDT', 'NOT/USDT', 'NEAR/USDT', '1000SATS/USDT', 'BOME/USDT',
    'CELO/USDT', 'DIA/USDT', '1000BONK/USDT', 'MYRO/USDT', '1000FLOKI/USDT',
    'ARK/USDT', 'HMSTR/USDT', 'LINK/USDT', 'OP/USDT', 'AAVE/USDT',
    'FIL/USDT', 'ADA/USDT', 'IO/USDT', 'ARB/USDT', 'BIGTIME/USDT',
    'INJ/USDT', 'BCH/USDT', 'TRX/USDT', 'TON/USDT', 'CFX/USDT',
    '1000RATS/USDT', 'GALA/USDT', 'OM/USDT', 'DOT/USDT', 'ZRO/USDT',
    'STX/USDT', 'ZEC/USDT', 'ALT/USDT', 'CHZ/USDT', 'ETHFI/USDT',
    'PHB/USDT', 'REZ/USDT', 'HIFI/USDT', 'RUNE/USDT', 'UXLINK/USDT',
    'ETC/USDT', 'LTC/USDT', 'GAS/USDT', 'DYDX/USDT', 'W/USDT',
    'ONDO/USDT', 'PENDLE/USDT', 'RENDER/USDT', 'SUN/USDT', 'DYM/USDT',
    'BNX/USDT', 'XAI/USDT', 'CRV/USDT', 'MEME/USDT', 'AR/USDT',
    'SUPER/USDT', 'TRB/USDT', 'FIDA/USDT', 'STRK/USDT', 'JUP/USDT',
    'LISTA/USDT', 'CKB/USDT', 'JTO/USDT', 'MKR/USDT', 'LDO/USDT',
    'ATOM/USDT', 'JASMY/USDT', 'ZK/USDT', 'ENS/USDT', 'ORBS/USDT',
    'APE/USDT', 'POL/USDT', 'BLUR/USDT', 'VIDT/USDT', 'ICP/USDT',
    'ZETA/USDT', 'GRT/USDT', 'AI/USDT', 'BB/USDT', 'ETHW/USDT',
    'SUSHI/USDT', 'STORJ/USDT', 'EOS/USDT', 'VANRY/USDT', 'KAVA/USDT',
    'RARE/USDT', 'OMNI/USDT', 'SYN/USDT', 'NEO/USDT', 'KAS/USDT',
    'IMX/USDT', 'AXS/USDT', 'GMT/USDT', 'THETA/USDT', 'SAND/USDT',
    '1000LUNC/USDT', 'PIXEL/USDT', 'ROSE/USDT', 'DAR/USDT', 'UMA/USDT',
    'AEVO/USDT', 'MANTA/USDT', 'XLM/USDT', 'YGG/USDT', 'MINA/USDT',
    'UNFI/USDT', 'LPT/USDT', 'BEAMX/USDT', 'NFP/USDT', 'USTC/USDT',
    'BAKE/USDT', 'BRETT/USDT', 'HBAR/USDT', 'PORTAL/USDT', 'LQTY/USDT',
    'POWR/USDT', 'PYTH/USDT', 'KDA/USDT', 'COTI/USDT', 'BSW/USDT',
    'MASK/USDT', 'CYBER/USDT', 'WOO/USDT', 'TNSR/USDT', 'POLYX/USDT',
    'XMR/USDT', 'ACH/USDT', 'GLM/USDT', 'ONG/USDT', 'SSV/USDT',
    'ALPACA/USDT', 'FIO/USDT', 'MAVIA/USDT', 'RDNT/USDT', 'TRU/USDT',
    'KEY/USDT', 'HOOK/USDT', 'EGLD/USDT', 'TWT/USDT', 'MANA/USDT',
    'TOKEN/USDT', 'VET/USDT', 'ALGO/USDT', 'LUNA2/USDT', 'DUSK/USDT',
    'ACE/USDT', '1000XEC/USDT', 'AGLD/USDT', 'WAXP/USDT', 'RSR/USDT',
    'SNX/USDT', '1INCH/USDT', 'FLOW/USDT', 'HIGH/USDT', 'EDU/USDT',
    'ONE/USDT', 'JOE/USDT', 'CAKE/USDT', 'LOOM/USDT', 'IOTX/USDT',
    'GTC/USDT', 'METIS/USDT', 'ONT/USDT', 'COMP/USDT', 'ZIL/USDT',
    'ZEN/USDT', 'CHR/USDT', 'MBOX/USDT', 'API3/USDT', 'G/USDT',
    'AMB/USDT', 'ASTR/USDT', 'VOXEL/USDT', 'AUCTION/USDT', 'ALICE/USDT',
    'ID/USDT', 'BOND/USDT', 'RONIN/USDT', 'XTZ/USDT', 'MAV/USDT',
    'QNT/USDT', 'RVN/USDT', 'ILV/USDT', 'NMR/USDT', 'SYS/USDT',
    'IOTA/USDT', 'QTUM/USDT', 'GMX/USDT', 'REN/USDT', 'STMX/USDT',
    'MTL/USDT', 'FXS/USDT', 'BICO/USDT', 'LRC/USDT', 'BEL/USDT',
    'COS/USDT', 'LINA/USDT', 'AERGO/USDT', 'BAND/USDT', 'ENJ/USDT',
    'BLZ/USDT', 'DODO/USDT', 'CELR/USDT', 'LEVER/USDT', 'SKL/USDT',
    'OMG/USDT', 'REI/USDT', 'NULS/USDT', 'MAGIC/USDT', 'YFI/USDT',
    'HOT/USDT', 'MOVR/USDT', 'QUICK/USDT', 'T/USDT', 'ZRX/USDT',
    'FLM/USDT', 'RIF/USDT', 'KSM/USDT', 'DASH/USDT', 'TLM/USDT',
    'LOKA/USDT', 'XVG/USDT', 'C98/USDT', 'NTRN/USDT', 'IOST/USDT',
    'BSV/USDT', 'ATA/USDT', 'ALPHA/USDT', 'RPL/USDT', 'GHST/USDT',
    'SPELL/USDT', 'FLUX/USDT', 'KLAY/USDT', 'ANKR/USDT', 'RLC/USDT',
    'BAL/USDT', 'BAT/USDT', 'CTSI/USDT', 'OGN/USDT', 'STG/USDT',
    'KNC/USDT', 'STEEM/USDT', 'PERP/USDT', 'CHESS/USDT', 'LIT/USDT',
    'BADGER/USDT', 'ICX/USDT', 'SFP/USDT', 'XVS/USDT', 'NKN/USDT',
    'ARPA/USDT', 'DENT/USDT', 'XEM/USDT', 'BTCDOM/USDT', 'COMBO/USDT',
    'OXT/USDT', 'HFT/USDT', 'BNT/USDT', 'LSK/USDT', 'DEFI/USDT',
]

# متغير لحفظ الحالة السابقة (شراء أو بيع) لكل رمز
previous_signals = {symbol: None for symbol in symbols}

# إنشاء Semaphore لحد تحديد عدد الرسائل المرسلة في نفس الوقت
semaphore = asyncio.Semaphore(10)  # يمكنك تحديد العدد بناءً على احتياجاتك

# دالة غير متزامنة لإرسال الرسالة عبر تلغرام
async def send_message_to_telegram(message):
    async with semaphore:  # تأكد من أن عدد الرسائل المرسلة في نفس الوقت محدود
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            # إضافة تأخير بسيط بين إرسال الرسائل (100 مللي ثانية)
            await asyncio.sleep(0.1)
        except Exception as e:
            print(f"فشل في إرسال الرسالة: {e}")

# دالة لتحميل البيانات وتحليلها
async def fetch_and_analyze(symbol):
    global previous_signals  # نستخدم المتغير السابق من خارج الدالة

    # تحميل البيانات التاريخية من بينانس
    ohlcv = binance.fetch_ohlcv(symbol, '1m', limit=100)

    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # حساب مستويات الدعم والمقاومة
    lookback_period = 100
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
        # تنفيذ جميع المهام بشكل غير متزامن
        await asyncio.gather(*tasks)
        await asyncio.sleep(60)  # الانتظار لمدة 60 ثانية قبل التحليل التالي

# تشغيل الحلقة غير المتزامنة باستخدام asyncio
if __name__ == "__main__":
    asyncio.run(main())
