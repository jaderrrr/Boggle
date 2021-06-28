
def main():
    #print board
    player_words = []

    word = input("Enter word: ")

    while word != "q":
        
        if len(word) < 3:
            print("A valid boggle word must be 3 or more letters.")

        elif word not in found_words:
            print("This word is impossible to get from this board.")

        else:
            player_words.append(word)
            print(f"{len(player_words)}/{len(found_words)}")

    #print how many found out of total 
    print(f"You found {len(player_words)}/{len(found_words)}, or {len(player_words)/len(found_words) * 100}% of the possible words.")
    
    print("You missed: ")
    for word in found_words:
        if word not in player_words:
            print(word, end = ", ")

    print()

if __name__ == "__main__":
    main()
