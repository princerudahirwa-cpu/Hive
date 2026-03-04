# bouclier.py - Le Bouclier du HIVE
# "Proteger sans dominer, surveiller sans opprimer"
# Loi V - Alvéole du Bouclier

import hashlib
import hmac
import secrets
import time
import json
from datetime import datetime, timezone

# Le nombre d'or - fondation mathématique du HIVE
PHI = 1.618033988749895


class Bouclier:
    """Le Bouclier protège la ruche sans l'opprimer.
    
    Sécurité HMAC, registre d'accès, pare-feu et quarantaine.
    Fondé sur φ (le nombre d'or) comme signature mathématique.
    """

    NOM = "Bouclier"
    VERSION = "0.1.0"
    
    def __init__(self):
        self.cle_maitre = self._generer_cle_maitre()
        self.registre_jetons = {}  # agent_id -> {jeton, expire, niveau}
        self.journal_acces = []    # logs de sécurité
        self.quarantaine = set()   # agents en quarantaine
        self.tentatives_echouees = {}  # agent_id -> count
        self.MAX_TENTATIVES = 5
        self.actif = True
        self._log("Bouclier activé — φ = {:.6f}".format(PHI))
    
    def _generer_cle_maitre(self):
        """Génère une clé maître unique pour cette session."""
        graine = str(PHI) + str(time.time()) + secrets.token_hex(16)
        return hashlib.sha256(graine.encode()).hexdigest()
    
    def _log(self, message, niveau="INFO"):
        """Enregistre un événement dans le journal de sécurité."""
        entree = {
            "temps": datetime.now(timezone.utc).isoformat(),
            "source": "BOUCLIER",
            "message": message,
            "niveau": niveau
        }
        self.journal_acces.append(entree)
        # Garder les 500 derniers logs
        if len(self.journal_acces) > 500:
            self.journal_acces = self.journal_acces[-500:]
        return entree
    
    def generer_jeton(self, agent_id, niveau="worker", duree=3600):
        """Génère un jeton HMAC pour un agent.
        
        Args:
            agent_id: Identifiant unique de l'agent
            niveau: Niveau d'accès (worker, soldier, general, queen)
            duree: Durée de validité en secondes
            
        Returns:
            dict avec jeton et métadonnées
        """
        if agent_id in self.quarantaine:
            self._log(f"Jeton refusé — {agent_id} en quarantaine", "ALERTE")
            return None
        
        # Créer le message à signer
        timestamp = time.time()
        message = f"{agent_id}:{niveau}:{timestamp}:{PHI}"
        
        # Signer avec HMAC-SHA256
        jeton = hmac.new(
            self.cle_maitre.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        # Enregistrer le jeton
        self.registre_jetons[agent_id] = {
            "jeton": jeton,
            "niveau": niveau,
            "cree": timestamp,
            "expire": timestamp + duree,
            "actif": True
        }
        
        self._log(f"Jeton généré pour {agent_id} (niveau: {niveau})")
        return {
            "agent_id": agent_id,
            "jeton": jeton,
            "niveau": niveau,
            "expire_dans": duree
        }
    
    def verifier_jeton(self, agent_id, jeton):
        """Vérifie l'authenticité et la validité d'un jeton.
        
        Returns:
            bool: True si le jeton est valide
        """
        if agent_id in self.quarantaine:
            self._log(f"Accès bloqué — {agent_id} en quarantaine", "ALERTE")
            return False
        
        if agent_id not in self.registre_jetons:
            self._enregistrer_echec(agent_id)
            return False
        
        info = self.registre_jetons[agent_id]
        
        # Vérifier expiration
        if time.time() > info["expire"]:
            self._log(f"Jeton expiré pour {agent_id}", "AVERT")
            del self.registre_jetons[agent_id]
            return False
        
        # Vérifier le jeton (comparaison constante pour éviter timing attacks)
        if not hmac.compare_digest(jeton, info["jeton"]):
            self._enregistrer_echec(agent_id)
            return False
        
        # Vérifier que le jeton est actif
        if not info["actif"]:
            self._log(f"Jeton désactivé pour {agent_id}", "AVERT")
            return False
        
        self._log(f"Accès autorisé — {agent_id}")
        return True
    
    def _enregistrer_echec(self, agent_id):
        """Enregistre une tentative échouée et met en quarantaine si nécessaire."""
        if agent_id not in self.tentatives_echouees:
            self.tentatives_echouees[agent_id] = 0
        
        self.tentatives_echouees[agent_id] += 1
        count = self.tentatives_echouees[agent_id]
        
        self._log(f"Tentative échouée #{count} pour {agent_id}", "AVERT")
        
        if count >= self.MAX_TENTATIVES:
            self.mettre_en_quarantaine(agent_id)
    
    def mettre_en_quarantaine(self, agent_id):
        """Place un agent en quarantaine — isolé de la ruche."""
        self.quarantaine.add(agent_id)
        
        # Révoquer son jeton s'il en a un
        if agent_id in self.registre_jetons:
            self.registre_jetons[agent_id]["actif"] = False
        
        self._log(f"QUARANTAINE — {agent_id} isolé de la ruche", "CRITIQUE")
    
    def liberer_quarantaine(self, agent_id):
        """Libère un agent de quarantaine (nécessite autorisation Capitaine)."""
        if agent_id in self.quarantaine:
            self.quarantaine.discard(agent_id)
            self.tentatives_echouees.pop(agent_id, None)
            self._log(f"Quarantaine levée pour {agent_id}", "INFO")
            return True
        return False
    
    def revoquer_jeton(self, agent_id):
        """Révoque le jeton d'un agent."""
        if agent_id in self.registre_jetons:
            self.registre_jetons[agent_id]["actif"] = False
            self._log(f"Jeton révoqué pour {agent_id}")
            return True
        return False
    
    def generer_watermark(self, contenu):
        """Génère un watermark HIVE pour protéger la propriété intellectuelle.
        
        Utilise φ comme signature cachée dans le hash.
        """
        signature = f"HIVE:{PHI}:{contenu}:{self.cle_maitre[:16]}"
        watermark = hashlib.sha256(signature.encode()).hexdigest()[:16]
        return f"HIVE-{watermark}"
    
    def verifier_watermark(self, contenu, watermark):
        """Vérifie un watermark HIVE."""
        attendu = self.generer_watermark(contenu)
        return hmac.compare_digest(watermark, attendu)
    
    def etat(self):
        """Retourne l'état actuel du Bouclier."""
        return {
            "nom": self.NOM,
            "version": self.VERSION,
            "actif": self.actif,
            "agents_autorises": len([j for j in self.registre_jetons.values() if j["actif"]]),
            "en_quarantaine": len(self.quarantaine),
            "evenements_securite": len(self.journal_acces),
            "phi": PHI
        }
    
    def rapport(self):
        """Génère un rapport de sécurité."""
        etat = self.etat()
        return (
            f"\n⬡ RAPPORT DU BOUCLIER — HIVE.AI\n"
            f"{'=' * 40}\n"
            f"  Version: {etat['version']}\n"
            f"  Statut: {'ACTIF' if etat['actif'] else 'INACTIF'}\n"
            f"  Agents autorisés: {etat['agents_autorises']}\n"
            f"  En quarantaine: {etat['en_quarantaine']}\n"
            f"  Événements: {etat['evenements_securite']}\n"
            f"  Fondation φ: {etat['phi']}\n"
            f"{'=' * 40}\n"
            f"  « Protéger sans dominer,\n"
            f"    surveiller sans opprimer. »\n"
        )


# === EXÉCUTION DIRECTE ===
if __name__ == "__main__":
    print("\n⬡ HIVE.AI — Bouclier v0.1.0")
    print("  Loi V: Protéger sans dominer, surveiller sans opprimer\n")
    
    bouclier = Bouclier()
    
    # Test: générer un jeton pour le Worker
    jeton_info = bouclier.generer_jeton("worker-001", niveau="worker")
    print(f"  ✓ Jeton Worker: {jeton_info['jeton'][:24]}...")
    
    # Test: vérifier le jeton
    valide = bouclier.verifier_jeton("worker-001", jeton_info["jeton"])
    print(f"  ✓ Vérification: {'VALIDE' if valide else 'INVALIDE'}")
    
    # Test: watermark
    wm = bouclier.generer_watermark("HIVE.AI - Swarmly SAS")
    print(f"  ✓ Watermark: {wm}")
    
    # Test: tentative non autorisée
    intrus = bouclier.verifier_jeton("intrus-666", "faux-jeton")
    print(f"  ✓ Intrus bloqué: {'OUI' if not intrus else 'NON'}")
    
    # Rapport
    print(bouclier.rapport())
