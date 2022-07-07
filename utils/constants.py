from pathlib import Path
import sys

class SolanaEndpoints():
    
    MAINNET_RPC = "https://api.mainnet-beta.solana.com"
 
    
class Bot():
    
    VERSION = "0.17.0.0"
    

class Keys():
    
    TLS_KEY = "oLZxFnte8n5UL6ERJqBjH7tJk37jVh503RP5IIt0"
    CF_API_KEY = "9c72148a-4e93-46b9-b5d0-d125e6c12f92"
    OS_API_KEY = "8216f4bf-659c-4b22-be8b-690285f86762"
    

class Paths():
    
    BIFROST_PATH  = str(Path("bin/bifrost.dll").resolve())
    TLS_PATH = str(Path("bin/TLS").resolve()) if sys.platform == "darwin" else str(Path("bin/TLS.exe").resolve())

class SolanaPrograms():
    
    CMV2_PROGRAM = "cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ"
    ME_PROGRAM = "CMZYPASGWeTz7RNGHaRJfCq2XQ5pYK6nDvVQxzkH51zb"
    LMN_PROGRAM = "ArAA6CZC123yMJLUe4uisBEgvfuw2WEvex9iFmFCYiXv"
    ML_PROGRAM = "minwAEdewYNqagUwzrVBUGWuo277eeSMwEwj76agxYd"
    

class EthereumContracts():
    
    OS_CONTRACT = "0x7f268357A8c2552623316e2562D90e642bB538E5"