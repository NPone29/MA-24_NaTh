import os
import sys

def resource_path(rel_path):
    """
    Retourne le chemin absolu utilisable à l'exécution.
    Fonctionne normalement et dans les bundles PyInstaller (--onefile) via sys._MEIPASS.
    """
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base, rel_path)