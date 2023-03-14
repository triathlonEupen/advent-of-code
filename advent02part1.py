score = 0
for line in open('input02.txt'):
    current = line.strip()
    if current == "A X": score += 4
    elif current == "A Y": score += 8
    elif current == "A Z": score += 3
    if current == "B X": score += 1
    elif current == "B Y": score += 5
    elif current == "B Z": score += 9
    if current == "C X": score += 7
    elif current == "C Y": score += 2
    elif current == "C Z": score += 6
print(score)