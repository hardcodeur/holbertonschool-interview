#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked
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
    
    print(statusBoxes)  # Print the status of all boxes for debugging
    
    # Return True if all boxes are unlocked, otherwise return False
    if False in statusBoxes:
        return False
    else:
        return True

def initStatusBoxes(boxes, statusBoxes):
    """
    Initializes the status of all boxes to False, except the first one
    """
    for _ in boxes:
        statusBoxes.append(False)  # Initially, all boxes are locked
    statusBoxes[0] = True  # The first box is always unlocked
