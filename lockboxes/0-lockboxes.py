#!/usr/bin/python3
def canUnlockAll(boxes):
    statusBoxes = []
    initStatuboxes(boxes,statusBoxes)
    keys = boxes[0]
    for key in keys:
        statusBoxes[key] = True
        keysUnlock = boxes[key]
        if keysUnlock:
            for newKey in keysUnlock:
                if newKey not in keys:
                    keys.append(newKey)
    if False in statusBoxes:
        return False
    else:
        return True

def initStatuboxes(boxes,statusBoxes):
    for i in boxes:
        statusBoxes.append(False)
    statusBoxes[0]=True