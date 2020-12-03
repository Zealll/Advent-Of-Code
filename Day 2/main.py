passwords = open('passwords.txt', 'r')

arr = []
for each in passwords:
    arr.append(each.split())

# ===== Part 1 Starts Here =====
# ***How many passwords are valid according to their policies?
    # EX: 
    #     1) 1-3 a: abcde
    #        - "a" must repeat at least once, but no more than 3 times
    #     2) 1-3 b: cdefg
    #        - "b" must repeat at least once, but no more than 3 times
    #     3) 2-9 c: ccccccccc
    #        - "c" must repeat at least twice, but no more than 9 times

validPass = 0
for i in arr:
    letter = 0
    for j in i[2]:
        if j == i[1][0]:
            letter += 1
    x, y = i[0].split('-')
    if letter >= int(x) and letter <= int(y):
        validPass += 1

print(validPass)
# ===== Part 1 Ends Here =====

# ===== Part 2 Starts Here =====
# Each policy actually describes two positions in the password, where 1 means the first character, 
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept 
# of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences 
# of the letter are irrelevant for the purposes of policy enforcement.

newValidPass = 0
for i in arr:
    x, y = i[0].split('-')
    xMatch = False
    yMatch = False

    if i[2][int(x) - 1] == i[1][0]:
        xMatch = True
    
    if i[2][int(y) - 1] == i[1][0]:
        yMatch = True
    
    result = xMatch != yMatch
    if result:
        newValidPass += 1

print(newValidPass)
# ===== Part 2 Ends Here =====