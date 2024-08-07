import requests

SABER_POOLS_API="https://raw.githubusercontent.com/saber-hq/saber-registry-dist/c417e1930d76273d2eaf07716be06c3f8edf7fb0/data/swaps.mainnet.json"
SABER_POOLS_DATA = requests.get(SABER_POOLS_API).json()