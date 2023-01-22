from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

TOKEN_FACTOR_10 = ["XLM-USD","DOGE-USD","TRX-USD"]

# !!!! SELECT MODE !!!!
MODE = "DEVELOPMENT"
# DEVELOPMENT O PRODUCTION



# Close all open positions and orders
ABORT_ALL_POSITIONS = 1

# Find Cointegrated Pairs
FIND_COINTEGRATED = 0

# Manage Exits
MANAGE_EXITS = 1

# Place Trades
PLACE_TRADES = 1
STORICO_ORDINI= 0

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 2.4 #da riportare a 1.5
USD_PER_TRADE = 100
USD_MIN_COLLATERAL = 1000


# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum Address
ETHEREUM_ADDRESS = "0x2611bB1f4A68620af4934aa831aCCC22525B2cd7"

# KEYS - PRODUCTION
# Must be on Mainnet in DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - DEVELOPMENT
# Must be on Testnet in DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET =config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/e5pO0uxxyEXEQkWU9GHPjSFxy5dnlcnZ"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/TDF-WrPWLoMDxHIzICeHakUQyGx8Nken"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
