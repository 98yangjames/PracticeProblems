#Write a function that prints a chessboard pattern, with "W" being white
#square and "B" being black. Input is an integer that is the number of squares
#on the board. Output is 2D char array. For example,
#Input = 2
#Output =
#W B
#B W

n = 5
arr = [ [0]*n for i in range(n)]

def chessboard(arr, n):
    white = True
    alternate = 0
    for i in range(n):
        for j in range(n):
            if alternate % 2 == 0:
                if j % 2 == 0:
                    arr[i][j] = 'W'
                else:
                    arr[i][j] = "B"
            else:
                if j % 2 == 0:
                    arr[i][j] = 'B'
                else:
                    arr[i][j] = "W"
        alternate +=1 
    return arr
arr = chessboard(arr, n)
for row in arr:
    print(row)