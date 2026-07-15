from pathlib import Path
import json

PLUGIN_DIR=Path("plugins")

def list_plugins():
    plugins=[]
    if not PLUGIN_DIR.exists():
        return []
    for p in PLUGIN_DIR.glob("*.json"):
        try:
            plugins.append(json.loads(p.read_text()))
        except Exception:
            pass
    return plugins
