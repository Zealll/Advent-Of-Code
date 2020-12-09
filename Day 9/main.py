test = open('test.txt', 'r')

arr = []
for group in test:
    arr.append(int(group.split()[0]))
    
# Correct Answers:
    # - Part 1: 10884537
    # - Part 2: 1261309

# ======= Part 1 =======
def part1():
    for i in range(25, len(arr)):
        sum = False
        for j in range(i - 25, i):
            if arr[i] - arr[j] in arr[i - 25 : i] and arr[i] - arr[j] != arr[j]:
                sum = True
                break
        
        if not sum: 
            return arr[i]


# ======= Part 2 =======
index = arr.index(part1())
for i in range(len(arr[ : index])):
    total = 0
    lastNum = 0
    for j in arr[i : index]:
        if total == arr[index]:
            break

        total += j
        lastNum = arr.index(j)
    
    if total == arr[index]:
        sortedNums = sorted(arr[i : lastNum + 1])
        print('Part 1:', part1())
        print('Part 2:', sortedNums[0] + sortedNums[len(sortedNums) - 1])
        break