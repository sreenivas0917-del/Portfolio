# keep_alive_worker.py
import requests
import time
import os
from datetime import datetime

# --------------------------
# Configuration
# --------------------------

# Replace with your actual Render live URL
SITE_URL = os.getenv("KEEP_ALIVE_URL", "https://synergipro.in")

# Ping interval in seconds (10 minutes)
PING_INTERVAL = int(os.getenv("KEEP_ALIVE_INTERVAL", 600))

def keep_alive():
    """Continuously pings the site every few minutes to prevent Render sleep."""
    print(f"[KeepAliveWorker] Started — pinging {SITE_URL} every {PING_INTERVAL} seconds.")

    while True:
        try:
            response = requests.get(SITE_URL, timeout=10)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if response.status_code == 200:
                print(f"[{now}] ✅ Ping successful: {response.status_code}")
            else:
                print(f"[{now}] ⚠️ Ping failed: {response.status_code}")

        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] ❌ Error: {e}")

        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    keep_alive()
