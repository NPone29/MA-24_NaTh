# Title : Script qui gère les chemins de ressources pour l'executable en .exe
# author : pj43svh & NPone29
# Date : 08.01.2026
# Version : 1.2.1


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