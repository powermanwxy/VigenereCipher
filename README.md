# VigenereCipher
A Vigenere Cipher Encrypter implement by python.

## Introduction
The Vigenère cipher is a method of encrypting
alphabetic text by usinga series of interwoven
Caesar ciphers based on theletters of a keyword.
It is a form of polyalphabetic substitution.

Though the cipher is easy to understand and implement,
for three centuries it resisted all attempts to break
it; this earned it the description le chiffre
indéchiffrable (French for 'the indecipherable cipher').
Many people have tried to implement encryption schemes
that are essentially Vigenère ciphers.

## Description (From WikiPedia)
In a Caesar cipher, each letter of the alphabet is
shifted along some number of places; for example,
in a Caesar cipher of shift 3, A would become D, B
would become E, Y would become B and so on.
The Vigenère cipher consists of several Caesar ciphers
in sequence with different shift values.

To encrypt, a table of alphabets can be used,
termed a tabula recta, Vigenère square, or Vigenère
table. It consists of the alphabet written out 26
times in different rows, each alphabet shifted
cyclically to the left compared to the previous
alphabet, corresponding to the 26 possible Caesar
ciphers. At different points in the encryption process,
the cipher uses a different alphabet from one of
the rows. The alphabet used at each point depends
on a repeating keyword.

For example, suppose that the plaintext to be
encrypted is:

    ATTACKATDAWN
The person sending the message chooses a keyword
and repeats it until it matches the length of the
plaintext, for example, the keyword "LEMON":

    LEMONLEMONLE
Each row starts with a key letter. The remainder
of the row holds the letters A to Z (in shifted order).
Although there are 26 key rows shown, one will only
use as many keys (different alphabets) as there are
unique letters in the key string, here just 5 keys,
{L, E, M, O, N}. For successive letters of the message,
we are going to take successive letters of the key
string, and encipher each message letter using its
corresponding key row. Choose the next letter of the
key, go along that row to find the column heading that
matches the message character; the letter at the
intersection of key-row, msg-col is the enciphered letter.

For example, the first letter of the plaintext,
A, is paired with L, the first letter of the key.
So use row L and column A of the Vigenère square,
namely L. Similarly, for the second letter of the
plaintext, the second letter of the key is used;
the letter at row E and column T is X. The rest of
the plaintext is enciphered in a similar fashion:

    Plaintext:	ATTACKATDAWN
    Key:	LEMONLEMONLE
    Ciphertext:	LXFOPVEFRNHR

Decryption is performed by going to the row in the
table corresponding to the key, finding the position
of the ciphertext letter in this row, and then using
the column's label as the plaintext. For example, in
row L (from LEMON), the ciphertext L appears in column
A, which is the first plaintext letter. Next we go
to row E (from LEMON), locate the ciphertext X which
is found in column T, thus T is the second plaintext
letter.

## Demo:
    Please input your encryption key
    Key: APPLE

    Please input your encryption text
    Text: BIG BROTHER IS WATCH YOU

    Ans: BXV MVOIWPV IH LLXCWXYK YDJ

Blog: http://www.cnblogs.com/scobbing/p/8663132.html