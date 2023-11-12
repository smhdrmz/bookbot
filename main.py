
with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

file_contents = file_contents.lower()
char_dict = {}
for ch in file_contents:
    if ch not in char_dict:
        char_dict[ch] = 0
    char_dict[ch] += 1

char_list = list(char_dict.items())

char_list.sort(key=lambda char: char[1], reverse=True)
for char in char_list:
    if char[0].isalpha():
        print(f"The '{char[0]}' was found {char[1]} times")




    