#!/usr/bin/python3

def findWall2(wallIndex,walls):
    for wall in walls[wallIndex+1:]:
        if(wall > 0): 
            return wall
        else :
            False
      
def cptWaterSpace(wallIndex,walls):
    waterSpace = 0
    for wall in walls[wallIndex+1:]:
        if(wall > 0): 
            return waterSpace
        else :
            waterSpace += 1

def rain(walls):
    rainwater = 0
    for wall in walls:
      if(wall > 0):
        wallIndex=walls.index(wall)
        wall_1 = wall
        wall_2 = findWall2(wallIndex,walls)
        waterSpace = cptWaterSpace(wallIndex,walls)

        if wall_2 and waterSpace:
            if(wall_1 > wall_2) :
                water = wall_2
            else:
                water = wall_1
            
            rainwater += water * waterSpace

    return rainwater

