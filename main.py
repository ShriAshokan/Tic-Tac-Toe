import time
 
 
the_board = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',           # the player board
             7: '7', 8: '8', 9: '9'}
 
 
def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])          # prints the board with boundaries
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
 
 
print('Enter player 1 name: ')
player1 = input()
print('Enter player 2 name: ')
player2 = input()                           # set player names, turn var and scoreboard vars
player = player1
turn = 'X'
p1wins = 0
p2wins = 0
 
 
def check_win(board):
    global p1wins, p2wins                      # checks win possibilities and determines a winner
    if (board[1] == board[2] == board[3] != ' ') or (board[4] == board[5] == board[6] != ' ') or \
            (board[7] == board[8] == board[9] != ' ') or (board[1] == board[4] == board[7] != ' ') or \
            (board[2] == board[5] == board[8] != ' ') or (board[3] == board[6] == board[9] != ' ') or \
            (board[3] == board[5] == board[7] != ' ') or (board[1] == board[5] == board[9] != ' '):
        print_board(board)
        print('player ' + player + ' wins!!')
        if turn == 'X':
            p1wins += 1
        else:
            p2wins += 1
        return True
    else:
        return False
 
 
def play():
    global turn, p1wins, p2wins, player1, player2, player
    for i in range(9):
        print_board(the_board)
        print("It's your turn " + player + '.')
        move = input()
        if turn == 'X':
            the_board[int(move)] = '\033[1;31m' + turn + '\033[m'      # the game itself
        else:
            the_board[int(move)] = '\033[1;32m' + turn + '\033[m'
        if check_win(the_board):
            break
        else:
            if turn == 'X':
                turn = '0'
                player = player2
            else:
                turn = 'X'
                player = player1
    print('GAME OVER')
    print(player1 + ' has ' + str(p1wins) + ' wins.')                   # scoreboard
    print(player2 + ' has ' + str(p2wins) + ' wins.')
 
 
print('Imagine the board like this, when you want to enter the desired space simply type in the number as shown here:')
print_board(the_board)
k = 1
while k <= 9:
    the_board[k] = ' '
    k += 1
print('------------------------------------------------')
pos = ['Y', 'YES']
play()
while True:
    print('Do you want to play again?')
    ans = input().upper()
    if ans in pos:
        for x in the_board:
            the_board[x] = ' '
        print('loading...')                          # play again
        time.sleep(2)
        play()
    else:
        break