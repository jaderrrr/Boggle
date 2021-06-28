
fd = open("wordlist.txt", "r")

to_write = open("validwordlist.txt", "w")

while True:
    line = fd.readline()

    if not line:
        break
    
    if len(line) <= 17 and len(line) >= 4: # longest boggle word + newline
        to_write.write(line)

fd.close()
to_write.close()

