text = input("string: ")

letters = 0
digits = 0

for i in range(len(text)):
    if 'a' <= text[i] <= 'z' or 'A' <= text[i] <= 'Z':
        letters += 1
    if '0' <= text[i] <= '9':
        digits += 1

print("letters:", letters)
print("digits:", digits)





text = input("string: ")
user_symbol = input("symbol: ")
count = 0

for i in range(len(text)):
    if text[i] == user_symbol:
        count += 1

print("count:", count)





text = input("string: ")
rev = ""

for i in range(len(text)-1, -1, -1):
    rev += text[i]

print("reversed:", rev)






text = input("string: ")
word = input("word: ")

words = text.split()
count = 0

for i in range(len(words)):
    if words[i] == word:
        count += 1

print("count:", count)






text = input("string: ")
old = input("replace: ")
new = input("new word: ")

words = text.split()
result = ""

for i in range(len(words)):
    if words[i] == old:
        result += new + " "
    else:
        result += words[i] + " "

print("result:", result)






text = input("string: ")
words = text.split()

longest = words[0]

for i in range(1, len(words)):
    if len(words[i]) > len(longest):
        longest = words[i]

print("longest word:", longest)
