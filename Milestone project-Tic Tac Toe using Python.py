import random

def choose_first():
    preference = random.randint(1,2)
    print(f'The player {preference} is going to make the first move')
    return preference

def display_board(board):  #Instead of using a nested list we use a single list and use print function to print this list like a game board
    print('\n' * 100)
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
    print('\n')

def choose_marker(preference):
    player1=''
    player2=''
    if preference==1:
        player1 = input('Player 1 please choose between X or O as your marker: \n').upper()
        if player1=='X':
            player2='O'
        else:
            player2='X'
    elif preference==2:
        player2 = input('Player 2 please choose between X or O as your marker: \n').upper()
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
    return (player1,player2)

def feasible_move(board,position):
    if board[position]==" ":
        return True
    else:
        return False

def move(board,marker,position):
        board[position]= marker
        return board

def win_check(board, mark):
    if board[1] ==board[2]==board[3]==mark:   #Checking for 1st row of the board if has 3 of the same markers
        return True
    elif board[4] ==board[5]==board[6]==mark: #Checking for 2nd row of the board if has 3 of the same markers
        return True
    elif board[7] ==board[8]==board[9]==mark: #Checking for 3rd row of the board if has 3 of the same markers
        return True
    elif board[1] == board[4] == board[7] == mark: #Checking for 1st column of the board if has 3 of the same markers
        return True
    elif board[2] == board[5] == board[8] == mark: #Checking for 2nd column of the board if has 3 of the same markers
        return True
    elif board[3] == board[6] == board[9] == mark: #Checking for 3rd column of the board if has 3 of the same markers
        return True
    elif board[1] == board[5] == board[9] == mark: #Checking for 1st diagonal
        return True
    elif board[3] == board[5] == board[7] == mark: #Checking for 2nd diagonal
        return True
    else:
        return False

def is_filled(board):
    if " " not in board:
        return True
    else:
        return False

game_status = True
board=[" "]*10
preference = choose_first()
display_board(board)
player1_marker,player2_marker=choose_marker(preference)

while game_status:
    board = [" "] * 10
    preference = choose_first()
    display_board(board)
    player1_marker, player2_marker = choose_marker(preference)


    if preference==1:
        player1_move=True
        player2_move=True
        while player1_move:
            position1 = int(input('Player 1 please enter the number between 1-9 for which you want a mark on the board '))
            if feasible_move(board,position1):
                board = move(board, player1_marker, position1)
                player1_move=False
            else:
                print('The position you want to mark is already occupied')

        display_board(board)
        if win_check(board,player1_marker):
            print('Player 1 has won the game')
            game_status=False
            break
        if is_filled(board):
            print("All the places within the board are filled, So it's a tie")
            game_status=False
            break
        while player2_move:
            position2 = int(input('Player 2 please enter the number between 1-9 for which you want a mark on the board '))
            if feasible_move(board,position2):
                board = move(board, player2_marker, position2)
                player2_move=False
            else:
                print('The position you want to mark is already occupied')
        display_board(board)
        if win_check(board,player2_marker):
            print('Player 2 has won the game')
            game_status=False
            break
        if is_filled(board):
            print("All the places within the board are filled, So it's a tie")
            game_status=False
            break

    elif preference==2:
        player1_move = True
        player2_move = True
        while player2_move:
            position2 = int(input('Player 2 please enter the number between 1-9 for which you want a mark on the board '))
            if feasible_move(board,position2):
                board = move(board, player2_marker, position2)
                player2_move=False
            else:
                print('The position you want to mark is already occupied')
        display_board(board)
        if win_check(board, player2_marker):
            print('Player 2 has won the game')
            game_status = False
            break
        if is_filled(board):
            print("All the places within the board are filled, So it's a tie")
            game_status = False
            break
        while player1_move:
            position1 = int(input('Player 1 please enter the number between 1-9 for which you want a mark on the board '))
            if feasible_move(board, position1):
                board = move(board, player1_marker, position1)
                player1_move = False
            else:
                print('The position you want to mark is already occupied')
        display_board(board)
        if win_check(board, player1_marker):
            print('Player 1 has won the game')
            game_status = False
            break
        if is_filled(board):
            print("All the places within the board are filled, So it's a tie")
            game_status = False
            break




