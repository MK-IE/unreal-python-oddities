from pprint import pprint
text = input('Please input your text to be bar charred ')

dict_bar = {}
for letter in text:
    if letter not in dict_bar:
        dict_bar[letter] = [letter]
    else:
        dict_bar[letter].append(letter)

pprint(dict_bar)
