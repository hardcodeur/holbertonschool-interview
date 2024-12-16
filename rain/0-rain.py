#!/usr/bin/python3

def find_next_wall(wall_index, walls):
    """Trouve le prochain mur à droite d'un mur donné.

    Args:
        wall_index (int): L'index du mur actuel.
        walls (list): La liste des hauteurs des murs.

    Returns:
        int: La hauteur du prochain mur ou 0 si aucun mur n'est trouvé.
    """
    for wall in walls[wall_index + 1:]:
        if wall > 0:
            return wall
    return 0  # Retourne 0 si aucun mur n'est trouvé


def count_water_space(wall_index, walls):
    """Compte l'espace d'eau entre le mur donné et le prochain mur.

    Args:
        wall_index (int): L'index du mur actuel.
        walls (list): La liste des hauteurs des murs.

    Returns:
        int: Le nombre d'espaces d'eau entre le mur actuel et le prochain mur.
    """
    water_space = 0
    for wall in walls[wall_index + 1:]:
        if wall > 0:
            return water_space
        water_space += 1
    return water_space  # Retourne l'espace d'eau compté


def rain(walls):
    """Calcule la quantité d'eau de pluie retenue entre les murs.

    Args:
        walls (list): La liste des hauteurs des murs.

    Returns:
        int: La quantité totale d'eau de pluie retenue.
    """
    rainwater = 0
    for wall_index, wall_height in enumerate(walls):
        if wall_height > 0:
            next_wall = find_next_wall(wall_index, walls)
            water_space = count_water_space(wall_index, walls)

            if next_wall > 0 and water_space > 0:
                water_level = min(wall_height, next_wall)
                rainwater += water_level * water_space

    return rainwater
