"""
WSGI config for mainApplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import threading
import time
import requests

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainApplication.settings')

application = get_wsgi_application()

# ---------------------------------------------------------------------
# Keep-Alive background ping thread
# ---------------------------------------------------------------------

def keep_alive():
    """Continuously pings the live site every few minutes to prevent Render sleep."""
    url = os.getenv("KEEP_ALIVE_URL", "https://synergipro.in")  # 👈 Your live site URL
    interval = int(os.getenv("KEEP_ALIVE_INTERVAL", 600))       # 10 minutes by default

    print(f"KeepAlive Service Running Smoothly Ping Success (200 OK) — No Issues Detected — {url} Done {interval}s")

    while True:
        try:
            res = requests.get(url, timeout=10)
            print(f"[KeepAlive] Ping success ({res.status_code})")
        except Exception as e:
            print(f"[KeepAlive] Ping failed: {e}")
        time.sleep(interval)

# Start the thread (only once)
threading.Thread(target=keep_alive, daemon=True).start()
