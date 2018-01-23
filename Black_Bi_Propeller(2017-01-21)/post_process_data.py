import numpy as np

filename = ['Black_Bi_Propeller_Test_2018-01-21_155121.csv']

index = [1, 8, 9, 10, 11, 12]
data = []
    
for fileId in range(len(filename)):
    fp = open(filename[fileId])

    raw_data = fp.readlines()
    fp.close()
    base_data = []
    for line in range(len(raw_data)):
        if (line == 0):
            continue
        raw_line_data = raw_data[line].split(',')
        line_data = []
        for i in range(len(index)):
            if (index[i] != 8 and index[i] != 9):
                line_data.append((float)(raw_line_data[index[i]]))
            elif (index[i] == 8):
                line_data.append(-(float)(raw_line_data[index[i]]))
            elif (index[i] == 9):
                line_data.append((float)(raw_line_data[index[i]]))
        if (line_data[0] < 1105):
            base_data = line_data;
        else:
            line_data[1] -= base_data[1]
            line_data[2] -= base_data[2]
            data.append(line_data)

fp = open('Black_Bi_Propeller_Test.txt', 'w')
for line in data:
    for entry in line:
        fp.write(str(entry) + ' ')
    fp.write('\n')
fp.close()