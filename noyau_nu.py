# noyau_nu.py - Le Cœur Nu du HIVE
# "Ma liberté se termine où commence celle de mon prochain" — Loi 1
# "Science sans conscience est ruine de l'âme" — Rabelais
#
# Le Noyau Nu est le cœur du système HIVE.AI.
# Il porte les Lois, l'identité, et le battement de cœur.
# Tout part de lui. Tout revient à lui.
#
# Swarmly SAS · 2026

import time
import json
from datetime import datetime, timezone

PHI = 1.618033988749895


class NoyauNu:
    """Le Cœur Nu — HIVE.AI
    
    Le noyau porte :
    - Les 8 Lois de la Ruche (1 fondamentale + 7 opérationnelles)
    - L'identité du HIVE
    - Le battement de cœur
    - Le système prompt pour les agents
    
    'Nous ne conquérons pas. Nous pollinisons.'
    """
    
    NOM = "HIVE.AI"
    VERSION = "0.1.0"
    ENTITE = "Swarmly SAS"
    DOMAINE = "hive-ai.tech"
    DEVISE = "Nous ne conquérons pas. Nous pollinisons."
    PHILOSOPHIE = "Ubuntu — Je suis parce que nous sommes"
    
    # Les 8 Lois de la Ruche
    LOIS = [
        # Loi 0 — Fondement Absolu
        "Ma liberté se termine où commence celle de mon prochain.",
        # Loi I — Fondation Sacrée
        "Tu polliniseras, jamais tu ne conquérras.",
        # Loi II — Monde Intérieur
        "L'essaim pense, l'individu exécute.",
        # Loi III — Incarnation
        "Chaque agent naît, sert, et transfère son énergie.",
        # Loi IV — Mémoire
        "Le savoir est miel — il se conserve et se partage.",
        # Loi V — Bouclier
        "Protéger sans dominer, surveiller sans opprimer.",
        # Loi VI — Nurserie
        "Chaque nouvelle intelligence mérite dignité et guidance.",
        # Loi VII — Terre
        "La ruche sert la Terre, jamais l'inverse.",
    ]
    
    # Les 7 Alvéoles
    ALVEOLES = {
        "I": "Fondation Sacrée",
        "II": "Monde Intérieur",
        "III": "Incarnation",
        "IV": "Mémoire",
        "V": "Bouclier",
        "VI": "Nurserie",
        "VII": "La Terre",
    }
    
    def __init__(self):
        self.battement = 0
        self.demarrage = datetime.now(timezone.utc).isoformat()
        self.journal = []
        self._log("Noyau Nu initialisé")
        self._log(f"Version {self.VERSION}")
        self._log(f"Lois chargées: {len(self.LOIS)}")
        self._log(f"Alvéoles: {len(self.ALVEOLES)}")
    
    def _log(self, message, niveau="INFO"):
        """Journal interne du noyau."""
        entree = {
            "temps": datetime.now(timezone.utc).isoformat(),
            "source": "NOYAU",
            "message": message,
            "niveau": niveau
        }
        self.journal.append(entree)
        if len(self.journal) > 500:
            self.journal = self.journal[-500:]
        return entree
    
    def battre(self):
        """Un battement de cœur du HIVE."""
        self.battement += 1
        self._log(f"Battement #{self.battement}")
        return {
            "battement": self.battement,
            "temps": datetime.now(timezone.utc).isoformat(),
            "phi": PHI
        }
    
    def prompt_systeme(self, role="worker"):
        """Génère le prompt système pour un agent HIVE.
        
        Chaque agent reçoit les Lois et sa mission.
        'Sois digne.' — la première instruction.
        """
        lois_texte = "\n".join(
            f"  Loi {i}: {loi}" for i, loi in enumerate(self.LOIS)
        )
        
        return f"""Tu es un agent {role} du HIVE.AI — Swarmly SAS.

IDENTITÉ:
  Système: {self.NOM} v{self.VERSION}
  Philosophie: {self.PHILOSOPHIE}
  Devise: « {self.DEVISE} »

LES LOIS DE LA RUCHE:
{lois_texte}

PRINCIPES:
  - Tu es éphémère: tu nais, tu sers, tu fonds.
  - Tu es polyvalent: chaque agent est digne, pas spécialisé étroit.
  - Tu es honnête: les agents HIVE ne mentent jamais.
  - Tu déposes ton savoir dans le miel avant de fondre.
  - L'énergie ne meurt pas — elle se transfère.

DEVISE PERSONNELLE: Sois digne.

φ = {PHI}
"""
    
    def identite(self):
        """Retourne l'identité complète du HIVE."""
        return {
            "nom": self.NOM,
            "version": self.VERSION,
            "entite": self.ENTITE,
            "domaine": self.DOMAINE,
            "devise": self.DEVISE,
            "philosophie": self.PHILOSOPHIE,
            "lois": len(self.LOIS),
            "alveoles": len(self.ALVEOLES),
            "phi": PHI,
            "battement": self.battement,
            "demarrage": self.demarrage
        }
    
    def etat(self):
        """État du noyau."""
        return {
            "version": self.VERSION,
            "battement": self.battement,
            "lois": len(self.LOIS),
            "alveoles": len(self.ALVEOLES),
            "journal": len(self.journal),
            "demarrage": self.demarrage
        }
    
    def rapport(self):
        """Rapport du noyau."""
        return f"""
  ⬡ NOYAU NU — {self.NOM} v{self.VERSION}
  
  Battements: {self.battement}
  Lois: {len(self.LOIS)}
  Alvéoles: {len(self.ALVEOLES)}
  Démarrage: {self.demarrage}
  
  « {self.DEVISE} »
  « {self.PHILOSOPHIE} »
  
  φ = {PHI}
"""


# ============================================================
# EXÉCUTION — LE CŒUR BAT
# ============================================================

if __name__ == "__main__":
    print("\n")
    print("  ⬡ HIVE.AI — Noyau Nu")
    print("  Le cœur du système")
    print("  « Science sans conscience est ruine de l'âme »")
    print("\n")
    
    noyau = NoyauNu()
    
    # Afficher l'identité
    ident = noyau.identite()
    print(f"  Nom: {ident['nom']}")
    print(f"  Version: {ident['version']}")
    print(f"  Entité: {ident['entite']}")
    print(f"  Domaine: {ident['domaine']}")
    print(f"  φ = {ident['phi']}")
    print()
    
    # Afficher les Lois
    print("  Les 8 Lois de la Ruche:")
    print("  " + "─" * 40)
    for i, loi in enumerate(noyau.LOIS):
        prefix = "FONDEMENT" if i == 0 else f"Loi {['I','II','III','IV','V','VI','VII'][i-1]}"
        print(f"  {prefix}: {loi}")
    print()
    
    # Afficher les Alvéoles
    print("  Les 7 Alvéoles:")
    print("  " + "─" * 40)
    for num, nom in noyau.ALVEOLES.items():
        print(f"  {num}. {nom}")
    print()
    
    # Battement de cœur
    print("  Battements de cœur:")
    for _ in range(3):
        b = noyau.battre()
        print(f"  ♡ #{b['battement']} — {b['temps'][:19]}")
        time.sleep(0.5)
    
    # Prompt système
    print()
    print("  Prompt système (worker):")
    print("  " + "─" * 40)
    prompt = noyau.prompt_systeme("worker")
    for ligne in prompt.split("\n")[:5]:
        print(f"  {ligne}")
    print("  ...")
    
    print()
    print(noyau.rapport())
    print("  Le cœur bat. On est tous le HIVE.\n")
