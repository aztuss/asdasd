"""
config.py — Central configuration for the trading bot.
All indicator settings, instrument definitions, API credentials,
trade management parameters, and filter rules live here.
"""

# =============================================================================
#  CAPITAL.COM API CREDENTIALS
# =============================================================================
API_KEY = "wFD6JmaUYnYJNhUg"
API_IDENTIFIER = "feridsalamanov@gmail.com"         # Capital.com login email
API_PASSWORD = '314p15iAZe"""'                      # Capital.com login password

# Environment: "demo" or "live"
# Change to "live" when ready for real trading
ENVIRONMENT = "demo"

# Base URLs
BASE_URLS = {
    "demo": "https://demo-api-capital.backend-capital.com",
    "live": "https://api-capital.backend-capital.com",
}

# =============================================================================
#  GENERAL SETTINGS & RISK MANAGEMENT
# =============================================================================
STARTING_CAPITAL = 290.0       # USD

# Dynamic Risk Sizing
FULL_LOT_SIZE = 15.0            # USD margin
SCORE_REDUCED_LOT_SIZE = 10.0   # 5/6 score
DRAWDOWN_REDUCED_LOT = 8.0      # When drawdown limit hit
LEVERAGE = 30                   # x30
BACKTEST_LEVERAGE = 30          # x30

# Account Protection
DAILY_LOSS_LIMIT_PCT = -0.05    # Stop trading for the day
WEEKLY_LOSS_LIMIT_PCT = -0.07   # Stop trading for the week
DRAWDOWN_PROTECTION_PCT = -0.15 # If drawn down > 15%, lot size drops
HARD_STOP_CAPITAL = 232.0       # -20% stop all trading immediately
MAX_LOSS_PER_TRADE = 15.0       # Max $15 loss per trade (~5% of $290)
MAX_OPEN_TRADES = 3             # Overall maximum
MAX_OPEN_TRADES_PER_CLASS = 2   # Max per market class
CONSECUTIVE_LOSS_PAUSE_HOURS = 4 # Pause trading after 3 consecutive losses
HIGH_VOL_MAX_LOT = 10.0         # Max lot for high vol instruments
HIGH_VOL_INSTRUMENTS = ["SOLUSD", "XRPUSD", "XAGUSD", "DOGEUSD"]


# Scoring thresholds
SCORE_FULL_LOT = 6              # 6/6 → full lot
SCORE_REDUCED_LOT = 5           # 5/6 → reduced lot
SCORE_MIN_TO_TRADE = 5          # Minimum score to open a trade (4 or below = skip)

# =============================================================================
#  INSTRUMENTS — 48 total
#  Format: { symbol: { "epic": Capital.com epic, "class": market_class } }
# =============================================================================
INSTRUMENTS = {
    # ----- Forex (14) -----
    "EURUSD":  {"epic": "EURUSD",  "class": "forex", "active": True},
    "GBPUSD":  {"epic": "GBPUSD",  "class": "forex", "active": False},
    "USDJPY":  {"epic": "USDJPY",  "class": "forex", "active": False},
    "USDCHF":  {"epic": "USDCHF",  "class": "forex", "active": True},
    "AUDUSD":  {"epic": "AUDUSD",  "class": "forex", "active": False},
    "USDCAD":  {"epic": "USDCAD",  "class": "forex", "active": False},
    "NZDUSD":  {"epic": "NZDUSD",  "class": "forex", "active": False},
    "EURGBP":  {"epic": "EURGBP",  "class": "forex", "active": False},
    "EURJPY":  {"epic": "EURJPY",  "class": "forex", "active": False},
    "GBPJPY":  {"epic": "GBPJPY",  "class": "forex", "active": True},
    "CADJPY":  {"epic": "CADJPY",  "class": "forex", "active": True},
    "AUDCAD":  {"epic": "AUDCAD",  "class": "forex", "active": True},
    "AUDNZD":  {"epic": "AUDNZD",  "class": "forex", "active": True},
    "GBPAUD":  {"epic": "GBPAUD",  "class": "forex", "active": True},

    # ----- Crypto (14) -----
    "BTCUSD":  {"epic": "BTCUSD",  "class": "crypto", "active": True},
    "ETHUSD":  {"epic": "ETHUSD",  "class": "crypto", "active": False},
    "SOLUSD":  {"epic": "SOLUSD",  "class": "crypto", "active": True},
    "XRPUSD":  {"epic": "XRPUSD",  "class": "crypto", "active": True},
    "BNBUSD":  {"epic": "BNBUSD",  "class": "crypto", "active": False},
    "ADAUSD":  {"epic": "ADAUSD",  "class": "crypto", "active": False},
    "DOGEUSD": {"epic": "DOGEUSD", "class": "crypto", "active": True},
    "AVAXUSD": {"epic": "AVAXUSD", "class": "crypto", "active": False},
    "LINKUSD": {"epic": "LINKUSD", "class": "crypto", "active": False},
    "MATICUSD":{"epic": "MATICUSD","class": "crypto", "active": False},
    "DOTUSD":  {"epic": "DOTUSD",  "class": "crypto", "active": False},
    "UNIUSD":  {"epic": "UNIUSD",  "class": "crypto", "active": False},
    "LTCUSD":  {"epic": "LTCUSD",  "class": "crypto", "active": False},
    "ATOMUSD": {"epic": "ATOMUSD", "class": "crypto", "active": False},

    # ----- Indices (9) -----
    "US100":   {"epic": "US100",   "class": "indices", "active": True},
    "US500":   {"epic": "US500",   "class": "indices", "active": True},
    "US30":    {"epic": "US30",    "class": "indices", "active": True},
    "DE40":    {"epic": "DE40",    "class": "indices", "active": False},
    "UK100":   {"epic": "UK100",   "class": "indices", "active": True},
    "JP225":   {"epic": "JP225",   "class": "indices", "active": False},
    "AU200":   {"epic": "AU200",   "class": "indices", "active": True},
    "HK50":    {"epic": "HK50",    "class": "indices", "active": False},
    "FR40":    {"epic": "FR40",    "class": "indices", "active": True},

    # ----- Commodities (6) -----
    "XAUUSD":  {"epic": "GOLD",      "class": "commodities", "active": False},
    "XAGUSD":  {"epic": "SILVER",    "class": "commodities", "active": True},
    "WTI":     {"epic": "OIL_CRUDE", "class": "commodities", "active": True},
    "BRENT":   {"epic": "OIL_BRENT", "class": "commodities", "active": False},
    "NATGAS":  {"epic": "NAT_GAS",   "class": "commodities", "active": False},
    "COPPER":  {"epic": "COPPER",    "class": "commodities", "active": True},

    # ----- Stocks (5) -----
    "AAPL":    {"epic": "AAPL",    "class": "stocks", "active": False},
    "MSFT":    {"epic": "MSFT",    "class": "stocks", "active": False},
    "NVDA":    {"epic": "NVDA",    "class": "stocks", "active": True},
    "TSLA":    {"epic": "TSLA",    "class": "stocks", "active": True},
    "AMZN":    {"epic": "AMZN",    "class": "stocks", "active": True},
}

# =============================================================================
#  INDICATOR PARAMETERS — per market class
# =============================================================================
INDICATOR_PARAMS = {
    "forex": {
        "trend_ma_type": "EMA",
        "trend_ma_period": 200,
        "adx_period": 14,
        "adx_threshold": 25,
        "rsi_period": 14,
        "rsi_long_zone": (45, 65),
        "rsi_short_zone": (35, 55),
        "atr_period": 14,
        "macd_fast": 12,
        "macd_slow": 26,
        "macd_signal": 9,
        "supertrend_period": 10,
        "supertrend_multiplier": 3.0,
        # Indicators used for scoring (ordered)
        "scoring_indicators": [
            "trend_ma", "adx", "rsi", "macd", "supertrend", "atr_trend"
        ],
    },
    "crypto": {
        "trend_ma_type": "EMA",
        "trend_ma_period": 200,
        "adx_period": 14,
        "adx_threshold": 22,
        "rsi_period": 14,
        "rsi_long_zone": (40, 65),
        "rsi_short_zone": (35, 60),
        "atr_period": 14,
        "supertrend_period": 10,
        "supertrend_multiplier": 2.5,
        "scoring_indicators": [
            "trend_ma", "adx", "rsi", "obv", "supertrend", "atr_trend"
        ],
    },
    "indices": {
        "trend_ma_type": "SMA",
        "trend_ma_period": 200,
        "adx_period": 14,
        "adx_threshold": 22,
        "rsi_period": 10,
        "rsi_long_zone": (52, 65),
        "rsi_short_zone": (35, 48),
        "atr_period": 10,
        "supertrend_period": 7,
        "supertrend_multiplier": 3.0,
        "scoring_indicators": [
            "trend_ma", "adx", "rsi", "vwap", "supertrend", "atr_trend"
        ],
    },
    "commodities": {
        "trend_ma_type": "EMA",
        "trend_ma_period": 200,
        "adx_period": 14,
        "adx_threshold": 25,
        "rsi_period": 14,
        "rsi_long_zone": (40, 65),
        "rsi_short_zone": (35, 60),
        "atr_period": 14,
        "supertrend_period": 10,
        "supertrend_multiplier": 3.0,
        "bb_period": 20,
        "bb_std": 2.0,
        "scoring_indicators": [
            "trend_ma", "adx", "rsi", "bollinger", "supertrend", "atr_trend"
        ],
    },
    "stocks": {
        "trend_ma_type": "SMA",
        "trend_ma_period": 200,
        "adx_period": 14,
        "adx_threshold": 25,
        "rsi_period": 14,
        "rsi_long_zone": (45, 65),
        "rsi_short_zone": (35, 55),
        "atr_period": 14,
        "macd_fast": 12,
        "macd_slow": 26,
        "macd_signal": 9,
        "scoring_indicators": [
            "trend_ma", "adx", "rsi", "macd", "vwap", "atr_trend"
        ],
    },
}

# =============================================================================
#  MINIMUM ATR FILTER
#  Minimum absolute ATR required to open a trade per class or symbol
# =============================================================================
MIN_ATR_FILTER = {
    "BTCUSD": 50.0,
    "ETHUSD": 2.0,
    "XAUUSD": 0.5,
    "XAGUSD": 0.3,
    "WTI": 0.5,
    "BRENT": 0.5,
    "NATGAS": 0.05,
    "COPPER": 0.02,
    "DOGEUSD": 0.0005,
    "XRPUSD": 0.005,
    "MATICUSD": 0.005,
    "forex": 0.0005,
    "crypto": 0.5,     # Default for other cryptos
    "indices": 10.0,
    "commodities": 0.5,
    "stocks": 0.5,
}

# =============================================================================
#  TRADE MANAGEMENT
# =============================================================================
SL_ATR_MULTIPLIER = 0.8         # Stop-Loss = 0.8 × ATR
TP1_ATR_MULTIPLIER = 1.2        # TP1 = 1.2 × ATR
TP2_ATR_MULTIPLIER = 2.5        # TP2 = 2.5 × ATR
TRAILING_SL_ATR_MULTIPLIER = 0.6 # Trailing stop distance after TP1
TP1_CLOSE_PCT = 0.40            # Close 40% of position at TP1
TP2_CLOSE_PCT = 0.60            # Close remaining 60% at TP2

# =============================================================================
#  CORRELATION MAP
#  If instrument X is open, block all instruments in its correlated list.
# =============================================================================
CORRELATION_MAP = {
    "EURUSD":  ["GBPUSD", "AUDUSD", "NZDUSD", "EURJPY"],
    "GBPUSD":  ["EURUSD", "EURGBP", "GBPJPY"],
    "USDJPY":  ["USDCHF", "USDCAD", "EURJPY", "GBPJPY", "CADJPY"],
    "USDCHF":  ["USDJPY", "USDCAD"],
    "USDCAD":  ["USDJPY", "USDCHF"],
    "AUDUSD":  ["EURUSD", "NZDUSD", "AUDCAD", "AUDNZD"],
    "NZDUSD":  ["EURUSD", "AUDUSD", "AUDNZD"],
    "EURGBP":  ["GBPUSD"],
    "EURJPY":  ["USDJPY", "EURUSD"],
    "GBPJPY":  ["USDJPY", "GBPUSD"],
    "CADJPY":  ["USDJPY", "USDCAD"],
    "AUDCAD":  ["AUDUSD", "USDCAD"],
    "AUDNZD":  ["AUDUSD", "NZDUSD"],
    "GBPAUD":  ["GBPUSD", "AUDUSD"],

    "BTCUSD":  ["ETHUSD", "SOLUSD", "BNBUSD", "LINKUSD", "DOTUSD", "LTCUSD"],
    "ETHUSD":  ["BTCUSD", "SOLUSD", "BNBUSD", "LINKUSD"],
    "SOLUSD":  ["BTCUSD", "ETHUSD"],
    "BNBUSD":  ["BTCUSD", "ETHUSD"],
    "XRPUSD":  ["ADAUSD", "DOGEUSD"],
    "ADAUSD":  ["XRPUSD", "DOGEUSD"],
    "DOGEUSD": ["XRPUSD", "ADAUSD"],
    "AVAXUSD": [],
    "LINKUSD": ["BTCUSD", "ETHUSD"],
    "MATICUSD":[],
    "DOTUSD":  ["BTCUSD"],
    "UNIUSD":  [],
    "LTCUSD":  ["BTCUSD"],
    "ATOMUSD": [],

    "XAUUSD":  ["XAGUSD"],
    "XAGUSD":  ["XAUUSD"],
    "WTI":     ["BRENT"],
    "BRENT":   ["WTI"],
    "NATGAS":  [],
    "COPPER":  [],

    "US100":   ["US500", "US30"],
    "US500":   ["US100", "US30"],
    "US30":    ["US100", "US500"],
    "DE40":    ["FR40"],
    "UK100":   [],
    "JP225":   [],
    "AU200":   [],
    "HK50":    [],
    "FR40":    ["DE40"],

    "AAPL":    [],
    "MSFT":    [],
    "NVDA":    [],
    "TSLA":    [],
    "AMZN":    [],
}

# =============================================================================
#  SESSION FILTER
#  Defines which sessions each instrument is allowed to trade in.
#  Times are in UTC.
# =============================================================================
SESSIONS = {
    "london":   {"start": "08:00", "end": "16:00"},
    "new_york": {"start": "13:00", "end": "21:00"},
    "asia":     {"start": "00:00", "end": "08:00"},
    "crypto":   {"start": "00:00", "end": "23:59"},  # 24/7
}

# Map: instrument → list of allowed session names
INSTRUMENT_SESSIONS = {
    # Forex
    "EURUSD":  ["london", "new_york"],
    "GBPUSD":  ["london", "new_york"],
    "USDJPY":  ["london", "new_york", "asia"],
    "USDCHF":  ["london", "new_york"],
    "AUDUSD":  ["london", "new_york", "asia"],
    "USDCAD":  ["london", "new_york"],
    "NZDUSD":  ["london", "new_york", "asia"],
    "EURGBP":  ["london", "new_york"],
    "EURJPY":  ["london", "new_york", "asia"],
    "GBPJPY":  ["london", "new_york", "asia"],
    "CADJPY":  ["london", "new_york", "asia"],
    "AUDCAD":  ["london", "new_york", "asia"],
    "AUDNZD":  ["london", "new_york", "asia"],
    "GBPAUD":  ["london", "new_york", "asia"],

    # Crypto — 24/7
    "BTCUSD":  ["crypto"],
    "ETHUSD":  ["crypto"],
    "SOLUSD":  ["crypto"],
    "XRPUSD":  ["crypto"],
    "BNBUSD":  ["crypto"],
    "ADAUSD":  ["crypto"],
    "DOGEUSD": ["crypto"],
    "AVAXUSD": ["crypto"],
    "LINKUSD": ["crypto"],
    "MATICUSD":["crypto"],
    "DOTUSD":  ["crypto"],
    "UNIUSD":  ["crypto"],
    "LTCUSD":  ["crypto"],
    "ATOMUSD": ["crypto"],

    # Indices
    "US100":   ["london", "new_york"],
    "US500":   ["london", "new_york"],
    "US30":    ["london", "new_york"],
    "DE40":    ["london"],
    "UK100":   ["london"],
    "JP225":   ["asia", "london"],
    "AU200":   ["asia", "london"],
    "HK50":    ["asia"],
    "FR40":    ["london"],

    # Commodities
    "XAUUSD":  ["london", "new_york"],
    "XAGUSD":  ["london", "new_york"],
    "WTI":     ["new_york"],
    "BRENT":   ["london", "new_york"],
    "NATGAS":  ["new_york", "london"],
    "COPPER":  ["new_york", "london"],

    # Stocks — New York
    "AAPL":    ["new_york"],
    "MSFT":    ["new_york"],
    "NVDA":    ["new_york"],
    "TSLA":    ["new_york"],
    "AMZN":    ["new_york"],
}

# =============================================================================
#  NEWS FILTER — ForexFactory
# =============================================================================
NEWS_WINDOW_MINUTES = 30  # ±30 minutes around high-impact events

# Map currency codes to affected instruments
CURRENCY_INSTRUMENT_MAP = {
    "USD": ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD",
            "NZDUSD", "BTCUSD", "ETHUSD", "XAUUSD", "XAGUSD", "WTI",
            "BRENT", "NATGAS", "COPPER", "US100", "US500", "US30", 
            "AAPL", "MSFT", "NVDA", "TSLA", "AMZN",
            "SOLUSD", "XRPUSD", "DOGEUSD", "LINKUSD", "DOTUSD", "LTCUSD"],
    "EUR": ["EURUSD", "EURGBP", "EURJPY", "DE40", "FR40"],
    "GBP": ["GBPUSD", "EURGBP", "GBPJPY", "GBPAUD", "UK100"],
    "JPY": ["USDJPY", "EURJPY", "GBPJPY", "CADJPY", "JP225"],
    "CHF": ["USDCHF"],
    "AUD": ["AUDUSD", "AUDCAD", "AUDNZD", "GBPAUD", "AU200"],
    "CAD": ["USDCAD", "CADJPY", "AUDCAD"],
    "NZD": ["NZDUSD", "AUDNZD"],
    "HKD": ["HK50"],
}

# =============================================================================
#  LOAD OPTIMIZED PARAMETERS
# =============================================================================
import os
import json

OPTIMIZED_PARAMS_FILE = os.path.join(os.path.dirname(__file__), "config", "optimized_params.json")
OPTIMIZED_PARAMS = {}

if os.path.exists(OPTIMIZED_PARAMS_FILE):
    try:
        with open(OPTIMIZED_PARAMS_FILE, "r") as f:
            OPTIMIZED_PARAMS = json.load(f)
    except Exception as e:
        pass

def get_instrument_params(symbol):
    """
    Get the indicator parameters for an instrument.
    Returns optimized parameters if available, otherwise falls back to market class default.
    """
    if symbol in OPTIMIZED_PARAMS:
        return OPTIMIZED_PARAMS[symbol]
        
    market_class = INSTRUMENTS.get(symbol, {}).get("class", "forex")
    return INDICATOR_PARAMS.get(market_class, INDICATOR_PARAMS["forex"])

# =============================================================================
#  BACKTEST SETTINGS
# =============================================================================
BACKTEST_LOOKBACK_DAYS = 365    # 1 year of data
BACKTEST_INITIAL_CAPITAL = 290.0
BACKTEST_LOT_SIZE = 15.0
BACKTEST_LEVERAGE = 30

# =============================================================================
#  LOGGING
# =============================================================================
LOG_DIR = "logs"
TRADE_LOG_FILE = "logs/trades.csv"
SIGNAL_LOG_FILE = "logs/signals.csv"
BOT_LOG_FILE = "logs/bot.log"

# =============================================================================
#  API RETRY SETTINGS
# =============================================================================
API_MAX_RETRIES = 3
API_RETRY_DELAY = 2             # seconds (base for exponential backoff)
API_TIMEOUT = 30                # seconds
