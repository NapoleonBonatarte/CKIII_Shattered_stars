import random

file_path = ''

file = open(file_path, 'r')
data = file.readlines()
to_write = open('end_file', 'w')
for i in data:
    line = i
    # creates colors for baronies
    if line.strip() == 'color = { 0 1 0 }':
        print('hello')
        output1 = random.randint(0,255)
        output2 = random.randint(0,255)
        output3 = random.randint(0,255)
        output = '\t\t\t\t\tcolor = { ' + str(output1) +' ' + str(output2) + ' ' + str(output3) + ' }\n'
        print(output)
        to_write.write(output)
    # creates color for counties
    elif line.strip() == 'color = { 1 0 0 }':
        output1 = random.randint(0,255)
        output2 = random.randint(0,255)
        output3 = random.randint(0,255)
        output = '\t\t\t\tcolor = { ' + str(output1) +' ' + str(output2) + ' ' + str(output3) + ' }\n'
        print(output)
        to_write.write(output)
    else:
        to_write.write(line)



file.close()
to_write.close()