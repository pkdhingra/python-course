import sys
from score_word import cal_score as cal

#Read file sowpods
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
print(data[0:6])

if len(sys.argv) < 2:
    raise Exception("Please provide a valid rack")

rack = sys.argv[1]

valid_words = []
for word in data:
    #set the word as the right candidate!!
    is_scrabble = True
    rack_letters = list(rack)
    for char in word:
        if char not in rack_letters:
            is_scrabble = False
            break #Skip this word and move on
        else:
            rack_letters.remove(letter)
    if is_scrabble == True: #if it's the word we're looking for
        cal(rack)
        valid_words.append([score, word])
