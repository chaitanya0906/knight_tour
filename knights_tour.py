'''''''''''''''''
import sys
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

import random
import sys
import time
start = time.process_time()
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


KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]


def find_neighbours(board, board_size, pos):
	neighbours = []
	for dx, dy in KNIGHT_MOVES:
		x = pos[0] + dx
		y = pos[1] + dy
		if 0 <= x < board_size and 0 <= y < board_size and board[x][y] is -1:
			neighbours.append((x, y))
	return neighbours


def find_next_pos(board, board_size, current_pos):
	empty_neighbours = find_neighbours(board, board_size, current_pos)
	if len(empty_neighbours) is 0:
		return None

	least_neighbour_pos = {}
	for neighbour in empty_neighbours:
		neighbours_of_neighbour = find_neighbours(board, board_size, neighbour)
		if len(neighbours_of_neighbour) in least_neighbour_pos:
			least_neighbour_pos[len(neighbours_of_neighbour)].append(neighbour)
		else:
			least_neighbour_pos[len(neighbours_of_neighbour)] = [neighbour]
	ind = sorted(least_neighbour_pos)

	# choose randomly among the nodes with least accessible neighbour
	least_neighbour_pos = random.choice(least_neighbour_pos[ind[0]])
	return least_neighbour_pos


def warnsdroff(board_size):

	board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
	indices = [i for i in range(board_size)]
	x_pos,  y_pos = random.choice(indices), random.choice(
            indices)  # choose start node randomly
	move = 1
	board[x_pos][y_pos] = move

	while move <= board_size * board_size:
		move += 1
		next_pos = find_next_pos(board, board_size, (x_pos, y_pos))
		if next_pos:
			x_pos, y_pos = next_pos
			board[x_pos][y_pos] = move
		else:
			break
	if move > board_size * board_size:
		print_board(board)
		return True
	return False


def print_board(board):
	for row in board:
		for col in row:
			print(col, end=" ")
		print('\n')


if __name__ == "__main__":
	print("Size of Board:", end=" ")
	n = int(input())
	board = [[0 for i in range(n)] for i in range(n)]
	is_solution = True
	if len(sys.argv) == 1:
		print("Using Brute force : ")
		if solveKnightMove(board, n, 1, 3, 1):
			print_board(board)
		else:
			print('Not Possible Solution')
			is_solution = False
	print("Using Warnsdorff’s algorithm : ")

	if is_solution is False:  # can run forever , Add some bound on number of interations
		print('Not Possible Solution')

	while warnsdroff(n) == False:
		pass
	print(time.process_time() - start)
