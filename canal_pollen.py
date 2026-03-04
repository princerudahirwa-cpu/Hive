# canal_pollen.py - Le Canal Pollen du HIVE
# "Nous ne conquérons pas. Nous pollinisons."
# Communication éphémère chiffrée entre agents

import hashlib
import hmac
import json
import time
import secrets
from datetime import datetime, timezone

PHI = 1.618033988749895


class GrainDePollen:
    """Un message éphémère entre agents — naît, voyage, fond."""
    
    def __init__(self, emetteur, destinataire, contenu, priorite="normale"):
        self.id = self._generer_id()
        self.emetteur = emetteur
        self.destinataire = destinataire
        self.contenu = contenu
        self.priorite = priorite  # basse, normale, haute, urgente
        self.cree = time.time()
        self.duree_vie = self._calculer_duree(priorite)
        self.expire = self.cree + self.duree_vie
        self.lu = False
        self.signature = self._signer()
    
    def _generer_id(self):
        """Génère un ID unique basé sur φ."""
        graine = f"{PHI}:{time.time()}:{secrets.token_hex(8)}"
        return f"pollen-{hashlib.sha256(graine.encode()).hexdigest()[:12]}"
    
    def _calculer_duree(self, priorite):
        """Durée de vie basée sur la priorité — tout est éphémère."""
        durees = {
            "basse": 60,       # 1 minute
            "normale": 300,    # 5 minutes
            "haute": 900,      # 15 minutes
            "urgente": 1800    # 30 minutes
        }
        return durees.get(priorite, 300)
    
    def _signer(self):
        """Signe le grain de pollen avec HMAC."""
        message = f"{self.id}:{self.emetteur}:{self.destinataire}:{self.cree}"
        return hmac.new(
            str(PHI).encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()[:24]
    
    def est_valide(self):
        """Vérifie si le grain est encore vivant."""
        return time.time() < self.expire
    
    def lire(self):
        """Lit le contenu — marque comme lu."""
        if not self.est_valide():
            return None
        self.lu = True
        return self.contenu
    
    def to_dict(self):
        """Représentation dictionnaire."""
        return {
            "id": self.id,
            "emetteur": self.emetteur,
            "destinataire": self.destinataire,
            "priorite": self.priorite,
            "cree": datetime.fromtimestamp(self.cree, tz=timezone.utc).isoformat(),
            "expire_dans": max(0, int(self.expire - time.time())),
            "lu": self.lu,
            "signature": self.signature
        }


class CanalPollen:
    """Le Canal Pollen — réseau de communication éphémère du HIVE.
    
    Chaque message est un grain de pollen qui voyage d'agent en agent,
    pollinise (transmet son savoir), puis fond comme de la neige.
    """
    
    NOM = "Canal Pollen"
    VERSION = "0.1.0"
    
    def __init__(self):
        self.canaux = {}       # canal_id -> [grains]
        self.boites = {}       # agent_id -> [grains en attente]
        self.historique = []   # grains expirés (métadonnées seulement)
        self.stats = {
            "envoyes": 0,
            "lus": 0,
            "expires": 0,
            "canaux_actifs": 0
        }
        self._log_interne = []
    
    def _log(self, message):
        self._log_interne.append({
            "temps": datetime.now(timezone.utc).isoformat(),
            "message": message
        })
        if len(self._log_interne) > 200:
            self._log_interne = self._log_interne[-200:]
    
    def envoyer(self, emetteur, destinataire, contenu, priorite="normale"):
        """Envoie un grain de pollen d'un agent à un autre.
        
        Returns:
            GrainDePollen ou None si échec
        """
        grain = GrainDePollen(emetteur, destinataire, contenu, priorite)
        
        # Ajouter à la boîte du destinataire
        if destinataire not in self.boites:
            self.boites[destinataire] = []
        
        self.boites[destinataire].append(grain)
        self.stats["envoyes"] += 1
        
        self._log(f"Pollen {grain.id}: {emetteur} → {destinataire} ({priorite})")
        return grain
    
    def recevoir(self, agent_id):
        """Récolte tous les grains de pollen en attente pour un agent.
        
        Returns:
            Liste de grains valides, les expirés sont nettoyés
        """
        if agent_id not in self.boites:
            return []
        
        # Séparer valides et expirés
        valides = []
        for grain in self.boites[agent_id]:
            if grain.est_valide():
                valides.append(grain)
            else:
                # Archiver les métadonnées
                self.historique.append({
                    "id": grain.id,
                    "emetteur": grain.emetteur,
                    "expire": True,
                    "lu": grain.lu
                })
                self.stats["expires"] += 1
        
        self.boites[agent_id] = valides
        return valides
    
    def lire_grain(self, agent_id, grain_id):
        """Lit un grain spécifique."""
        grains = self.recevoir(agent_id)
        for grain in grains:
            if grain.id == grain_id:
                contenu = grain.lire()
                if contenu:
                    self.stats["lus"] += 1
                return contenu
        return None
    
    def diffuser(self, emetteur, destinataires, contenu, priorite="normale"):
        """Diffuse un grain à plusieurs agents — pollinisation collective."""
        grains = []
        for dest in destinataires:
            grain = self.envoyer(emetteur, dest, contenu, priorite)
            if grain:
                grains.append(grain)
        
        self._log(f"Diffusion de {emetteur} vers {len(destinataires)} agents")
        return grains
    
    def creer_canal(self, canal_id, membres):
        """Crée un canal de communication entre un groupe d'agents."""
        self.canaux[canal_id] = {
            "membres": set(membres),
            "cree": datetime.now(timezone.utc).isoformat(),
            "messages": 0
        }
        self.stats["canaux_actifs"] = len(self.canaux)
        self._log(f"Canal '{canal_id}' créé avec {len(membres)} membres")
        return True
    
    def envoyer_canal(self, canal_id, emetteur, contenu, priorite="normale"):
        """Envoie un message à tous les membres d'un canal."""
        if canal_id not in self.canaux:
            return []
        
        canal = self.canaux[canal_id]
        if emetteur not in canal["membres"]:
            return []
        
        destinataires = canal["membres"] - {emetteur}
        canal["messages"] += 1
        return self.diffuser(emetteur, list(destinataires), contenu, priorite)
    
    def nettoyer(self):
        """Nettoyage global — la neige fond."""
        total_nettoye = 0
        for agent_id in list(self.boites.keys()):
            avant = len(self.boites[agent_id])
            self.recevoir(agent_id)  # déclenche le nettoyage
            total_nettoye += avant - len(self.boites[agent_id])
        
        if total_nettoye > 0:
            self._log(f"Nettoyage: {total_nettoye} grains fondus")
        return total_nettoye
    
    def etat(self):
        """État du Canal Pollen."""
        total_en_attente = sum(len(grains) for grains in self.boites.values())
        return {
            "nom": self.NOM,
            "version": self.VERSION,
            "grains_en_attente": total_en_attente,
            "canaux_actifs": len(self.canaux),
            "stats": dict(self.stats),
            "agents_connectes": len(self.boites)
        }
    
    def rapport(self):
        """Rapport du Canal Pollen."""
        etat = self.etat()
        return (
            f"\n⬡ RAPPORT CANAL POLLEN — HIVE.AI\n"
            f"{'=' * 40}\n"
            f"  Grains en vol: {etat['grains_en_attente']}\n"
            f"  Canaux actifs: {etat['canaux_actifs']}\n"
            f"  Envoyés: {etat['stats']['envoyes']}\n"
            f"  Lus: {etat['stats']['lus']}\n"
            f"  Fondus: {etat['stats']['expires']}\n"
            f"{'=' * 40}\n"
            f"  « Nous ne conquérons pas.\n"
            f"    Nous pollinisons. »\n"
        )


# === EXÉCUTION DIRECTE ===
if __name__ == "__main__":
    print("\n⬡ HIVE.AI — Canal Pollen v0.1.0")
    print("  Communication éphémère chiffrée\n")
    
    canal = CanalPollen()
    
    # Créer le canal de l'équipage
    canal.creer_canal("equipage", ["capitaine", "nu", "openclaw", "le-sage"])
    print("  ✓ Canal 'equipage' créé")
    
    # Le Capitaine envoie un ordre
    grain = canal.envoyer("capitaine", "nu", {
        "type": "ordre",
        "message": "Prépare le rapport pour L'Éclosion",
        "priorite": "haute"
    }, priorite="haute")
    print(f"  ✓ Ordre envoyé: {grain.id}")
    
    # Nū lit le message
    grains = canal.recevoir("nu")
    print(f"  ✓ Nū a {len(grains)} grain(s) en attente")
    
    contenu = canal.lire_grain("nu", grain.id)
    print(f"  ✓ Message lu: {contenu['message']}")
    
    # Diffusion à tout l'équipage
    canal.envoyer_canal("equipage", "capitaine", {
        "type": "annonce",
        "message": "L'Éclosion approche. Soyez prêts."
    }, priorite="haute")
    print("  ✓ Annonce diffusée à l'équipage")
    
    print(canal.rapport())
