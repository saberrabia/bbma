import ccxt
import pandas as pd
import requests
import time

# إعداد الاتصال بمنصة بينانس باستخدام ccxt
exchange = ccxt.binance()

# قائمة العملات
symbols = [
    'BTC/USDT', 'ETH/USDT', 'NEIRO/USDT', 'SOL/USDT', '1000PEPE/USDT',
    'WIF/USDT', '1MBABYDOGE/USDT', 'ENA/USDT', 'WLD/USDT', 'POPCAT/USDT',
    'EIGEN/USDT', 'DOGE/USDT', 'DOGS/USDT', 'SAGA/USDT', 'TAO/USDT',
    'TIA/USDT', 'SEI/USDT', 'SXP/USDT', 'REEF/USDT', 'TURBO/USDT', 'BNB/USDT',
    '1000SHIB/USDT', 'ORDI/USDT', 'FTM/USDT', 'AVAX/USDT', 'XRP/USDT',
    'PEOPLE/USDT', 'MEW/USDT', 'APT/USDT', 'UNI/USDT', 'AXL/USDT', 'BANANA/USDT',
    'CATI/USDT', 'ARKM/USDT', 'FET/USDT', 'NOT/USDT', 'NEAR/USDT', '1000SATS/USDT',
    'BOME/USDT', 'CELO/USDT', 'DIA/USDT', '1000BONK/USDT', 'MYRO/USDT',
    '1000FLOKI/USDT', 'ARK/USDT', 'HMSTR/USDT', 'LINK/USDT', 'OP/USDT',
    'AAVE/USDT', 'FIL/USDT', 'ADA/USDT', 'IO/USDT', 'ARB/USDT', 'BIGTIME/USDT',
    'INJ/USDT', 'BCH/USDT', 'TRX/USDT', 'TON/USDT', 'CFX/USDT', '1000RATS/USDT',
    'GALA/USDT', 'OM/USDT', 'DOT/USDT', 'ZRO/USDT', 'STX/USDT', 'ZEC/USDT',
    'ALT/USDT', 'CHZ/USDT', 'ETHFI/USDT', 'PHB/USDT', 'REZ/USDT', 'HIFI/USDT',
    'RUNE/USDT', 'UXLINK/USDT', 'ETC/USDT', 'LTC/USDT', 'GAS/USDT', 'DYDX/USDT',
    'W/USDT', 'ONDO/USDT', 'PENDLE/USDT', 'RENDER/USDT', 'SUN/USDT', 'DYM/USDT',
    'BNX/USDT', 'XAI/USDT', 'CRV/USDT', 'MEME/USDT', 'AR/USDT', 'SUPER/USDT',
    'TRB/USDT', 'FIDA/USDT', 'STRK/USDT', 'JUP/USDT', 'LISTA/USDT', 'CKB/USDT',
    'JTO/USDT', 'MKR/USDT', 'LDO/USDT', 'ATOM/USDT', 'JASMY/USDT', 'ZK/USDT',
    'ENS/USDT', 'ORBS/USDT', 'APE/USDT', 'POL/USDT', 'BLUR/USDT', 'VIDT/USDT',
    'ICP/USDT', 'ZETA/USDT', 'GRT/USDT', 'AI/USDT', 'BB/USDT', 'ETHW/USDT',
    'SUSHI/USDT', 'STORJ/USDT', 'EOS/USDT', 'VANRY/USDT', 'KAVA/USDT',
    'RARE/USDT', 'OMNI/USDT', 'SYN/USDT', 'NEO/USDT', 'KAS/USDT', 'IMX/USDT',
    'AXS/USDT', 'GMT/USDT', 'THETA/USDT', 'SAND/USDT', '1000LUNC/USDT',
    'PIXEL/USDT', 'ROSE/USDT', 'DAR/USDT', 'UMA/USDT', 'AEVO/USDT', 'MANTA/USDT',
    'XLM/USDT', 'YGG/USDT', 'MINA/USDT', 'UNFI/USDT', 'LPT/USDT', 'BEAMX/USDT',
    'NFP/USDT', 'USTC/USDT', 'BAKE/USDT', 'BRETT/USDT', 'HBAR/USDT', 'PORTAL/USDT',
    'LQTY/USDT', 'POWR/USDT', 'PYTH/USDT', 'KDA/USDT', 'COTI/USDT', 'BSW/USDT',
    'MASK/USDT', 'CYBER/USDT', 'WOO/USDT', 'TNSR/USDT', 'POLYX/USDT', 'XMR/USDT',
    'ACH/USDT', 'GLM/USDT', 'ONG/USDT', 'SSV/USDT', 'ALPACA/USDT', 'FIO/USDT',
    'MAVIA/USDT', 'RDNT/USDT', 'TRU/USDT', 'KEY/USDT', 'HOOK/USDT', 'EGLD/USDT',
    'TWT/USDT', 'MANA/USDT', 'TOKEN/USDT', 'VET/USDT', 'ALGO/USDT', 'LUNA2/USDT',
    'DUSK/USDT', 'ACE/USDT', '1000XEC/USDT', 'AGLD/USDT', 'WAXP/USDT', 'RSR/USDT',
    'SNX/USDT', '1INCH/USDT', 'FLOW/USDT', 'HIGH/USDT', 'EDU/USDT', 'ONE/USDT',
    'JOE/USDT', 'CAKE/USDT', 'LOOM/USDT', 'IOTX/USDT', 'GTC/USDT', 'METIS/USDT',
    'ONT/USDT', 'COMP/USDT', 'ZIL/USDT', 'ZEN/USDT', 'CHR/USDT', 'MBOX/USDT',
    'API3/USDT', 'G/USDT', 'AMB/USDT', 'ASTR/USDT', 'VOXEL/USDT', 'AUCTION/USDT',
    'ALICE/USDT', 'ID/USDT', 'BOND/USDT', 'RONIN/USDT', 'XTZ/USDT', 'MAV/USDT',
    'QNT/USDT', 'RVN/USDT', 'ILV/USDT', 'NMR/USDT', 'SYS/USDT', 'IOTA/USDT',
    'QTUM/USDT', 'GMX/USDT', 'REN/USDT', 'STMX/USDT', 'MTL/USDT', 'FXS/USDT',
    'BICO/USDT', 'LRC/USDT', 'BEL/USDT', 'COS/USDT', 'LINA/USDT', 'AERGO/USDT',
    'BAND/USDT', 'ENJ/USDT', 'BLZ/USDT', 'DODO/USDT', 'CELR/USDT', 'LEVER/USDT',
    'SKL/USDT', 'OMG/USDT', 'REI/USDT', 'NULS/USDT', 'MAGIC/USDT', 'YFI/USDT',
    'HOT/USDT', 'MOVR/USDT', 'QUICK/USDT', 'T/USDT', 'ZRX/USDT', 'FLM/USDT',
    'RIF/USDT', 'KSM/USDT', 'DASH/USDT', 'TLM/USDT', 'LOKA/USDT', 'XVG/USDT',
    'C98/USDT', 'NTRN/USDT', 'IOST/USDT', 'BSV/USDT', 'ATA/USDT', 'ALPHA/USDT',
    'RPL/USDT', 'GHST/USDT', 'SPELL/USDT', 'FLUX/USDT', 'KLAY/USDT', 'ANKR/USDT',
    'RLC/USDT', 'BAL/USDT', 'BAT/USDT', 'CTSI/USDT', 'OGN/USDT', 'STG/USDT',
    'KNC/USDT', 'STEEM/USDT', 'PERP/USDT', 'CHESS/USDT', 'LIT/USDT', 'BADGER/USDT',
    'ICX/USDT', 'SFP/USDT', 'XVS/USDT', 'NKN/USDT', 'ARPA/USDT', 'DENT/USDT',
    'XEM/USDT', 'BTCDOM/USDT', 'COMBO/USDT', 'OXT/USDT', 'HFT/USDT', 'BNT/USDT',
    'LSK/USDT', 'DEFI/USDT',
]

# Token للبوت
TELEGRAM_BOT_TOKEN = '7881688707:AAEHc_15-NzaGuGtwT51ZvmFOt5PKhQ0dwI'
# معرف القناة أو المجموعة
TELEGRAM_CHAT_ID = '7039034340'

# فترة البحث للحصول على البيانات
timeframe = '1m'  # الإطار الزمني 1 دقيقة
lookback_period = 100  # فترة النظر لحساب أعلى قمة وأدنى قاع

# دالة لتحميل البيانات من منصة بينانس
def get_ohlcv(symbol, timeframe='1m', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# دالة لتحديد إشارة الشراء أو البيع
def check_buy_sell_signals(df):
    signals = []
    # حساب أعلى قمة وأدنى قاع في الفترة المحددة باستخدام Rolling
    df['highest_high'] = df['high'].rolling(window=lookback_period).max()
    df['lowest_low'] = df['low'].rolling(window=lookback_period).min()

    # التحقق من إشارات الشراء والبيع بناءً على الشروط
    for i in range(lookback_period, len(df)):
        current_high = df.iloc[i]['high']
        current_low = df.iloc[i]['low']
        highest_high = df.iloc[i]['highest_high']
        lowest_low = df.iloc[i]['lowest_low']

        # تحقق من إشارة شراء (BUY)
        if current_low <= highest_high and current_high >= highest_high:
            signals.append("BUY")

        # تحقق من إشارة بيع (SELL)
        elif current_high >= lowest_low and current_low <= lowest_low:
            signals.append("SELL")

        # في حالة عدم وجود إشارة
        else:
            signals.append("NO SIGNAL")

    return signals

# دالة لإرسال التنبيه عبر تلجرام
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.get(url, params=params)

# الدالة الرئيسية لتحديث البيانات والتحقق من الإشارات
def main():
    previous_signals = {symbol: None for symbol in symbols}  # إشارة سابقة لكل رمز
    while True:
        for symbol in symbols:
            # تحميل البيانات (أحدث 100 شمعة)
            df = get_ohlcv(symbol, timeframe='1m', limit=100)

            # التأكد من أن البيانات تحتوي على ما يكفي من الشموع
            if len(df) < lookback_period:
                print(f"البيانات غير كافية للعملة {symbol}")
                continue  # تخطي هذه الدورة والانتقال للعملة التالية

            # حساب الإشارات بناءً على البيانات
            signals = check_buy_sell_signals(df)

            # التحقق من أن قائمة الإشارات ليست فارغة
            if signals:
                current_signal = signals[-1]
                if previous_signals[symbol] != current_signal and current_signal != "NO SIGNAL":
                    message = f"إشارة {current_signal} للعملة {symbol}!"
                    send_telegram_message(message)
                    print(message)
                    previous_signals[symbol] = current_signal
            else:
                print(f"لا توجد إشارات للعملة {symbol} في هذه اللحظة.")

        # الانتظار لمدة دقيقة قبل التحقق مرة أخرى
        time.sleep(60)

# تشغيل البرنامج
if __name__ == '__main__':
    main()
