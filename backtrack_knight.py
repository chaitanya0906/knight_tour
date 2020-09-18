'''''''''''''''''
BackTracking Based Solution

First we go in a particular direction and see if we can find
the solution there if not we move to the next direction by backtracking
at the point after which we couldn't find the solution.

Analysis:

N*N cells.
Memory Complexity: O(N*N) we just need to store the board
Time Complexity: O(8^(N*N)) each location can move atmax 8 position so
upper limit is 8^(N*N).

Next We will explain our Heuristic based Solution.

'''''''''''''''''

rowDir = [2, 1, -1, -2, -2, -1, 1, 2]
colDir = [1, 2, 2, 1, -1, -2, -2, -1]


def canPlaceKnight(board, row, col, n):
   return row >= 0 and col >= 0 and row < n and col < n and board[row][col] == 0


def solveKnightMove(board, n, move_no, currRow, currCol):
	board[currRow][currCol] = move_no
	if move_no == (n*n):
		return True
	for i in range(8):
		nextRow = currRow + rowDir[i]
		nextCol = currCol + colDir[i]
		if canPlaceKnight(board, nextRow, nextCol, n):
			board[nextRow][nextCol] = move_no + 1
			isSuccessfull = solveKnightMove(
                            board, n, move_no+1, nextRow, nextCol)
			if isSuccessfull:
				return True
			board[nextRow][nextCol] = 0
	return False


if __name__ == "__main__":
	print("Size of Board:", end=" ")
	n = int(input())
	board = [[0 for i in range(n)] for i in range(n)]
	if solveKnightMove(board, n, 1, 0, 0):
		for row in board:
			for col in row:
				print(col, end=" ")
			print('\n')
	else:
		print('Not Possible Solution')