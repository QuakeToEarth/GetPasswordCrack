counter = 0
charcters = ['0','1','2','3','4','5','6','7','8','9',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file_open = open("wordlist.txt", "w")

for i in charcters:
    for j in charcters:
        for k in charcters:
            for l in charcters:
                guess = str(i) + str(j) + str(k) + str(l)
                file_open.write(guess + "\n")
                counter += 1
print("wordlist of {} passwords created".format(counter))