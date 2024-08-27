#!/usr/bin/python3
"""
This module contains the canUnlockAll function that determines
if all the boxes in a list can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of list of int): The list of boxes, where each box contains a list of keys.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    status_boxes = []  # List to track which boxes are unlocked
    init_status_boxes(boxes, status_boxes)
    keys = boxes[0]  # Start with the keys in the first box

    # Loop through all the keys to unlock boxes
    for key in keys:
        status_boxes[key] = True  # Unlock the box corresponding to the key
        keys_unlock = boxes[key]  # Get the keys from the newly unlocked box
        if keys_unlock:
            # Add new keys to the list of keys if they are not already present
            for new_key in keys_unlock:
                if new_key not in keys:
                    keys.append(new_key)

    # If any box remains locked, return False
    if False in status_boxes:
        return False
    else:
        return True

def init_status_boxes(boxes, status_boxes):
    """
    Initializes the status of each box to False (locked), except the first one.

    Parameters:
    boxes (list of list of int): The list of boxes.
    status_boxes (list of bool): The list that tracks the lock status of each box.
    """
    for _ in boxes:
        status_boxes.append(False)  # Initially, all boxes are locked
    status_boxes[0] = True  # The first box is always unlocked
