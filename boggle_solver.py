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

def roll_the_dice():
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

    return rolls

def enter_board():
    
    current_four = input("Please enter the first row, each letter separated by a space: ")
    current_letters = current_four.split()

    rolls = []

    rolls.append(current_letters[0].lower())
    rolls.append(current_letters[1].lower())
    rolls.append(current_letters[2].lower())
    rolls.append(current_letters[3].lower())
    
    i = 0

    while i < 3:
        current_four = input("Please enter the next row, each letter separated by a space: ")
        current_letters = current_four.split()

        rolls.append(current_letters[0].lower())
        rolls.append(current_letters[1].lower())
        rolls.append(current_letters[2].lower())
        rolls.append(current_letters[3].lower())
    
        i += 1

    return rolls


def fill_out_board(game_mode):
    
    if game_mode == "n":
        rolls = roll_the_dice()
    else:
        rolls = enter_board()

    one = letter(rolls[0])
    two = letter(rolls[1])
    three = letter(rolls[2])
    four = letter(rolls[3])
    five = letter(rolls[4])
    six = letter(rolls[5])
    seven = letter(rolls[6])
    eight = letter(rolls[7])
    nine = letter(rolls[8])
    ten = letter(rolls[9])
    eleven = letter(rolls[10])
    twelve = letter(rolls[11])
    thirteen = letter(rolls[12])
    fourteen = letter(rolls[13])
    fifteen = letter(rolls[14])
    sixteen = letter(rolls[15])

    board = [one, two, three, four, five, six, seven, eight, nine, ten, eleven,
            twelve, thirteen, fourteen, fifteen, sixteen]

    #one neighbours
    neighbours = [two, five, six]
    for elem in neighbours:
        one.set_neighbour(elem)

    #two neighbours
    neighbours = [one, three, five, six, seven]
    for elem in neighbours:
        two.set_neighbour(elem)

    #three neighbours
    neighbours = [two, four, six, seven, eight]
    for elem in neighbours:
        three.set_neighbour(elem)

    #four neighbours
    neighbours = [three, seven, eight]
    for elem in neighbours:
        four.set_neighbour(elem)

    #five neighbours
    neighbours = [one, two, six, nine, ten]
    for elem in neighbours:
        five.set_neighbour(elem)

    #six neighbours
    neighbours = [one, two, three, five, seven, nine, ten, eleven]
    for elem in neighbours:
        six.set_neighbour(elem)

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

    return board

def word_search(node, curr, ok_words, visited):
    new_visited = visited + [node, ]
    
    curr += node.value # this is the current string we are looking for e.g. "a" or "abcd"

    #if curr is a valid word, append it to the words_found list
    for word in ok_words:
        if curr == word:
            if word not in words_found:
                words_found.append(curr)
    
    i = len(curr) - 1
    
    new_words = []
    
    for word in ok_words:
        if len(word) > i:
            #'qu' case
            if len(node.value) == 2:
                if word[i-1] == node.value[0] and word[i] == node.value[1]:
                    new_words.append(word)
            #all other letters
            if word[i] == node.value:
                new_words.append(word)

    if len(new_words) != 0:
        for neighbour in node.neighbours:
            if neighbour not in new_visited:
                word_search(neighbour, curr, new_words, new_visited)


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

def welcome():
    print("---------------------")
    print("-~- Boggle Player -~-")
    print("---------------------")

    game_mode = input("Would you like to enter your own board? (y/n) ")

    while game_mode != "y" and game_mode != "n":
        game_mode = input("Incorrect input. Would you like to enter your own board? (y/n) ")

    if game_mode == "n":
        print("Auto-generating a board for you...\n")

    return game_mode

def main():

    game_mode = welcome()

    board = fill_out_board(game_mode)

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
