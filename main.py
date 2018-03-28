import Defines

print("Please input your encryption key")
key = raw_input('Key: ').lower()

print("Please input your encryption text")
text = raw_input('Text: ').lower()

pos = 0
ans = ""

for x in text:
    if x == " ":
        ans += " "
        continue
    i = Defines.alphabet.find(x)
    cipherKey = key[pos]
    j = Defines.alphabet.find(cipherKey)
    ans += Defines.CaesaTable[i][j]
    if pos == len(key) - 1:
        pos = 0
    else:
        pos += 1

print "\nAns:", ans

