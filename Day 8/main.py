test = open('test.txt', 'r')

arr = []
for group in test:
    arr.append(group.split())
    
# Correct Answers:
    # - Part 1: 268
    # - Part 2: 7867



# ======= Part 1 =======
visited = []
acc = 0
index = 0
while index not in visited:
    visited.append(index)
    x, y = arr[index]
    index += 1
    if x == 'nop':
        continue
    
    if x == 'jmp':
        index += int(y) - 1
        continue

    acc += int(y)

print(acc)