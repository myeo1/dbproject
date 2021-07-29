filename = input('file to save: ')

with open(filename + '.txt', 'w') as file:
   while True:
      text = input('insert file text:')
      if text == 'X' or text == 'x':
         break
      else:
          file.write(text+'\n')

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