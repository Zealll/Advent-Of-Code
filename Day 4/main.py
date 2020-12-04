import math
paths = open('test.txt', 'r')

arr = []
for each in paths:
    arr.append(each.split())



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