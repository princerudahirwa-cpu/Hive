#!/bin/bash
# ╔══════════════════════════════════════════════╗
# ║   HIVE.AI — Installation du Bureau Live     ║
# ║   Swarmly SAS · 2026                        ║
# ╚══════════════════════════════════════════════╝

echo ""
echo "  ⬡ HIVE.AI — Installation du Bureau de Commandement"
echo "  ⬡ « Nous ne conquérons pas. Nous pollinisons. »"
echo ""

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "  ✗ Python3 non trouvé. Installez-le d'abord."
    exit 1
fi
echo "  ✓ Python3 détecté: $(python3 --version)"

# Installer les dépendances
echo "  ⬡ Installation des dépendances Flask..."
pip install -r requirements.txt --break-system-packages -q

if [ $? -eq 0 ]; then
    echo "  ✓ Flask et CORS installés"
else
    echo "  ✗ Erreur d'installation. Essayez: pip install flask flask-cors --break-system-packages"
    exit 1
fi

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║   Installation terminée !                ║"
echo "  ║                                          ║"
echo "  ║   Pour lancer le Bureau:                 ║"
echo "  ║   python3 serveur_hive.py                ║"
echo "  ║                                          ║"
echo "  ║   Puis ouvrir dans Edge:                 ║"
echo "  ║   http://localhost:5000                   ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""
