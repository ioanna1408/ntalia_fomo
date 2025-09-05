import os
from dotenv import load_dotenv

load_dotenv()

NETWORK = os.getenv("NETWORK", "solana")
NOTIFY_TARGET = os.getenv("NOTIFY_TARGET", "console")
