passports = open('passports.txt', 'r')

arr = []
for passport in passports:
    arr.append(passport.split())

# Correct Answers:
    # - Part 1: 216
    # - Part 2: 150



filteredPass = [[]]
for i in arr:
    if len(i) == 0:
        filteredPass.append(i)
    else:
        # print('hello')
        filteredPass[len(filteredPass) - 1] += i

check = {
    "byr": True,
    "iyr": True,
    "eyr": True,
    "hgt": True,
    "hcl": True,
    "ecl": True,
    "pid": True
}

# ======= VERSION 2 =======


def main():
    count = 0
    for i in filteredPass:
        tempArr = []
        validFormat = True
        allFields = True
        for j in i:
            x, y = j.split(':')
            validFormat, field = validator(x, y)
            if validFormat:
                tempArr.append(field)
            else:
                continue

        if not validFormat:
            continue
        
        for k in check:
            if k not in tempArr:
                allFields = False
        
        if allFields:
            count += 1

    print(count)





def validator(x, y):
    key = None
    validFormat = True
    if x == 'byr':
        if int(y) < 1920 or int(y) > 2002:
            return [False, '']
    if x == 'iyr':
        if int(y) < 2010 or int(y) > 2020:
            return [False, '']
    if x == 'eyr':
        if int(y) < 2020 or int(y) > 2030:
            return [False, '']
    if x == 'hgt':
        if y[len(y) - 2:] == 'in':
            if int(y[:len(y) - 2]) < 59 or int(y[:len(y) - 2]) > 76:
                return [False, '']
        elif y[len(y) - 2:] == 'cm':
            if int(y[:len(y) - 2]) < 150 or int(y[:len(y) - 2]) > 193:
                return [False, '']
        else:
            return [False, '']
    if x == 'hcl':
        letterArr = ['#', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if y[0] != '#': 
            return [False, '']
        for letter in y:
            if letter not in letterArr:
                
                return [False, '']
    if x == 'ecl':
        colorArr = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if y not in colorArr:
            return [False, '']
    if x == 'pid':
        if len(y) != 9:
            return [False, '']
        for num in y:
            if not num.isdigit():
                return [False, '']
    key = x
    return [validFormat, key]
    


if __name__ == '__main__':
    main()






# ======= VERSION 1 =======
# # ======= Part 2 =======
# count = 0
# for i in filteredPass:
#     tempArr = []
#     allFields = True
#     validFormat = True
#     # print(i)
#     for j in i:
        
#         x, y = j.split(':')
#         if x == 'byr':
#             if int(y) < 1920 or int(y) > 2002:
#                 validFormat = False
#                 break
#         if x == 'iyr':
#             if int(y) < 2010 or int(y) > 2020:
#                 validFormat = False
#                 break
#         if x == 'eyr':
#             if int(y) < 2020 or int(y) > 2030:
#                 validFormat = False
#                 break
#         if x == 'hgt':
#             if y[len(y) - 2:] == 'in':
#                 if int(y[:len(y) - 2]) < 59 or int(y[:len(y) - 2]) > 76:
#                     validFormat = False
#                     break
#             elif y[len(y) - 2:] == 'cm':
#                 # print(y)
#                 if int(y[:len(y) - 2]) < 150 or int(y[:len(y) - 2]) > 193:
#                     validFormat = False
#                     break
#             else:
#                 validFormat = False

#         if x == 'hcl':
#             letterArr = ['#', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#             if y[0] != '#':
                
#                 validFormat = False
#                 break
#             for letter in y:
#                 print(letter)
#                 if letter not in letterArr:
                   
#                     validFormat = False
#                     break
#         if x == 'ecl':
#             colorArr = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#             if y not in colorArr:
#                 validFormat = False
#                 break
#         if x == 'pid':
#             if len(y) != 9:
#                 validFormat = False
#                 break
#             for num in y:
#                 if not num.isdigit():
#                     validFormat = False
#                     break


#         tempArr.append(x)
#     # print(validFormat)
#     if not validFormat:
#         continue
    
#     for k in check:
#         if k not in tempArr:
#             allFields = False
    
#     if allFields:
#         count += 1

# print(count)









# ======= Part 1 =======
# filteredPass = [[]]
# for i in arr:
#     if len(i) == 0:
#         filteredPass.append(i)
#     else:
#         # print('hello')
#         filteredPass[len(filteredPass) - 1] += i

# check = {
#     "ecl": True,
#     "byr": True,
#     "iyr": True,
#     "eyr": True,
#     "hgt": True,
#     "hcl": True,
#     "pid": True
# }

# count = 0
# for i in filteredPass:
#     tempArr = []
#     allFields = True
#     for j in i:
#         tempArr.append(j.split(':')[0])
    
#     for k in check:
#         if k not in tempArr:
#             allFields = False
    
#     if allFields:
#         count += 1

# print(count)