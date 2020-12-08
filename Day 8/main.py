test = open('test.txt', 'r')

arr = []
for group in test:
    arr.append(group.split())
    
# Correct Answers:
    # - Part 1: 268
    # - Part 2: 7867


# ======= Part 2 =======
def checker(array):
    visited = []
    acc = 0
    index = 0
    while index not in visited and index < len(array):
        visited.append(index)
        x, y = array[index]
        index += 1

        if x == 'nop':
            continue
        
        if x == 'jmp':
            index += int(y) - 1
            continue

        acc += int(y)
    return index == len(array), acc


for i in range(len(arr)):
    x, y = arr[i]
    
    if x == 'acc':
        continue

    swapBetween = ['jmp', 'nop']
    k, l = swapBetween.index(x), abs(swapBetween.index(x) - 1)

    arr[i][0] = swapBetween[l]

    finished, total = checker(arr)

    arr[i][0] = swapBetween[k]

    if finished:
        print(total)
        break




# ======= Part 1 =======
# while index not in visited:
#     visited.append(index)
#     x, y = arr[index]
#     index += 1
#     if x == 'nop':
#         continue
    
#     if x == 'jmp':
#         index += int(y) - 1
#         continue

#     acc += int(y)

# print(index)
# print(acc)