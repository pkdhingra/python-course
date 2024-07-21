x = input("Enter letters: ")
score = 0

for char in x:
    score += scores[char]
print(score)
