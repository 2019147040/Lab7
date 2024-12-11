file = open("input_7_2.txt", "r")
text = file.read()

char_count = {}

for char in text:
    if char.isalpha():
        char_upper = char.upper()
        char_count[char_upper] = char_count.get(char_upper, 0) + 1

char_items = list(char_count.items())
char_items.sort(key=lambda item: item[1], reverse=True)
sorted_chars = char_items

sorted_letters = [item[0] for item in sorted_chars]

print(sorted_letters)

file.close()