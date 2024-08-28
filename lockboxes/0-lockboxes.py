#!/usr/bin/python3
""" Module to determine if all boxes can be unlocked """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked
    :param boxes: List of lists, where each list represents a box
    and contains keys to other boxes.
    :return: True if all boxes can be unlocked, otherwise False.
    """
    statusBoxes = []
    initStatusBoxes(boxes, statusBoxes)  # Initialize the status of all boxes
    keys = boxes[0]  # Get the keys from the first box
    # Iterate through each key in the initial set of keys
    for key in keys:
        if key < len(boxes):  # Ensure the key is a valid index
            statusBoxes[key] = True  # Mark the box as unlocked
            keysUnlock = boxes[key]  # Get the keys from the current box
            if keysUnlock:  # If there are any keys in this box
                for newKey in keysUnlock:  # Iterate through the new keys
                    if newKey not in keys:  # Avoid duplicates
                        keys.append(newKey)  # Add the new key to the keys list
    # Return True if all boxes are unlocked, otherwise return False
    return False not in statusBoxes


def initStatusBoxes(boxes, statusBoxes):
    """
    Initializes the status of all boxes to False, except the first one.
    :param boxes: List of lists, representing the boxes.
    :param statusBoxes: List to store the status of whether
    each box is unlocked or not.
    """
    for _ in boxes:
        statusBoxes.append(False)  # Initially, all boxes are locked
    statusBoxes[0] = True  # The first box is always unlocked
