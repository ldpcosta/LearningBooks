#### Tic Tac Toe

board = {"T-L":" ", "T-M":" ", "T-R":" ",
		 "M-L":" ", "M-M":" ", "M-R":" ",
		 "B-L":" ", "B-M":" ", "B-R":" "}


def drawBoard(board = board):

	print """%s | %s | %s \n %s | %s | %s \n %s | %s | %s """ % (board["T-L"], board["T-M"], board["T-R"],
			 					 								 board["M-L"], board["M-M"], board["M-R"],
			 					 								 board["B-L"], board["B-M"], board["B-R"],)


def play():
	play_board = board
	
	while victory(play_board) != True:
		drawBoard(play_board)
		t = turn(play_board)
		move = raw_input("%s to play \n > " % (t) )

		try:
			if play_board[move] == " ":
				play_board[move] = t
			else:
				print "Invalid play"
		except KeyError:
			print "Invalid play"

	drawBoard(play_board)


def turn(board):

	ls = [item for item in board.values() if item != " "]

	if len(ls)%2 == 0:
		return "X"
	return "O"


def victory(board):
	#diagonals
	if ((board["T-L"] == board["M-M"] == board["B-R"]) or (board["T-R"] == board["M-M"] == board["B-L"])) and (board["M-M"] != " "):
		print board["M-M"]," wins!"
		return True

	#others

	for hor in ["T","M","B"]:
		hor_ls = [board[i] for i in board.keys() if i[0] == hor]

		if (hor_ls[0] == hor_ls[1] == hor_ls[2]) and (" " not in hor_ls):
			print hor_ls[0]," wins!"
			return True

	for ver in ["L","M","R"]:
		ver_ls = [board[i] for i in board.keys() if i[2] == ver]

		if (ver_ls[0] == ver_ls[1] == ver_ls[2]) and (" " not in ver_ls):
			print ver_ls[0]," wins!"
			return True

	return False

play()