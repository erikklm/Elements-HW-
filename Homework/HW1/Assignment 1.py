
class FindWayOut():

    myDic = {'U':[-1,0], 'D':[1,0], 'R':[0,1], 'L':[0,-1]}

    def __init__(self, file) -> None:
        self.board = self.makeBoard(file)
        self.start = self.startOfBoard(self.board)
        self.visited = []
    
    def makeBoard(self, file): #This function is going to help actually read in the code and put it into a board variable that is an instance variable
        board = []
        with open(file, 'r') as f:
            for line in f:
                board.append(list(line.strip()))
        return board
    
    def startOfBoard(self, board):
        start = []
        for indexX,x in enumerate(board):
            for indexY,y in enumerate(x):
                if y == 'p':
                    start = [indexX, indexY]
                    return start
    
    def movingOnBoard(self, x, y, path, dist):
        if self.board[x][y] == '@':
            return dist, path


        keepTrack_distance = float('inf')
        keepTrack_path = None

        for walk, [dirX, dirY] in self.myDic.items():
            tempX = dirX + x
            tempY = dirY + y

            if(self.checkIfWall(tempX, tempY) and (self.checkIfMove(tempX, tempY))):
                self.visited.append([tempX, tempY])

                #path.append(walk)
                check_keepTrack_distance, check_keepTrack_path = self.movingOnBoard(tempX, tempY, path + [walk], dist +1)

                if (check_keepTrack_distance < keepTrack_distance):
                    keepTrack_distance = check_keepTrack_distance
                    keepTrack_path = check_keepTrack_path

                self.visited.remove([tempX, tempY])

            

        return keepTrack_distance, keepTrack_path
        


    def checkIfWall(self, x, y):
        if not (0 <= x < len(self.board)):
        #if not((x >= 0) and (x < len(self.board))):
            return False
        #0 <= y
        if not (0 <= y < len(self.board[1])):
            return False
        return True
    
    def checkIfMove(self, x, y):
        if((self.board[x][y] == 'X') or ([x,y] in self.visited)):
            return False
        return True
    

    def convertToString(self, path):
        string = ''
        for i in path:
            string += i
        return string



    def solve(self):
        self.visited.append([self.start[0], self.start[1]])
        dist_traveled, path_taken = self.movingOnBoard(self.start[0], self.start[1], [], 0)
        if dist_traveled == float('inf'):
            print("No path found")
            return None
        #print(dist_traveled, path_taken)
        finalAnswer = self.convertToString(path_taken)
        print(finalAnswer, dist_traveled)




if __name__ == "__main__":
    import sys
    
    escape_solver = FindWayOut("C:\\Users\\KLEMS\\OneDrive\\Documents\\Elements-HW-\\Homework\\HW1\\castle_map. txt")
    escape_solver.solve()
    
    



        



