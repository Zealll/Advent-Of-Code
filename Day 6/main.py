test = open('test.txt', 'r')

arr = []
for each in test:
    arr.append(each.split())

filteredAnswers = [[]]
for i in arr:
    if len(i) == 0:
        filteredAnswers.append(i)
    else:
        filteredAnswers[len(filteredAnswers) - 1] += i

# ======= Part 2 =======
total = 0
for i in filteredAnswers:
    # print(i)
    if len(i) == 1:
        count = 0
        letters = ''
        for letter in range(len(i[0])):
            if i[0][letter] not in letters:
                count += 1
        total += count
    else:
        exampleString = [i[0]]
        for group in range(1, len(i)):
            exampleString.append([])
            for letter in i[group]:
                if letter in exampleString[len(exampleString) - 2] and letter not in exampleString[len(exampleString) - 1]:
                        exampleString[len(exampleString) - 1].append(letter)

        total += len(exampleString[len(exampleString) - 1])

print(total)


# ======= Part 1 =======
# total = 0
# for i in filteredAnswers:
#     fullString = ''.join(i)
#     answered = []
#     for letter in fullString:
#         if letter not in answered:
#             answered.append(letter)
#     total += len(answered)

# print(total)
