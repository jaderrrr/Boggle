import validwordlist
import random

words = validwordlist.create_word_list()

global words_found
words_found = []

class letter:

    def __init__(self, value):
        self.value = value
        self.neighbours = []
        
    def set_neighbour(self, letter):
        self.neighbours.append(letter)

def fill_out_board(board):
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    #dice configuration from english boggle
    die_1 = ["r", "i", "f", "o", "b", "x"]
    die_2 = ["i", "f", "e", "h", "e", "y"]
    die_3 = ["d", "e", "n", "o", "w", "s"]
    die_4 = ["u", "t", "o", "k", "n", "d"]
    die_5 = ["h", "m", "s", "r", "a", "o"]
    die_6 = ["l", "u", "p", "e", "t", "s"]
    die_7 = ["a", "c", "i", "t", "o", "a"]
    die_8 = ["y", "l", "g", "k", "u", "e"]
    die_9 = ["qu", "b", "m", "j", "o", "a"]
    die_10 = ["e", "h", "i", "s", "p", "n"]
    die_11 = ["v", "e", "t", "i", "g", "n"]
    die_12 = ["b", "a", "l", "i", "y", "t"]
    die_13 = ["e", "z", "a", "v", "n", "d"]
    die_14 = ["r", "a", "l", "e", "s", "c"]
    die_15 = ["u", "w", "i", "l", "r", "g"]
    die_16 = ["p", "a", "c", "e", "m", "d"]

    dice = [die_1, die_2, die_3, die_4, die_5, die_6, die_7, die_8,
            die_9, die_10, die_11, die_12, die_13, die_14, die_15, die_16]

    rolls = []
    for die in dice:
        result = die[random.randrange(0, 6)]
        rolls.append(result)
    
    random.shuffle(rolls)

    one = letter(rolls[0])
    board.append(one)

    two = letter(rolls[1])
    board.append(two)

    three = letter(rolls[2])
    board.append(three)

    four = letter(rolls[3])
    board.append(four)

    five = letter(rolls[4])
    board.append(five)

    six = letter(rolls[5])
    board.append(six)

    seven = letter(rolls[6])
    board.append(seven)

    eight = letter(rolls[7])
    board.append(eight)

    nine = letter(rolls[8])
    board.append(nine)

    ten = letter(rolls[9])
    board.append(ten)

    eleven = letter(rolls[10])
    board.append(eleven)

    twelve = letter(rolls[11])
    board.append(twelve)

    thirteen = letter(rolls[12])
    board.append(thirteen)

    fourteen = letter(rolls[13])
    board.append(fourteen)

    fifteen = letter(rolls[14])
    board.append(fifteen)

    sixteen = letter(rolls[15])
    board.append(sixteen)

    #one neighbours
    one.set_neighbour(two)
    one.set_neighbour(five)
    one.set_neighbour(six)

    #two neighbours
    two.set_neighbour(one)
    two.set_neighbour(three)
    two.set_neighbour(five)
    two.set_neighbour(six)
    two.set_neighbour(seven)

    #three neighbours
    three.set_neighbour(two)
    three.set_neighbour(four)
    three.set_neighbour(six)
    three.set_neighbour(seven)
    three.set_neighbour(eight)

    #four neighbours
    four.set_neighbour(three)
    four.set_neighbour(seven)
    four.set_neighbour(eight)

    #five neighbours
    five.set_neighbour(one)
    five.set_neighbour(two)
    five.set_neighbour(six)
    five.set_neighbour(nine)
    five.set_neighbour(ten)

    #six neighbours
    six.set_neighbour(one)
    six.set_neighbour(two)
    six.set_neighbour(three)
    six.set_neighbour(five)
    six.set_neighbour(seven)
    six.set_neighbour(nine)
    six.set_neighbour(ten)
    six.set_neighbour(eleven)

    #seven neighbours
    neighbours = [two, three, four, six, eight, ten, eleven, twelve]
    for elem in neighbours:
        seven.set_neighbour(elem)

    #eight neighbours
    neighbours = [three, four, seven, eleven, twelve]
    for elem in neighbours:
        eight.set_neighbour(elem)

    #nine neighbours
    neighbours = [five, six, ten, thirteen, fourteen]
    for elem in neighbours:
        nine.set_neighbour(elem)

    #ten neighbours
    neighbours = [five, six, seven, nine, eleven, thirteen, fourteen, fifteen]
    for elem in neighbours:
        ten.set_neighbour(elem)

    #eleven neighbours
    neighbours = [six, seven, eight, ten, twelve, fourteen, fifteen, sixteen]
    for elem in neighbours:
        eleven.set_neighbour(elem)

    #twelve neighbours
    neighbours = [seven, eight, eleven, fifteen, sixteen]
    for elem in neighbours:
        twelve.set_neighbour(elem)

    #thirteen neighbours
    neighbours = [nine, ten, fourteen]
    for elem in neighbours:
        thirteen.set_neighbour(elem)

    #fourteen neighbours
    neighbours = [nine, ten, eleven, thirteen, fifteen]
    for elem in neighbours:
        fourteen.set_neighbour(elem)

    #fifteen neighbours
    neighbours = [ten, eleven, twelve, fourteen, sixteen]
    for elem in neighbours:
        fifteen.set_neighbour(elem)

    #sixteen neighbours
    neighbours = [eleven, twelve, fifteen]
    for elem in neighbours:
        sixteen.set_neighbour(elem)

def word_search(node, curr, ok_words, visited):
    new_visited = visited + [node, ]
    
    curr += node.value # this is the current string we are looking for e.g. "a" or "abcd"

    for word in ok_words:
        if curr == word:
            if word not in words_found:
                words_found.append(curr)
    
    i = len(curr) - 1
    
    new_words = []
    
    for word in ok_words:
        if len(word) > i:
            if word[i] == node.value:
                new_words.append(word)

    if len(new_words) != 0:
        for neighbour in node.neighbours:
            if neighbour not in new_visited:
                word_search(neighbour, curr, new_words, new_visited)


def DFS(node):
    print(node.value)
    visited.append(node)

    for neighbour in node.neighbours:
        if neighbour not in visited:
            DFS(neighbour)

def print_board(board):
    to_print = ""
    
    i = 1
    while i <= len(board):
        if i % 4 != 0:
            to_print += board[i-1].value + " "

        else:
            to_print += board[i-1].value + "\n"
        
        i += 1

    print(to_print)

def play_game(board):
    score = 0

    player_words = []
    
    print(words_found)

    print_board(board)
    word = input("Enter word: ")
    
    while word != "q":
        if len(word) < 3:
            print("A valid boggle word must be 3 or more letters.")

        elif word not in words_found:
            print("Invalid word.")

        elif word in player_words:
            print("Word already found.")

        else:
            player_words.append(word)
            score += len(word) - 2
            print(f"{len(player_words)}/{len(words_found)}")
        
        print()

        print_board(board)
        word = input("Enter word: ")

    #print how many found out of total 
    print(f"You found {len(player_words)}/{len(words_found)}, or {len(player_words)/len(words_found) * 100:.2f}% of the possible words.")
    
    max_score = 0
    for word in words_found:
        max_score += len(word) - 2

    print(f"This is a score of {score}/{max_score}")

    print("You missed: ")
    for word in words_found:
        if word not in player_words:
            print(word, end = ", ")

    print()

def main():
    board = []
    fill_out_board(board)

    global words_found
    words_found = []

    ok_words = words
    visited = []

    for i in board:
        word_search(i, "", ok_words, visited)
    
    play_game(board)
    """
    print(f"found {len(words_found)} words: ")
    for word in words_found:
        print(word)
    """

if __name__ == "__main__":
    main()
