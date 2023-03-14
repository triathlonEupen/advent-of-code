score = 0
for line in open('input02.txt'):
    current = line.strip()
    if current == "A X": score += 0+3
    elif current == "A Y": score += 3+1
    elif current == "A Z": score += 6+2
    if current == "B X": score += 0+1
    elif current == "B Y": score += 3+2
    elif current == "B Z": score += 6+3
    if current == "C X": score += 0+2
    elif current == "C Y": score += 3+3
    elif current == "C Z": score += 6+1
print(score)