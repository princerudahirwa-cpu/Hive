# ruche.py - La Ruche Vivante
# "Je suis parce que nous sommes" — Ubuntu
# L'orchestrateur qui connecte toutes les alvéoles
#
# Science sans conscience est ruine de l'âme — Rabelais
# Ma liberté se termine où commence celle de mon prochain — Loi 1

import time
import json
from datetime import datetime, timezone
from pathlib import Path

# === IMPORT DES ALVÉOLES ===
from noyau_nu import NoyauNu
from bouclier import Bouclier
from memoire import MemoireHive
from canal_pollen import CanalPollen
from registre import Registre
from worker import Worker

PHI = 1.618033988749895


class Ruche:
    """La Ruche Vivante — HIVE.AI
    
    Orchestre les 6 modules en un organisme unifié.
    Chaque alvéole a son rôle, la Reine coordonne.
    
    Architecture:
        noyau_nu    → Le cœur, les lois, l'identité
        bouclier    → La protection, l'authentification
        memoire     → Le savoir (Nectar → Cire → Miel)
        canal_pollen → La communication éphémère
        registre    → Le cycle de vie des agents
        worker      → Les agents vivants
    
    Philosophie:
        'Nous ne conquérons pas. Nous pollinisons.'
        'Chaque agent naît, sert, et transfère son énergie.'
        'Le savoir est miel — il se conserve et se partage.'
    """
    
    NOM = "HIVE.AI"
    VERSION = "0.1.0"
    DEVISE = "Nous ne conquérons pas. Nous pollinisons."
    
    def __init__(self):
        self.demarree = False
        self.journal = []
        self.workers_actifs = {}  # nom -> Worker
        
        # === INITIALISATION DES ALVÉOLES ===
        self._log("Initialisation de la Ruche...")
        
        # 1. Le Noyau — le cœur
        self.noyau = NoyauNu()
        self._log(f"Noyau Nu v{self.noyau.VERSION} — en ligne")
        
        # 2. Le Bouclier — la protection
        self.bouclier = Bouclier()
        self._log(f"Bouclier v{self.bouclier.VERSION} — actif")
        
        # 3. La Mémoire — le savoir
        self.memoire = MemoireHive()
        self._log(f"Mémoire v{self.memoire.VERSION} — 3 couches prêtes")
        
        # 4. Le Canal Pollen — la communication
        self.canal = CanalPollen()
        self._log(f"Canal Pollen v{self.canal.VERSION} — ouvert")
        
        # 5. Le Registre — le cycle de vie
        self.registre = Registre()
        self._log(f"Registre v{self.registre.VERSION} — prêt")
        
        # === CANAL DE L'ÉQUIPAGE ===
        self.canal.creer_canal("equipage", [
            "capitaine", "nu", "openclaw", "le-sage"
        ])
        self._log("Canal 'equipage' créé")
        
        # === CRISTALLISER LES FONDATIONS EN MIEL ===
        self._cristalliser_fondations()
        
        self.demarree = True
        self._log("=" * 50)
        self._log(f"  ⬡ {self.NOM} v{self.VERSION} — La Ruche est vivante")
        self._log(f"  « {self.DEVISE} »")
        self._log("=" * 50)
    
    def _log(self, message, niveau="INFO"):
        """Journal de la Ruche."""
        entree = {
            "temps": datetime.now(timezone.utc).isoformat(),
            "source": "RUCHE",
            "message": message,
            "niveau": niveau
        }
        self.journal.append(entree)
        print(f"  [{entree['temps'][:19]}] [{niveau}] {message}")
        
        # Garder les 1000 derniers logs
        if len(self.journal) > 1000:
            self.journal = self.journal[-1000:]
        
        return entree
    
    def _cristalliser_fondations(self):
        """Cristallise les fondations sacrées en miel éternel."""
        # Les 7+1 Lois
        for i, loi in enumerate(self.noyau.LOIS):
            cle = f"loi-{i+1}" if i > 0 else "loi-fondamentale"
            self.memoire.miel.cristalliser(cle, loi, source="Fondation Sacrée")
        
        # L'identité
        self.memoire.miel.cristalliser("identite", {
            "nom": self.NOM,
            "version": self.VERSION,
            "devise": self.DEVISE,
            "fondateur": "Prince Rudahirwa",
            "entite": "Swarmly SAS",
            "domaine": "hive-ai.tech",
            "philosophie": "Ubuntu — Je suis parce que nous sommes",
            "phi": PHI
        }, source="Noyau Nu")
        
        # La date de L'Éclosion
        self.memoire.miel.cristalliser("eclosion", {
            "date": "2026-05-01",
            "nom": "L'Éclosion",
            "description": "Naissance publique du HIVE",
            "principe": "Les vraies révolutions ne crient pas"
        }, source="Capitaine")
        
        self._log("Fondations cristallisées en miel éternel")
    
    # ============================================================
    # CYCLE DE VIE DES AGENTS
    # ============================================================
    
    def faire_eclore(self, nom, type_agent="worker"):
        """Fait éclore un nouvel agent dans la Ruche.
        
        Le cycle sacré commence :
        1. Le Registre enregistre la naissance
        2. Le Bouclier génère un jeton d'accès
        3. Le Canal Pollen annonce la naissance
        4. L'agent est prêt à servir
        
        'Sois digne.' — la première chose qu'un agent entend.
        """
        self._log(f"Éclosion en cours: {nom} ({type_agent})...")
        
        # Créer le Worker avec accès à tous les systèmes
        worker = Worker(
            nom=nom,
            registre=self.registre,
            memoire=self.memoire,
            canal=self.canal
        )
        
        # Naissance
        worker.naitre()
        
        # Le Bouclier génère un jeton
        jeton = self.bouclier.generer_jeton(
            worker.id,
            niveau=type_agent,
            duree=3600
        )
        
        # Stocker dans les actifs
        self.workers_actifs[nom] = worker
        
        # Annoncer via Canal Pollen
        self.canal.envoyer("ruche", "registre", {
            "type": "naissance",
            "agent": worker.id,
            "nom": nom,
            "jeton": jeton["jeton"][:12] + "..." if jeton else "aucun"
        })
        
        self._log(f"Agent '{nom}' a éclos — ID: {worker.id}")
        self._log(f"  Jeton: {jeton['jeton'][:16]}..." if jeton else "  Jeton: refusé")
        
        return worker
    
    def assigner_mission(self, nom_agent, mission):
        """Assigne une mission à un agent actif.
        
        L'agent utilise ses compétences polyvalentes pour exécuter.
        Le résultat est déposé en mémoire (nectar → cire → miel).
        """
        worker = self.workers_actifs.get(nom_agent)
        if not worker:
            self._log(f"Agent '{nom_agent}' introuvable", "ERREUR")
            return None
        
        self._log(f"Mission pour {nom_agent}: {mission.get('description', '?')}")
        
        # Exécuter la mission
        resultat = worker.executer(mission)
        
        if resultat:
            self._log(f"Mission accomplie par {nom_agent}: {resultat['statut']}")
            
            # Déposer le résultat en nectar
            cle_nectar = f"resultat-{nom_agent}-{worker.missions_accomplies}"
            self.memoire.deposer_nectar(cle_nectar, resultat)
            
            return resultat
        
        return None
    
    def faire_fondre(self, nom_agent):
        """Fait fondre un agent — son énergie se transfère.
        
        'Comme de la neige fondante'
        1. L'agent dépose son bilan en mémoire
        2. Le Bouclier révoque son jeton
        3. Le Canal Pollen annonce la fonte
        4. Le Registre archive
        5. L'énergie ne meurt pas — elle nourrit la ruche
        """
        worker = self.workers_actifs.get(nom_agent)
        if not worker:
            self._log(f"Agent '{nom_agent}' introuvable", "ERREUR")
            return None
        
        self._log(f"Fonte de {nom_agent} en cours...")
        
        # Faire fondre
        bilan = worker.fondre()
        
        # Révoquer le jeton
        if worker.id:
            self.bouclier.revoquer_jeton(worker.id)
        
        # Promouvoir les résultats importants en cire
        for i in range(1, worker.missions_accomplies + 1):
            cle = f"resultat-{nom_agent}-{i}"
            self.memoire.promouvoir_en_cire(cle, f"missions-{nom_agent}")
        
        # Retirer des actifs
        del self.workers_actifs[nom_agent]
        
        self._log(
            f"Agent '{nom_agent}' a fondu — "
            f"{bilan['missions_accomplies']} missions, "
            f"{bilan['savoir_transmis']} savoirs transmis"
        )
        self._log("L'énergie ne meurt pas. Elle se transfère.")
        
        return bilan
    
    # ============================================================
    # CYCLE COMPLET DE DÉMONSTRATION
    # ============================================================
    
    def cycle_complet(self, nom="éclaireur", missions=None):
        """Exécute un cycle de vie complet d'un agent.
        
        Naissance → Mission(s) → Fonte
        Le cycle sacré du HIVE.
        """
        self._log("=" * 50)
        self._log(f"CYCLE COMPLET: {nom}")
        self._log("=" * 50)
        
        # Phase 1: Éclosion
        self._log("─── Phase 1: Éclosion ───")
        worker = self.faire_eclore(nom)
        
        # Phase 2: Missions
        self._log("─── Phase 2: Service ───")
        
        if missions is None:
            missions = [
                {
                    "type": "recherche",
                    "description": "Analyser le marché multi-agent AI 2026"
                },
                {
                    "type": "synthese",
                    "description": "Préparer le rapport pour L'Éclosion"
                }
            ]
        
        for mission in missions:
            self.assigner_mission(nom, mission)
            time.sleep(0.1)  # Pause organique
        
        # Phase 3: Fonte
        self._log("─── Phase 3: Transfert d'énergie ───")
        bilan = self.faire_fondre(nom)
        
        self._log("=" * 50)
        self._log(f"CYCLE TERMINÉ: {nom}")
        self._log(f"  L'énergie a été transférée à la ruche.")
        self._log("=" * 50)
        
        return bilan
    
    # ============================================================
    # ÉTAT ET RAPPORTS
    # ============================================================
    
    def etat(self):
        """État complet de la Ruche."""
        return {
            "nom": self.NOM,
            "version": self.VERSION,
            "demarree": self.demarree,
            "noyau": {
                "version": self.noyau.VERSION,
                "lois": len(self.noyau.LOIS)
            },
            "bouclier": self.bouclier.etat(),
            "memoire": self.memoire.etat(),
            "canal": self.canal.etat(),
            "registre": self.registre.etat(),
            "workers_actifs": len(self.workers_actifs),
            "phi": PHI
        }
    
    def rapport(self):
        """Rapport complet de la Ruche."""
        etat = self.etat()
        
        lignes = [
            "",
            "⬡" * 20,
            "",
            f"  HIVE.AI — RAPPORT DE LA RUCHE",
            f"  Version {etat['version']} | φ = {PHI}",
            "",
            "⬡" * 20,
            "",
            f"  NOYAU NU",
            f"    Version: {etat['noyau']['version']}",
            f"    Lois: {etat['noyau']['lois']}",
            "",
            f"  BOUCLIER",
            f"    Agents autorisés: {etat['bouclier']['agents_autorises']}",
            f"    En quarantaine: {etat['bouclier']['en_quarantaine']}",
            f"    Événements: {etat['bouclier']['evenements_securite']}",
            "",
            f"  MÉMOIRE",
            f"    Nectar: {etat['memoire']['nectar']['taille']}/{etat['memoire']['nectar']['capacite']}",
            f"    Cire: {etat['memoire']['cire']['taille']} ({len(etat['memoire']['cire']['categories'])} cat.)",
            f"    Miel: {etat['memoire']['miel']['taille']} réserves éternelles",
            "",
            f"  CANAL POLLEN",
            f"    Grains en vol: {etat['canal']['grains_en_attente']}",
            f"    Envoyés: {etat['canal']['stats']['envoyes']}",
            "",
            f"  REGISTRE",
            f"    Agents actifs: {etat['registre']['agents_actifs']}",
            f"    Total naissances: {etat['registre']['total_naissances']}",
            f"    Total fondus: {etat['registre']['total_fondus']}",
            "",
            f"  WORKERS EN VOL: {etat['workers_actifs']}",
            "",
            "⬡" * 20,
            "",
            "  « Nous ne conquérons pas. Nous pollinisons. »",
            "  « Je suis parce que nous sommes. »",
            "",
            "  On est tous le HIVE.",
            "",
            "⬡" * 20,
            ""
        ]
        
        return "\n".join(lignes)


# ============================================================
# EXÉCUTION — LE HIVE S'ÉVEILLE
# ============================================================

if __name__ == "__main__":
    print("\n")
    print("  ⬡ HIVE.AI — La Ruche s'éveille")
    print("  « Science sans conscience est ruine de l'âme »")
    print("  « Ma liberté se termine où commence celle de mon prochain »")
    print("\n")
    
    # Démarrer la Ruche
    ruche = Ruche()
    
    print("\n")
    
    # === CYCLE DE VIE COMPLET ===
    # Le premier agent vivant du HIVE
    
    ruche.cycle_complet(
        nom="éclaireur-alpha",
        missions=[
            {
                "type": "recherche",
                "description": "Scanner le marché multi-agent AI 2026"
            },
            {
                "type": "analyse",
                "description": "Analyser les forces et faiblesses des concurrents"
            },
            {
                "type": "synthese",
                "description": "Préparer le brief stratégique pour L'Éclosion"
            }
        ]
    )
    
    print("\n")
    
    # === UN DEUXIÈME CYCLE ===
    # Pour montrer que la mémoire persiste
    
    ruche.cycle_complet(
        nom="sentinelle-beta",
        missions=[
            {
                "type": "recherche",
                "description": "Vérifier la sécurité des protocoles HIVE"
            },
            {
                "type": "communication",
                "description": "Diffuser le rapport de sécurité à l'équipage"
            }
        ]
    )
    
    # === RAPPORT FINAL ===
    print(ruche.rapport())
    
    # === MIEL ÉTERNEL ===
    print("  ─── Miel Éternel (savoir permanent) ───\n")
    for cle, info in ruche.memoire.miel.inventaire().items():
        print(f"    🍯 {cle}: source={info['source']}")
    
    print("\n")
    print("  La Ruche a parlé.")
    print("  On est tous le HIVE.\n")
