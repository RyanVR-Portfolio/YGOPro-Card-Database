# playwright.config.py

from playwright.sync_api import Playwright, sync_playwright
from playwright import Page

def config():
    return {
        "use": {
            "base_url": 'https://ygoprodeck.com/card-database/',
            "trace": 'on-first-retry',
            # Add other settings here if needed
        },
        "projects": [
            {
                "name": "chromium",
                "use": {
                    "channel": "chrome",  # or "msedge" for Edge
                    "viewport": {"width": 1280, "height": 720},
                    # Add more settings if needed
                },
            },
            {
                "name": "firefox",
                "use": {
                    "channel": "firefox",
                    "viewport": {"width": 1280, "height": 720},
                    # Add more settings if needed
                },
            },
            {
                "name": "webkit",
                "use": {
                    "channel": "webkit",
                    "viewport": {"width": 1280, "height": 720},
                    # Add more settings if needed
                },
            },
        ],
    }