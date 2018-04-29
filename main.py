# -*- coding: UTF-8 -*-

print("Please input your encryption key")
key = raw_input('Key: ').lower()

print("Please input your encryption text")
text = raw_input('Text: ').lower()

pos = 0
ans = ""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
str_list = alphabet + alphabet

for x in text:
    # if x is blank, then just simply skip
    if x == " ":
        ans += " "
        continue

    # calculate encrypt result
    i = alphabet.find(x)
    cipherKey = key[pos]
    j = alphabet.find(cipherKey)
    ans += str_list[i + j]

    # update cipher key index
    if pos == len(key) - 1:
        pos = 0
    else:
        pos += 1

print "\nAns:", ans.upper()
