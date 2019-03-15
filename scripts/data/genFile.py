# -*- coding: utf-8 -*-
import csv

reader = csv.reader(open("d_road.csv", "r+",encoding='UTF-8'))

table = [line for line in reader]

keys = table[0];
types = table[1];
# descs = table[2];


count = 0
line = ""
print(table[2])
for key  in keys:

    '''
    str_key = '"'+ key +'"'
    print("%s:self[%d]," % (str_key,count))
    count += 1
'''
    '''
    print("<" + key +">")
    str_type =""
    if types[count] == 'int':
        str_type = "INT32"
    elif types[count] == 'float':
        str_type = "FLOAT"
    elif types[count] == 'string':
        str_type = "STRING"
    else:
        print("error ------------------------->")

    print("\t"+'<Type>' + str_type + '</Type>')

    print('</' + key + ">")
    count += 1
    '''

    count += 1
    str_key = 'd["' + key + '"],'
    line += str_key
    if count %5 == 0:
        print(line)
        line = ""
    elif count > (len(keys) - len(keys)/5) and count == len(keys):
        print(line)







