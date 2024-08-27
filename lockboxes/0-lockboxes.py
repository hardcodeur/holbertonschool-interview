#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Vérifie si toutes les boîtes peuvent être déverrouillées à partir de la boîte 0.
    
    Paramètres:
        boxes (list): Liste de boîtes, où chaque boîte contient une liste de clés.
        
    Retourne:
        bool: True si toutes les boîtes peuvent être déverrouillées, sinon False.
    """
    status_boxes = []  # Liste pour suivre l'état de chaque boîte (ouverte ou fermée)
    init_statuboxes(boxes, status_boxes)  # Initialiser l'état des boîtes
    
    keys = boxes[0]  # Commence avec les clés de la première boîte
    for key in keys:
        status_boxes[key] = True  # Déverrouille la boîte correspondant à la clé actuelle
        
        # Récupère les clés dans la boîte déverrouillée
        keys_unlock = boxes[key]
        if keys_unlock:
            for new_key in keys_unlock:
                # Ajoute la nouvelle clé à la liste des clés si elle n'y est pas déjà
                if new_key not in keys:
                    keys.append(new_key)
    
    # Si toutes les boîtes sont déverrouillées (pas de False dans status_boxes)
    if False in status_boxes:
        return False
    else:
        return True


def init_statuboxes(boxes, status_boxes):
    """
    Initialise l'état de chaque boîte (fermée par défaut sauf la première).
    
    Paramètres:
        boxes (list): Liste de boîtes.
        status_boxes (list): Liste qui sera utilisée pour stocker l'état des boîtes.
    """
    for i in boxes:
        status_boxes.append(False)  # Toutes les boîtes sont fermées au départ
    status_boxes[0] = True  # La première boîte est ouverte par défaut
