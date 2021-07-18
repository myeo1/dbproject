file = open('climate.csv', 'r')
climate = file.readlines()
# print(climate)
#
# newList = []
# for line in climate:
#    newList.append(line[:-1])
# #all the lines will be used, except the last one (-1)
# print(newList)
#
# newList = []
# for line in climate:
#    if line[-1] == '\n':
#        newList.append(line[:-1])
# print(newList)
#
# newList = []
# for line in climate:
#    if line[-1] == '\n':
#        newList.append(line[:-1])
#    else:
#        newList.append(line)
# print(newList)
#
# newList = []
# for line in climate:
#    newList.append(line.strip())
# print(newList)

filename = input('file to save: ')
with open(filename + '.txt', 'w') as file:
   file.write(input('insert file text:'))
counter_dict = {}
with open(filename + ".txt") as f:
   line = f.readline()
   while line:
       line = line.strip()
       if line in counter_dict:
           counter_dict[line] +=1
       else:
           counter_dict[line] =1
       line = f.readline()
print(counter_dict)
