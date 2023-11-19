fileopen = open("wordlist.txt")
lines = fileopen.readlines()
for i in lines:
    print(i[0:4])