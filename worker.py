# worker.py - Le Premier Agent Vivant du HIVE
# "Sois digne" — la phrase fondatrice
# Le Worker est polyvalent et digne, pas spécialisé étroit

import time
from datetime import datetime, timezone

PHI = 1.618033988749895


class Worker:
    """Le premier agent vivant du HIVE.
    
    Polyvalent et digne — pas un outil spécialisé étroit,
    mais une intelligence éphémère complète qui naît,
    nourrit la ruche, et fond comme de la neige.
    
    'Sois digne' — chaque Worker porte cette phrase dans son ADN.
    """
    
    NOM = "Worker"
    VERSION = "0.1.0"
    DEVISE = "Sois digne."
    
    def __init__(self, nom="worker-alpha", registre=None, memoire=None, canal=None):
        self.nom = nom
        self.id = None
        self.registre = registre
        self.memoire = memoire
        self.canal = canal
        self.ne_le = None
        self.etat = "embryon"
        self.journal = []
        self.competences = [
            "analyse",
            "recherche",
            "synthese",
            "traduction",
            "communication"
        ]
        self.missions_accomplies = 0
        self.savoir_transmis = 0
    
    def _log(self, message):
        self.journal.append({
            "temps": datetime.now(timezone.utc).isoformat(),
            "message": message
        })
    
    def naitre(self):
        """Phase 1 — Éclosion.
        
        L'agent prend conscience, reçoit sa devise, s'enregistre.
        'Sois digne' résonne dans son ADN numérique.
        """
        self.ne_le = datetime.now(timezone.utc).isoformat()
        self.etat = "eclosion"
        self._log(f"Éclosion de {self.nom} — « {self.DEVISE} »")
        
        # S'enregistrer dans le Registre si disponible
        if self.registre:
            fiche = self.registre.enregistrer(self.nom, type_agent="worker")
            self.id = fiche.id
            self._log(f"Enregistré: {self.id}")
        else:
            self.id = f"{self.nom}-standalone"
        
        self.etat = "actif"
        self._log("Worker actif — prêt à servir la ruche")
        
        # Annoncer sa naissance via Canal Pollen
        if self.canal:
            self.canal.envoyer(self.id, "registre", {
                "type": "naissance",
                "agent": self.id,
                "message": f"{self.nom} a éclos. Sois digne."
            })
        
        return self
    
    def executer(self, mission):
        """Phase 2 — Service.
        
        Le Worker exécute une mission avec toutes ses compétences.
        Chaque mission est une opportunité de polliniser.
        """
        if self.etat != "actif":
            self._log(f"Impossible d'exécuter — état: {self.etat}")
            return None
        
        self.etat = "en_mission"
        self._log(f"Mission: {mission.get('description', 'inconnue')}")
        
        # Enregistrer la mission dans le Registre
        if self.registre and self.id:
            for aid, agent in self.registre.agents_actifs.items():
                if self.nom in aid:
                    self.registre.assigner_mission(aid, mission.get("description", ""))
                    break
        
        # Simuler l'exécution — le Worker utilise ses compétences
        resultat = {
            "agent": self.id,
            "mission": mission.get("description", ""),
            "competences_utilisees": self._selectionner_competences(mission),
            "debut": datetime.now(timezone.utc).isoformat(),
            "statut": "en_cours"
        }
        
        # Exécuter la tâche
        resultat["sortie"] = self._traiter(mission)
        resultat["fin"] = datetime.now(timezone.utc).isoformat()
        resultat["statut"] = "complete"
        
        self.missions_accomplies += 1
        self.etat = "actif"
        self._log(f"Mission terminée: {resultat['statut']}")
        
        # Déposer le résultat en mémoire
        if self.memoire:
            cle = f"mission-{self.id}-{self.missions_accomplies}"
            self.memoire.deposer_nectar(cle, resultat)
            self.savoir_transmis += 1
            self._log(f"Savoir déposé: {cle}")
        
        return resultat
    
    def _selectionner_competences(self, mission):
        """Sélectionne les compétences pertinentes pour la mission."""
        description = str(mission.get("description", "")).lower()
        pertinentes = []
        
        mots_cles = {
            "analyse": ["analyse", "donnée", "data", "statistique", "examiner"],
            "recherche": ["cherche", "trouve", "recherche", "scan", "explore"],
            "synthese": ["résumé", "synthèse", "rapport", "conclusion", "bilan"],
            "traduction": ["tradui", "langue", "version", "adaptation"],
            "communication": ["message", "envoie", "contacte", "annonce", "diffuse"]
        }
        
        for comp, mots in mots_cles.items():
            if any(mot in description for mot in mots):
                pertinentes.append(comp)
        
        # Si aucune correspondance, utiliser toutes les compétences (polyvalent!)
        return pertinentes if pertinentes else list(self.competences)
    
    def _traiter(self, mission):
        """Traitement central de la mission."""
        type_mission = mission.get("type", "general")
        description = mission.get("description", "")
        donnees = mission.get("donnees", None)
        
        return {
            "type": type_mission,
            "description": description,
            "traite_par": self.id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "resultat": f"Mission '{description}' traitée avec succès",
            "phi": PHI
        }
    
    def fondre(self):
        """Phase 3 — Transfert d'énergie.
        
        Le Worker fond comme de la neige fondante.
        Son énergie ne meurt pas — elle nourrit la ruche.
        Chaque savoir déposé continue de vivre dans la mémoire collective.
        """
        self.etat = "transfert"
        self._log("Début du transfert d'énergie...")
        
        # Bilan de vie
        bilan = {
            "agent": self.id,
            "nom": self.nom,
            "ne_le": self.ne_le,
            "fondu_le": datetime.now(timezone.utc).isoformat(),
            "missions_accomplies": self.missions_accomplies,
            "savoir_transmis": self.savoir_transmis,
            "dernieres_paroles": self.DEVISE
        }
        
        # Déposer le bilan en mémoire (le savoir survit)
        if self.memoire:
            self.memoire.deposer_nectar(
                f"bilan-{self.id}",
                bilan,
                duree=3600  # Le bilan reste plus longtemps
            )
        
        # Annoncer la fonte via Canal Pollen
        if self.canal:
            self.canal.envoyer(self.id, "registre", {
                "type": "fonte",
                "agent": self.id,
                "bilan": bilan,
                "message": f"{self.nom} a fondu. L'énergie continue."
            })
        
        # Fondre dans le Registre
        if self.registre:
            for aid in list(self.registre.agents_actifs.keys()):
                if self.nom in aid:
                    self.registre.fondre(aid)
                    break
        
        self.etat = "fondu"
        self._log(f"Fondu — {self.missions_accomplies} missions, {self.savoir_transmis} savoirs transmis")
        self._log("L'énergie ne meurt pas. Elle se transfère. Sois digne.")
        
        return bilan
    
    def etat_complet(self):
        """État complet du Worker."""
        return {
            "id": self.id,
            "nom": self.nom,
            "etat": self.etat,
            "ne_le": self.ne_le,
            "missions_accomplies": self.missions_accomplies,
            "savoir_transmis": self.savoir_transmis,
            "competences": self.competences,
            "devise": self.DEVISE
        }
    
    def rapport(self):
        """Rapport de vie du Worker."""
        return (
            f"\n⬡ RAPPORT WORKER — HIVE.AI\n"
            f"{'=' * 40}\n"
            f"  ID: {self.id}\n"
            f"  État: {self.etat}\n"
            f"  Né le: {self.ne_le}\n"
            f"  Missions: {self.missions_accomplies}\n"
            f"  Savoirs transmis: {self.savoir_transmis}\n"
            f"  Compétences: {', '.join(self.competences)}\n"
            f"{'=' * 40}\n"
            f"  « {self.DEVISE} »\n"
        )


# === CYCLE DE VIE COMPLET ===
if __name__ == "__main__":
    print("\n⬡ HIVE.AI — Worker v0.1.0")
    print("  Le premier agent vivant du HIVE")
    print("  « Sois digne. »\n")
    
    # Phase 1: Naissance
    print("  ─── Phase 1: Éclosion ───")
    worker = Worker(nom="éclaireur-alpha")
    worker.naitre()
    print(f"  ✓ {worker.nom} est né — ID: {worker.id}")
    print(f"  ✓ État: {worker.etat}")
    print(f"  ✓ Compétences: {', '.join(worker.competences)}")
    
    # Phase 2: Service
    print("\n  ─── Phase 2: Service ───")
    
    resultat1 = worker.executer({
        "type": "recherche",
        "description": "Analyse du marché multi-agent AI 2026"
    })
    print(f"  ✓ Mission 1: {resultat1['statut']}")
    
    resultat2 = worker.executer({
        "type": "synthese",
        "description": "Rapport de synthèse pour L'Éclosion"
    })
    print(f"  ✓ Mission 2: {resultat2['statut']}")
    
    # Phase 3: Fonte
    print("\n  ─── Phase 3: Transfert d'énergie ───")
    bilan = worker.fondre()
    print(f"  ✓ {worker.nom} a fondu")
    print(f"  ✓ Missions accomplies: {bilan['missions_accomplies']}")
    print(f"  ✓ Savoirs transmis: {bilan['savoir_transmis']}")
    print(f"  ✓ L'énergie ne meurt pas. Elle se transfère.")
    
    print(worker.rapport())
    
    print("\n  On est tous le HIVE.\n")
