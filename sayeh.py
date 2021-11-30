#!/usr/bin/env python3
#
# {Program}
# Sayeh
# Sayeh creates passwords using special words
# Sayeh is a Persian word & Means shadow
#
# version 1.1
#
#
# {Author}
# Mehrshad Mollaafzal
#    Email add: mehrshad.afzal.1379@gmail.com
#    Linkedin add: linkedin.com/in/mehrshad-mollaafza


import os
from itertools import product

inp_list = []
Use_char = []

###### list for GPU bortforce ######
All_char_G_large = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '|', ']', '[', '}', '{',
             ';', ':', '"', "'", '/', '.', ',', '?', '>', '<']  # 31

Char_for_G_medium = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', ']', '[',
                   ';', "'", '/', '.', ',', '?', ':', '<', '>']   # 26

Char_for_G_small = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', '?', '.']   # 16

###### list for online bortforce ######
Char_for_O_Large = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', ']', '[',
                    ';', '/', '.', ',', '?', ':', '<', '>']   # 25

Char_for_O_medium = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '=', '+', '_', '.', ',', '?']  # 15

Char_for_O_small = ['!', '@', '#', '$', '&', '*', '-', '=', '_', '+', '?', '.']   # 12


####################################################################################################
####################################################################################################
print('\n\n++++ version 1.1 ++++')


print('\n\n[*] g/G == Use the GPU for bruteforce. The number of passwords in the list increases\n'
      '     Like NTLM,SHA,WPA,...\n\n'      
      '[*] o/O == Bortforce online\n'
      '     Like SSH,SMB,...\n')
while True:
    GPU_str = input('------> Enter [O/G]?').lower()
    if GPU_str in ['g', 'o']:
        break


print('\n\n\n[*]Size of password list\n'
      '     1=Small       2=Medium       3=Large\n')
while True:
    size_str = input('------> Enter [1/2/3]?')
    if size_str in ['1', '2', '3']:
        break


print('\n\n\n[*]Outpute File\n')
Filename = input('------> File name [default : sayeh_pass_list.txt]')

if Filename:
    file1 = open(Filename, 'w')
else:
    Filename = 'sayeh_pass_list.txt'
    file1 = open(Filename, 'w')


def Creat_list_from_inputs():
    print('\n\n\n[*]Enter your word:')
    while True:
        inp_str = str(input('Empty input ---> start to create password list => ')).lower()
        if inp_str == '':
            print('##### Please wait a few seconds #####')
            # print(inp_list)
            break
        elif inp_str in inp_list:
            print('Your input is a duplicate')
        elif ' ' in inp_str:
            print('Password should not have a space')
        else:
            inp_list.append(inp_str)  # Create list from inputs


Creat_list_from_inputs()
####################################################################################################
####################################################################################################

#print(len(Use_char))

len_inp_list = len(inp_list)
# print(len_inp_list)


# Input permutation
def G_3():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                file1.write(inp_permutation + i + i + '\n')
                file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1330, end_year=1403, inp_permutation=inp_permutation, size=3)   # Solar
            year(start_year=1950, end_year=2024, inp_permutation=inp_permutation, size=3)   # Georgian
            year(start_year=1390, end_year=1445, inp_permutation=inp_permutation, size=3)   # Lunar
            One_num(size=3, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Ziro_num_arrangement(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_ziro_num_arrangment(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            Five_same_num(inp_permutation=inp_permutation)
            Six_same_num(inp_permutation=inp_permutation)
            Seven_same_num(inp_permutation=inp_permutation)
            Eight_same_num(inp_permutation=inp_permutation)
            Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=0, inp_permutation=inp_permutation)


def G_2():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                file1.write(inp_permutation + i + i + '\n')
                file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1350, end_year=1403, inp_permutation=inp_permutation, size=2)   # Solar
            year(start_year=1970, end_year=2024, inp_permutation=inp_permutation, size=2)   # Georgian
            year(start_year=1400, end_year=1445, inp_permutation=inp_permutation, size=2)   # Lunar
            One_num(size=2, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement_end_ziro(start_num=1, end_num=6, inp_permutation=inp_permutation)
            Ziro_num_arrangement(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_ziro_num_arrangment(start_num=1, end_num=6, inp_permutation=inp_permutation)
            Num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            Five_same_num(inp_permutation=inp_permutation)
            Six_same_num(inp_permutation=inp_permutation)
            Seven_same_num(inp_permutation=inp_permutation)
            # Eight_same_num(inp_permutation=inp_permutation)
            # Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=0, inp_permutation=inp_permutation)


def G_1():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                file1.write(inp_permutation + i + i + '\n')
                file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1360, end_year=1403, inp_permutation=inp_permutation, size=1)   # Solar
            year(start_year=1980, end_year=2024, inp_permutation=inp_permutation, size=1)   # Georgian
            year(start_year=1410, end_year=1445, inp_permutation=inp_permutation, size=1)   # Lunar
            One_num(size=1, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            # Reverse_num_arrangement_end_ziro()
            Ziro_num_arrangement(start_num=1, end_num=10, inp_permutation=inp_permutation)
            # Reverse_ziro_num_arrangment()
            Num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement(start_num=2, end_num=6, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            Five_same_num(inp_permutation=inp_permutation)
            Six_same_num(inp_permutation=inp_permutation)
            # Seven_same_num(inp_permutation=inp_permutation)
            # Eight_same_num(inp_permutation=inp_permutation)
            # Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=0, inp_permutation=inp_permutation)


def O_3():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                file1.write(inp_permutation + i + i + '\n')
                file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1350, end_year=1403, inp_permutation=inp_permutation, size=3)   # Solar
            year(start_year=1970, end_year=2024, inp_permutation=inp_permutation, size=3)   # Georgian
            # Lunar_year(start_year=1390, end_year=1445, inp_permutation=inp_permutation, size=3)
            One_num(size=3, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement_end_ziro(start_num=1, end_num=6, inp_permutation=inp_permutation)
            Ziro_num_arrangement(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Reverse_ziro_num_arrangment(start_num=1, end_num=6, inp_permutation=inp_permutation)
            Num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Reverse_num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            Five_same_num(inp_permutation=inp_permutation)
            Six_same_num(inp_permutation=inp_permutation)
            # Seven_same_num(inp_permutation=inp_permutation)
            # Eight_same_num(inp_permutation=inp_permutation)
            # Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            # Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=0, inp_permutation=inp_permutation)


def O_2():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                file1.write(inp_permutation + i + i + '\n')
                # file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1360, end_year=1403, inp_permutation=inp_permutation, size=2)   # Solar
            year(start_year=1980, end_year=2024, inp_permutation=inp_permutation, size=2)   # Georgian
            # Lunar_year(start_year=1400, end_year=1445, inp_permutation=inp_permutation, size=2)
            One_num(size=2, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            # Reverse_num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Ziro_num_arrangement(start_num=1, end_num=10, inp_permutation=inp_permutation)
            # Reverse_ziro_num_arrangment(start_num=1, end_num=6, inp_permutation=inp_permutation)
            Num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            # Reverse_num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            Five_same_num(inp_permutation=inp_permutation)
            # Six_same_num(inp_permutation=inp_permutation)
            # Seven_same_num(inp_permutation=inp_permutation)
            # Eight_same_num(inp_permutation=inp_permutation)
            # Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            # Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=-9, inp_permutation=inp_permutation)


def O_1():
    for elem_list in range(len_inp_list):
        index_list = inp_list[elem_list]
        cases = zip(*[index_list, index_list.swapcase()])
        for permutation in product(*cases):
            inp_permutation = ("".join(permutation))

            file1.write(inp_permutation + inp_permutation+'\n')

            for i in Use_char:
                file1.write(inp_permutation + i + '\n')
                file1.write(i + inp_permutation + '\n')
                # file1.write(inp_permutation + i + i + '\n')
                # file1.write(i + i + inp_permutation + '\n')
                file1.write(i + inp_permutation + i + '\n')
            year(start_year=1370, end_year=1403, inp_permutation=inp_permutation, size=1)   # Solar
            year(start_year=1990, end_year=2024, inp_permutation=inp_permutation, size=1)   # Georgian
            # Lunar_year(start_year=1410, end_year=1445, inp_permutation=inp_permutation, size=1)
            One_num(size=1, inp_permutation=inp_permutation)
            Num_arrangement_end_ziro(start_num=1, end_num=5, inp_permutation=inp_permutation)
            # Reverse_num_arrangement_end_ziro(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Ziro_num_arrangement(start_num=1, end_num=6, inp_permutation=inp_permutation)
            # Reverse_ziro_num_arrangment(start_num=1, end_num=10, inp_permutation=inp_permutation)
            Num_arrangement(start_num=2, end_num=6, inp_permutation=inp_permutation)
            # Reverse_num_arrangement(start_num=2, end_num=10, inp_permutation=inp_permutation)
            Two_same_num(inp_permutation=inp_permutation)
            Three_same_num(inp_permutation=inp_permutation)
            Four_same_num(inp_permutation=inp_permutation)
            # Five_same_num(inp_permutation=inp_permutation)
            # Six_same_num(inp_permutation=inp_permutation)
            # Seven_same_num(inp_permutation=inp_permutation)
            # Eight_same_num(inp_permutation=inp_permutation)
            # Nine_same_num(inp_permutation=inp_permutation)
            Ziro_one_num(inp_permutation=inp_permutation)
            Num_big_to_small(inp_permutation=inp_permutation)
            # Num_big_to_small_with_ziro(inp_permutation=inp_permutation)
            Ziro_num_big_to_small(start_num=-10, end_num=-9, inp_permutation=inp_permutation)


# Add year to input
def year(start_year, end_year, inp_permutation, size):
    for Georgian in range(start_year, end_year):
        for i in Use_char:
            if size == 3:
                file1.write(inp_permutation + i + str(Georgian) + '\n')
                file1.write(i + inp_permutation + str(Georgian) + '\n')
                file1.write(i + str(Georgian) + inp_permutation + '\n')
                file1.write(inp_permutation + str(Georgian) + i + '\n')
                file1.write(str(Georgian) + i + inp_permutation + '\n')
                file1.write(str(Georgian) + inp_permutation + i + '\n')
            elif size == 2:
                file1.write(inp_permutation + i + str(Georgian) + '\n')
                file1.write(inp_permutation + str(Georgian) + i + '\n')
                file1.write(i + inp_permutation + str(Georgian) + '\n')
                file1.write(str(Georgian) + i + inp_permutation + '\n')
            elif size == 1:
                file1.write(inp_permutation + str(Georgian) + i + '\n')
                file1.write(inp_permutation + i + str(Georgian) + '\n')


def One_num(size, inp_permutation):
    for a_num in range(10):
        for i in Use_char:
            if size == 3:                                               # 0
                file1.write(inp_permutation + i + str(a_num) + '\n')    # 1
                file1.write(i + inp_permutation + str(a_num) + '\n')    # 2
                file1.write(i + str(a_num) + inp_permutation + '\n')    # 3
                file1.write(inp_permutation + str(a_num) + i + '\n')    # .
                file1.write(str(a_num) + i + inp_permutation + '\n')    # 9
                file1.write(str(a_num) + inp_permutation + i + '\n')
            elif size == 2:
                file1.write(inp_permutation + i + str(a_num) + '\n')
                file1.write(inp_permutation + str(a_num) + i + '\n')
                file1.write(i + inp_permutation + str(a_num) + '\n')
                file1.write(str(a_num) + i + inp_permutation + '\n')
            elif size == 1:
                file1.write(inp_permutation + i + str(a_num) + '\n')
                file1.write(inp_permutation + str(a_num) + i + '\n')


def Num_arrangement_end_ziro(start_num, end_num, inp_permutation):
    for num_arr in range(start_num, end_num):                   # 10
        for i in Use_char:                                      # 120
            file1.write(inp_permutation + i)                    # 1230
            for j in range(1, num_arr + 1):                     # .....
                file1.write(str(j))                             # 1234567890
            file1.write('0\n')


def Reverse_num_arrangement_end_ziro(start_num, end_num, inp_permutation):
    for re_num_arr in range(start_num, end_num):
        for i in Use_char:
            for j in range(1, re_num_arr + 1):
                file1.write(str(j))
            file1.write('0' + i + inp_permutation + '\n')


def Ziro_num_arrangement(start_num, end_num, inp_permutation):
    for ziro_num_arr in range(start_num, end_num):                  # 01
        for i in Use_char:                                          # 012
            file1.write(inp_permutation + i)                        # 0123
            file1.write('0')                                        # 01234
            for b in range(1, ziro_num_arr + 1):                    # ......
                file1.write(str(b))                                 # 0123456789
            file1.write('\n')


def Reverse_ziro_num_arrangment(start_num, end_num, inp_permutation):
    for re_ziro_num_arr in range(start_num, end_num):
        for i in Use_char:
            file1.write('0')
            for b in range(1, re_ziro_num_arr + 1):
                file1.write(str(b))
            file1.write(i + inp_permutation + '\n')


def Num_arrangement(start_num, end_num, inp_permutation):
    for a in range(start_num, end_num):                      # 1
        for i in Use_char:                      # 12
            file1.write(inp_permutation + i)    # 123
            for p in range(1, a + 1):           # 1234
                file1.write(str(p))             # .....
            file1.write('\n')                   # 123456789


def Reverse_num_arrangement(start_num, end_num, inp_permutation):
    for a in range(start_num, end_num):
        for i in Use_char:
            for p in range(1, a + 1):
                file1.write(str(p))
                file1.write(i + inp_permutation)
                file1.write('\n')


def Two_same_num(inp_permutation):                    # 00
    for a in range(10):                               # 11
        for i in Use_char:                            # 99
            file1.write(inp_permutation + i + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + inp_permutation + i + '\n')


def Three_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(inp_permutation + i + str(a) + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Four_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(inp_permutation + i + str(a) + str(a) + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Five_same_num(inp_permutation):               # 00000
    for a in range(10):                           # 11111
        for i in Use_char:                        # 99999
            file1.write(inp_permutation + i + str(a) + str(a) + str(a) + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Six_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(inp_permutation + i + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Seven_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(inp_permutation + i + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + '\n')
            file1.write(str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Eight_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(
                inp_permutation + i + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + '\n')
            file1.write(
                str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Nine_same_num(inp_permutation):
    for a in range(10):
        for i in Use_char:
            file1.write(
                inp_permutation + i + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(
                    a) + '\n')
            file1.write(str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + str(a) + i + inp_permutation + '\n')


def Ziro_one_num(inp_permutation):
    for a in range(2, 10):
        for i in Use_char:
            file1.write(inp_permutation + i + '0' + str(a) + '\n')
            file1.write('0' + str(a) + i + inp_permutation + '\n')


def Num_big_to_small(inp_permutation):
    for a in range(-10, 0):                       # 987654321
        for i in Use_char:                        # 87654321
            file1.write(inp_permutation + i)      # 7654321
            for h in range(a+1, 0):               # ......
                file1.write(str(h*-1))            # 1
            file1.write('\n')


def Num_big_to_small_with_ziro(inp_permutation):
    for a in range(-10, 1):                     # 9876543210
        for i in Use_char:                      # 876543210
            file1.write(inp_permutation+i)      # 76543210
            for h in range(a+1, 1):             # ......
                file1.write(str(h*-1))          # 10
            file1.write('\n')                   # 0


def Ziro_num_big_to_small(start_num, end_num, inp_permutation):
    for a in range(start_num, end_num):             # 0987654321
        for i in Use_char:                          # 087654321
            file1.write(inp_permutation + i + '0')  # 07654321
            for h in range(a+1, 0):                 # ......
                file1.write(str(h*-1))              # 01
            file1.write('\n')


if GPU_str == 'g':
    if size_str == '3':
        for k in All_char_G_large:
            Use_char.append(k)
        G_3()
    elif size_str == '2':
        for k in Char_for_G_medium:
            Use_char.append(k)
        G_2()
    elif size_str == '1':
        for k in Char_for_G_small:
            Use_char.append(k)
        G_1()

elif GPU_str == 'o':
    if size_str == '3':
        for k in Char_for_O_Large:
            Use_char.append(k)
        O_3()
    elif size_str == '2':
        for k in Char_for_O_medium:
            Use_char.append(k)
        O_2()
    elif size_str == '1':
        for k in Char_for_O_small:
            Use_char.append(k)
        O_1()


# delete duplicate pass
uniqlines = set(open(Filename).readlines())
bar = open(Filename, 'w').writelines(set(uniqlines))

file1 = open(Filename, "r")
line_count = 0
for line in file1:
    if line != '\n':
        line_count += 1
print('\n\n  ',  line_count, 'Passwords')


file_size = os.stat(Filename)
file_size1 = file_size.st_size


if file_size1 >= 1024000:
    file_size2 = file_size1//1024000
    print("  The file size is close to :", file_size2, "MB")
else:
    file_size2 = file_size1//1000
    print("  The file size is close to :", file_size2, "KB")