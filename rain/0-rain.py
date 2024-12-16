#!/usr/bin/python3

""" Module Rain """

def find_next_wall(wall_index, walls):
    """Finds the next wall to the right of a given wall.

    Args:
        wall_index (int): The index of the current wall.
        walls (list): The list of wall heights.

    Returns:
        int: The height of the next wall or 0 if no wall is found.
    """
    for wall in walls[wall_index + 1:]:
        if wall > 0:
            return wall
    return 0  # Returns 0 if no wall is found


def count_water_space(wall_index, walls):
    """Counts the water space between the given wall and the next wall.

    Args:
        wall_index (int): The index of the current wall.
        walls (list): The list of wall heights.

    Returns:
        int: The number of water spaces between the current wall and the next wall.
    """
    water_space = 0
    for wall in walls[wall_index + 1:]:
        if wall > 0:
            return water_space
        water_space += 1
    return water_space  # Returns the counted water space


def rain(walls):
    """Calculates the amount of rainwater trapped between the walls.

    Args:
        walls (list): The list of wall heights.

    Returns:
        int: The total amount of trapped rainwater.
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
