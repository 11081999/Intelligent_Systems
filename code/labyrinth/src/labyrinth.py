#This code is a derivative work from the following page
#https://www.techwithtim.net/tutorials/breadth-first-search/

import queue

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze

#   We create the maze
#   # - Wall
#   O - Goal
#   X - Start
#   + - path

def createMaze3():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#"])
    maze.append(["#", "X", "#", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", "O", "#"])
    maze.append(["#", "#", "#", "#", "#", "#"])

    return maze


def printMaze(maze, path=""):
    #   This wont work if the goal is not on the first row.
    for j in range(0, len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == "O":
                start_x = x
                start_y = j

    i = start_x
    j = 0 + start_y
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for j in range(0, len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == "O":
                start_x = x
                start_y = j

    i = start_x
    j = 0 + start_y
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for j in range(0, len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == "O":
                start_x = x
                start_y = j

    i = start_x
    j = 0 + start_y
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("\nFound: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

#FI-FO Queue
nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze3()

while not findEnd(maze, add): 
    add = nums.get()
    print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
