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
        total += len(i[0])
        print(i[0])
    else:
        exampleString = [i[0]]
        for group in range(1, len(i)):
            exampleString.append([])
            for letter in i[group]:
                if letter in exampleString[len(exampleString) - 2]:
                    if letter not in exampleString[len(exampleString) - 1]:
                        exampleString[len(exampleString) - 1].append(letter)
        # print(exampleString[len(exampleString) - 1])
        total += len(exampleString[len(exampleString) - 1])
    


    # total += len(answered)

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
