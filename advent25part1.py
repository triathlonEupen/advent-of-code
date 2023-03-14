total = 0
for line in open('input25.txt').read().splitlines():
    snafu = line[::-1] # reverse order
    for i, elem in enumerate(snafu):
        if elem == "-":
            total -= pow(5, i)
        elif elem == "=":
            total -= 2*pow(5, i)
        else:
            total += int(elem)*pow(5, i)

answer = ""
while total>0:
    rem = total % 5
    total = total // 5
    if rem < 3:
        answer = str(rem) + answer
    else:
        total +=1
        if rem == 3: answer = "=" + answer
        else: answer = "-" + answer
print(answer)