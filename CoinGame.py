
initial_board =['H','H','H','H','H','T','T','T','T','T']
final_board = ['_','_','H','T','H','T','H','T','H','T','H','T']
final2_board = ['_','_','T','H','T','H','T','H','T','H','T','H']
final3_board = ['H','T','H','T','H','T','H','T','H','T','_','_']
final4_board = ['T','H','T','H','T','H','T','H','T','H','_','_']
space = '_'

def print_b(c_list):
    print ("".join(c for c in c_list))

def user_in():
    print("Select position:\n")
    print_b(initial_board)
    user_in = input()
    index = len(user_in)
    return index

def swap(board, start):
    second = start+1
    element1 = board[start]
    element2 = board[second]
    
    if space in board:
        space1 = board.index(space)
        space2 = space1+1
        board[start] = space
        board[second] = space
        board[space1] = element1
        board[space2] = element2
        return board
    else:
        print("You can only move to the end or beginning.")
        end = user_in()
        if end == len(board)-1:
            board[start] = space
            board[second] = space
            board.append(element1)
            board.append(element2)
            return board
        elif end == 0:
            board[start] = space
            board[second] = space
            board.insert(0,element2)
            board.insert(0,element1)
            return board
        elif end > 0:
            print("You can only move to the end or beginning.\nYour move was place at the end")
            board[start] = space
            board[second] = space
            board.append(element1)
            board.append(element2)
            return board
    
def game():
    start = user_in()
    while start >= len(initial_board)-1:
        print("Try Again")
        start = user_in()      
    b1 = swap(initial_board, start)
    counter = 1
    while counter != 5:
        while space in b1:
            start1 = user_in()
            swap(b1, start1)
            counter +=1
            if counter == 5:
                if b1 == final_board or b1 == final2_board:
                    print("won")
                    break
                elif b1 == final3_board or b1 == final4_board:
                    print("won")
                    break
                else:
                    print("LOSER")
                    break
            print(counter)
        print_b(b1)


game()
