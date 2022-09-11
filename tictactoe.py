
def introduction():
    print('WELCOME TO THE GAME')
    
    player1 = input('Player 1 pick a symbol- X or O: ')
    player1 = player1.lower()

    while player1 not in ['x','o']:
        player1 = input('Player 1 pick a symbol- X or O: ')
        player1 = player1.lower()
        
    if player1 == 'x':
        return ('X','O')
    else:
        return ('O','X')

def next_player(num:int):
    if num == 1:
        return 2
    return 1

def game_won(board: dict):
    #r1, r2, r3, c1, c2, c3, d1, d2
    winning_combo = ['XXX','OOO']

    r1 = board['7'] + board['8'] + board['9']
    r2 = board['4'] + board['5'] + board['6']
    r3 = board['1'] + board['2'] + board['3']
    c1 = board['7'] + board['4'] + board['1']
    c2 = board['8'] + board['5'] + board['2']
    c3 = board['9'] + board['6'] + board['3']
    d1 = board['7'] + board['5'] + board['3']
    d2 = board['9'] + board['5'] + board['1']

    if r1 in winning_combo: 
        return True
    if r2 in winning_combo: 
        return True
    if r3 in winning_combo: 
        return True
    if c1 in winning_combo: 
        return True
    if c2 in winning_combo: 
        return True
    if c3 in winning_combo: 
        return True
    if d1 in winning_combo: 
        return True
    if d2 in winning_combo: 
        return True

    return False

def print_board(board:dict):
    print(board['7'], board['8'], board['9'])
    print(board['4'], board['5'], board['6'])
    print(board['1'], board['2'], board['3'] )

def play_game(players:set):
    all_moves = []
    p1_moves = []
    p2_moves = []
    
    current_player = 2

    while(len(all_moves) < 9):
        current_player = next_player(current_player)
        
        
        move = input(f'Player {current_player} make a move from [1-9]: ')
        while (not move.isdigit()) or (int(move) not in range(1,10)) or (move in all_moves):
            move = input(f'Invalid move Player {current_player}! Make another move from [1-9]: ')

    
        board = {'7':'','8':'','9':''
                ,'4':'','5':'','6':''
                ,'1':'','2':'','3':''}
        
        if current_player == 1:
            p1_moves.append(move)
        else:
            p2_moves.append(move)
        
        if len(p1_moves) > 0:
            for num in p1_moves:
                str_num = str(num)
                if board[str_num] == '':
                    board[str_num] = players[0]
    
        if len(p2_moves) > 0:
            for num in p2_moves:
                str_num = str(num)
                if board[str_num] == '':
                    board[str_num] = players[1]
        
        if game_won(board):
            print(f'Congratulations Player {current_player}! You won!!')
            break

        all_moves.append(move)
        if len(all_moves) == 9:
            print('We have a tie!')
            break

        print('This is the current board')
        print_board(board)
    
    
    print_board(board)
       

def main():
    players = introduction()
    p1 = players[0]
    p2 = players[1]
    print(f'player 1 is {p1} while player 2 is {p2}')
    play_game(players)

main()