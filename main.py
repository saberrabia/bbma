import ccxt
import time
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder

# إعدادات
exchange = ccxt.binance()
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

# إعداد بوت تلجرام
TELEGRAM_TOKEN = '7881688707:AAEHc_15-NzaGuGtwT51ZvmFOt5PKhQ0dwI'  # استبدل بـ API Token الخاص بك 
CHAT_ID = '7039034340'  # ضع الـ chat ID هنا

# قائمة لتتبع آخر 20 عملة تم إرسال إشعار عنها
recently_notified = []

# دالة لجلب تغييرات الأسعار في آخر 24 ساعة
def fetch_24h_changes():
    changes = {}
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        changes[symbol] = ticker['percentage']  # نسبة التغيير في آخر 24 ساعة
    return changes

# دالة لتحديد العملات الصاعدة
def check_top_up(changes):
    valid_changes = {symbol: change for symbol, change in changes.items() if change is not None}
    sorted_changes = sorted(valid_changes.items(), key=lambda x: x[1])
    
    top_up = sorted_changes[-10:]  # أعلى 10 عملات صعودًا
    return top_up

# قائمة لتتبع العملات في القوائم
tracked_up = set()

# إعداد تطبيق تلجرام
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# دالة لإرسال الرسالة عبر تلجرام
async def send_message(symbol, change):
    global recently_notified
    if symbol not in recently_notified:
        await app.bot.send_message(chat_id=CHAT_ID, text=f"عملة حالياً في قائمة أعلى 10: {symbol} - تغيير: {change:.2f}%")
        
        # إضافة العملة إلى القائمة
        recently_notified.append(symbol)
        
        # الاحتفاظ بحدود 20 عملة فقط
        if len(recently_notified) > 20:
            recently_notified.pop(0)  # إزالة أقدم عملة إذا تجاوز العدد 20

# دالة للمراقبة
async def monitor():
    global tracked_up
    initial_changes = fetch_24h_changes()
    top_up = check_top_up(initial_changes)

    # إضافة العملات الأولى للقوائم
    for symbol, change in top_up:
        tracked_up.add(symbol)
        print(f"عملة حالياً في قائمة أعلى 10: {symbol} - تغيير: {change:.2f}%")
        await send_message(symbol, change)

    while True:
        changes = fetch_24h_changes()
        await asyncio.sleep(60)  # الانتظار دقيقة

        top_up = check_top_up(changes)

        # طباعة العملات الصاعدة
        for symbol, change in top_up:
            if symbol not in tracked_up:
                print(f"عملة دخلت قائمة أعلى 10: {symbol} - تغيير: {change:.2f}%")
                await send_message(symbol, change)
                tracked_up.add(symbol)

        # تحديث القوائم
        for symbol in list(tracked_up):
            if symbol not in dict(top_up):
                print(f"عملة خرجت من قائمة أعلى 10: {symbol}")
                tracked_up.remove(symbol)

# بدء العملية
if __name__ == '__main__':
    asyncio.run(monitor()) 
