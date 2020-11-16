'''
Interns Task

Obasi Franklin


HELP:
-----
The script contains six funtions
1) random_position
    This parameterless function returns an encoded string with neat formating structure for 
    position pieces randomly in a chess board

2) print_position
     This function's duty is to take one single argument, which is an encoded string. It
     uses the format structure of the encoded string to display and position the pieces on 
     terminal window as if it were a chess board

3) main
   This is the function that calls every other function in this script. It provides answers 
   to the given task

4) findPieceIndex
    This function returns a tuple (row index, column index) of a piece. It takes two parameters;
    encoded_string and piece

5) whiteKing_dangerZones
     This function returns a list of possible positions that a black piece exerts dominance. it
     takes in just one argument, which is the enconded string

6) whieKing_check
     This function is used to check if the white king is in danger. It returns true when the
     king is in danger and False when the king is safe. it takes encoded string as its only
     parameter.

'''

from random import randint as r
from random import choice



def main():
    encoded_string = random_position()
    print_position(encoded_string)

    print('\nThe position of white king is :', findPieceIndex(encoded_string, 'x'))

    print('is the white king in check?')
    print('result: ', whiteKing_check(encoded_string))

def random_position():
    string = ''
    
    pieces = ["X","x","Q","q","R","r","K","k","B","b", "P", "p"] # All kinds of pieces on a customary chess
    norm_pieces = pieces[-2:] # Pawns
    used_piece = []

    for __ in range(64):#----------------------- Because there are 64 squares on a chess board
        flag = True
        while flag:
            _ = r(1, 10)# -----------------------generate an integer between 1 and 10
            
            if _%2 == 1:# -----------------------if the integer is an odd number,   
                string += "*" #                   concat an asterik(*) to our string variable name and break the while loop
                flag = False                     
            
            else:
                insert = choice(pieces)# --------the program chooses any piece from the pieces list
                
                if insert in norm_pieces:# ------ checks whether piece is a pawn
                    string += insert #             if it is a pawn, concat it to the string variable name and break the while loop
                    flag = False
                    
                elif insert not in used_piece:#--- when the piece chosen isn't a pawn, that is, it is an special piece
                    string += insert #             make sure that it has not been used before, then concat it to the string variable name
                    used_piece.append(insert) #    then add the piece to the list of special pieces that has been used
                    flag = False

    return string

def print_position(encoded_string):
    print('\nThe string encoding of the positioning is :\n',
     encoded_string,
      '\n\n')

    index = 0
    chess_board = [] # Empty

    # Create the board and fix pieces in following format of encoded strings
    for _ in range(8):
        # Create new row for each iteration
        row = []
        for __ in range(8):
            square_input = encoded_string[index]

            # Handle irrelevances in the encoded string
            if square_input == '*':
                square_input = ' '
            
            row.append(square_input)
            index += 1
        
        # Add new constructed row to the Chess board
        chess_board.append(row)

    #Pretty print the chess board
    for i in range(8):
        for j in range(8):
            square = "|" + chess_board[i][j]
            if j == 7: 
                square += "|"
            print(square,end="")
        print()

def findPieceIndex(encoded_string, piece):
    pos = 0
    for i in range(8):
        for j in range(8):
            if encoded_string[pos] == piece:
                return (i, j)
            
            pos += 1

def whiteKing_dangerZones(encoded_string):
    enemy_pieces = ['X','Q','K','B','R','P']
    enemy_zone = [] #                              -------------list of zones that keeps the white king in check
    for piece in enemy_pieces:
        if piece == 'K' and piece in encoded_string:      #-----BLACK KNIGHT-----
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            knight_moves = ((x - 1, y + 2), #possible knight moves
                            (x + 1, y + 2),
                            (x - 2, y + 1),
                            (x + 2, y + 1),
                            (x - 2, y - 1),
                            (x + 2, y - 1),
                            (x - 1, y - 2),
                            (x + 1, y - 2))

            for move in knight_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move)

        elif piece == 'X' and piece in encoded_string:    #------BLACK KING-------
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            king_moves = ((x - 1, y),  # possible black king moves
                          (x + 1, y),
                          (x, y + 1),
                          (x, y - 1),
                          (x + 1, y + 1),
                          (x - 1, y + 1),
                          (x - 1, y - 1),
                          (x + 1, y - 1))

            for move in king_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move)

        elif piece == 'B' and piece in encoded_string:    #------BLACK BISHOP-----
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            # case 1 - NE , North-East movement
            increment = 0
            NE_moves = []
            for _ in range(8):
                increment += 1
                move = (x + increment, y + increment)
                NE_moves.append(move)

            #case 2 - SE, South-East movemnt
            increment = 0
            SE_moves = []
            for _ in range(8):
                increment += 1
                move = (x + increment, y - increment)
                SE_moves.append(move)

            #case 3 - SW, South-West movemnt
            increment = 0
            SW_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y - increment)
                SW_moves.append(move)

            #case 4 - NW, North-West movemnt
            increment = 0
            NW_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y + increment)
                NW_moves.append(move)

            bishop_moves = tuple(SE_moves) + tuple(SW_moves) + tuple(NE_moves) + tuple(NW_moves)

            for move in bishop_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move)

        elif piece == 'R' and piece in encoded_string:    #------BLACK ROOK------
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            #case 1 - N, North movement
            increment = 0
            N_moves = []
            for _ in range(8):
                increment += 1
                move = (x , y + increment)
                N_moves.append(move)

            #case 2 - E, East movement
            increment = 0
            E_moves = []
            for _ in range(8):
                increment += 1
                move = (x + 1, y)
                E_moves.append(move)

            #case 3 - S, South movement
            increment = 0
            S_moves = []
            for _ in range(8):
                increment += 1
                move = (x , y - increment)
                S_moves.append(move)

            #case 4 - W, West movement
            increment = 0
            W_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y)
                W_moves.append(move)
            
            rook_moves = tuple(S_moves) + tuple(W_moves) + tuple(E_moves) + tuple(N_moves)

            for move in rook_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move)

        elif piece == 'Q' and piece in encoded_string:    #------BLACK QUEEN-----
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            '''
            The queen's move is a combination of both the bishop's moves and the rook's move.
            so i will be creating a total of 8 cases here
            4 cases for bishop-like possible moves
            4 cases for rook-like possible moves
            '''

            # case 1 - NE , North-East movement
            increment = 0
            NE_moves = []
            for _ in range(8):
                increment += 1
                move = (x + increment, y + increment)
                NE_moves.append(move)

            #case 2 - SE, South-East movemnt
            increment = 0
            SE_moves = []
            for _ in range(8):
                increment += 1
                move = (x + increment, y - increment)
                SE_moves.append(move)

            #case 3 - SW, South-West movemnt
            increment = 0
            SW_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y - increment)
                SW_moves.append(move)

            #case 4 - NW, North-West movemnt
            increment = 0
            NW_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y + increment)
                NW_moves.append(move)

            queen_bishopLike_moves = tuple(SE_moves) + tuple(SW_moves) + tuple(NE_moves) + tuple(NW_moves)

             #case 5 - N, North movement
            increment = 0
            N_moves = []
            for _ in range(8):
                increment += 1
                move = (x , y + increment)
                N_moves.append(move)

            #case 6 - E, East movement
            increment = 0
            E_moves = []
            for _ in range(8):
                increment += 1
                move = (x + 1, y)
                E_moves.append(move)

            #case 7 - S, South movement
            increment = 0
            S_moves = []
            for _ in range(8):
                increment += 1
                move = (x , y - increment)
                S_moves.append(move)

            #case 8 - W, West movement
            increment = 0
            W_moves = []
            for _ in range(8):
                increment += 1
                move = (x - increment, y)
                W_moves.append(move)
            
            queen_rookLike_moves = tuple(S_moves) + tuple(W_moves) + tuple(E_moves) + tuple(N_moves)

            # queen's possible move is the combination of biship-like moves and rook-like moves 
            queen_moves = queen_bishopLike_moves + queen_rookLike_moves

            for move in queen_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move)

        elif piece == 'P' and piece in encoded_string:    #------BLACK PAWN------
            position = findPieceIndex(encoded_string, piece)
            x = position[0]
            y = position[1]

            pawn_moves = ((x - 1, y + 1),   #Pawn kill moves
                          (x + 1, y + 1))

            for move in pawn_moves:
                a = move[0]
                b = move[1]
                if a < 0 or b < 0:
                    pass
                else:
                    enemy_zone.append(move) 
    
    return enemy_zone

def whiteKing_check(encoded_string):
    enemy_zone = whiteKing_dangerZones(encoded_string)
    whiteKing_position = findPieceIndex(encoded_string, 'x')
    if whiteKing_position in enemy_zone:
        return True
    else:
        return False


if __name__ == '__main__':
    main()