from zipfile import ZipFile
fileopen = open("wordlist.txt")
lines = fileopen.readlines()
counter = 0
for i in lines:
    pw = i[0:4]
    with ZipFile("CrackPassword.zip") as zf:
        try:
            zf.extractall(pwd = bytes(pw,'utf-8'))
            print("success")
        except:
            print('retrying again')
        
