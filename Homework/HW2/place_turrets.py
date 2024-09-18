#!/usr/local/bin/python3
#
# place_turrets.py : arrange turrets on a grid, avoiding conflicts
#
# Submitted by : erikklem
#
# Based on skeleton code in CSCI B551, Fall 2024.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of turrets on castle_map
def count_turrets(castle_map):
    return sum([ row.count('p') for row in castle_map ] )

# Return a string with the castle_map rendered in a human-turretly format
def printable_castle_map(castle_map):
    return "\n".join(["".join(row) for row in castle_map])

# Add a turret to the castle_map at the given position, and return a new castle_map (doesn't change original)
def add_turret(castle_map, row, col):
    return castle_map[0:row] + [castle_map[row][0:col] + ['p',] + castle_map[row][col+1:]] + castle_map[row+1:]

# Get list of successors of given castle_map state
"""
This function goes through the entire board and places a turret on any spot that has a ".". This is to help with the 
algo, yet the main reason is to generate all possible configurations of the map where one additional turret is placed 
in every available empty position. This helps in exploring different possibilities when trying to solve the problem 
of placing turrets according to the rules. 
"""
def successors(castle_map):
    return [ add_turret(castle_map, r, c) for r in range(0, len(castle_map)) for c in range(0,len(castle_map[0])) if castle_map[r][c] == '.' ]

# check if castle_map is a goal state
def is_goal(castle_map, k):
    return count_turrets(castle_map) == k 

# Arrange turrets on the map
#
# This function MUST take two parameters as input -- the castle map and the value k --
# and return a tuple of the form (new_castle_map, success), where:
# - new_castle_map is a new version of the map with k turrets,
# - success is True if a solution was found, and False otherwise.
#

def checkIfRight(new_castle_map):
    x_indices = []
    w_indices = []
    for i in new_castle_map:
          if i.count('p') >= 2:
               if i.count('X') < 1:
                    return False
               else:
                    for j in range(len(i)):
                        if j[i] == 'p':
                            x_indices.append(i)
                        elif j[i] == 'X':
                             w_indices.append(i)
                    
                    for w in w_indices:
                        for i in range(len(x_indices) - 1):
                            if not(x_indices[i] < w < x_indices[i + 1]):
                                 return False
                        return True
                                 

# Find all the indices of 'W'
                
     

def solve(initial_castle_map,k):
    fringe = [initial_castle_map]
    while len(fringe) > 0:
        for new_castle_map in successors( fringe.pop() ):
            if checkIfRight(new_castle_map):
                 pass
            if is_goal(new_castle_map,k):
                return(new_castle_map,True)
            fringe.append(new_castle_map)

# Main Function
if __name__ == "__main__":
    #castle_map=parse_map(sys.argv[1])
    
    
    
    castle_map=parse_map("C:\\Users\\KLEMS\\OneDrive\\Documents\\Elements-HW-\\Homework\\HW2\\map2.txt")
    
    
    # This is k, the number of turrets
    
    
    
    #k = int(sys.argv[2])
    
    
    
    k = 7
    print ("Starting from initial castle map:\n" + printable_castle_map(castle_map) + "\n\nLooking for solution...\n")
    solution = solve(castle_map,k)
    print ("Here's what we found:")
    print (printable_castle_map(solution[0]) if solution[1] else "False")