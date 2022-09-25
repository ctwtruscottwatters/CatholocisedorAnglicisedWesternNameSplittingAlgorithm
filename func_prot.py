# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott Watters, a few months out from my course at MIT, the Massachusetts Institute of Technology
Thank you MIT Staff
Just a quick string processing algorithm design between numerical principles of how to treat arbitrary length character data instead of using string object methods such as .split(), say in the OO class Person(object) example from the course
May be able to define the mathematical definition of an algorithm which simply takes the first space and anything up to the last space and split between the first name, last name and arbitrary length middle names, e.g. validation is not sound of any other than a four-word name whereas 2n + 1 and 3n + 1 length names and the null-byte character end split the arbitrary length - 1 spaces between the first name and last name, e.g. two spaces between middle names and one after the first name and one proceeding the last name
May be able to also define a recursive process to do so, a recursive function definition with base cases in a memoisation, instead of an iterative process
8:40 p.m. 25/09/2022 Byron Bay NSW 2481
"""
"""


runfile('C:/Users/Visual_Studio/Desktop/func_prot.py', wdir='C:/Users/Visual_Studio/Desktop')
There are 3 spaces in this string
So there is presumably a first name, a last name, and 2 middle names
First name:  First count: 7
The first space is at the 7th index
The first name is: Charles 
Second loop from 8 to 31
Mid count in loop: 1
Second loop from 8 to 31
Mid count in loop: 2
Second loop from 8 to 31
Mid count in loop: 3
Second loop from 8 to 31
Mid count in loop: 4
Second loop from 8 to 31
Mid count in loop: 5
Second loop from 8 to 31
Mid count in loop: 6
Second loop from 8 to 31
Mid count in loop: 7
Space found at mid count: 7
mid_count for string: 14
mid_count_two loop vals: start 14 stop 31
mid_count_two: 1
mid_count_two loop vals: start 14 stop 31
mid_count_two: 2
mid_count_two loop vals: start 14 stop 31
mid_count_two: 3
mid_count_two loop vals: start 14 stop 31
mid_count_two: 4
mid_count_two loop vals: start 14 stop 31
mid_count_two: 5
mid_count_two loop vals: start 14 stop 31
mid_count_two: 6
mid_count_two loop vals: start 14 stop 31
mid_count_two: 7
mid_count_two loop vals: start 14 stop 31
mid_count_two: 8
space found at mid_count_two: 8
The first middle name is at the 7th index and the second middle name is at the 14th index
Mid count two: 23
The first name is: Charles 
The first middle name is: Thomas
The second middle-name is:  Wallace 
The last name is: Truscott
There are 3 spaces in this string
So there is presumably a first name, a last name, and 2 middle names
First name:  First count: 3
The first space is at the 3th index
The first name is: Tai 
Second loop from 4 to 29
Mid count in loop: 1
Second loop from 4 to 29
Mid count in loop: 2
Second loop from 4 to 29
Mid count in loop: 3
Second loop from 4 to 29
Mid count in loop: 4
Second loop from 4 to 29
Mid count in loop: 5
Second loop from 4 to 29
Mid count in loop: 6
Second loop from 4 to 29
Mid count in loop: 7
Second loop from 4 to 29
Mid count in loop: 8
Space found at mid count: 8
mid_count for string: 11
mid_count_two loop vals: start 11 stop 29
mid_count_two: 1
mid_count_two loop vals: start 11 stop 29
mid_count_two: 2
mid_count_two loop vals: start 11 stop 29
mid_count_two: 3
mid_count_two loop vals: start 11 stop 29
mid_count_two: 4
mid_count_two loop vals: start 11 stop 29
mid_count_two: 5
mid_count_two loop vals: start 11 stop 29
mid_count_two: 6
mid_count_two loop vals: start 11 stop 29
mid_count_two: 7
mid_count_two loop vals: start 11 stop 29
mid_count_two: 8
mid_count_two loop vals: start 11 stop 29
mid_count_two: 9
space found at mid_count_two: 9
The first middle name is at the 3th index and the second middle name is at the 11th index
Mid count two: 21
The first name is: Tai 
The first middle name is: William
The second middle-name is:  Wedekind 
The last name is: Truscott
There are 3 spaces in this string
So there is presumably a first name, a last name, and 2 middle names
First name:  First count: 5
The first space is at the 5th index
The first name is: Needs 
Second loop from 6 to 22
Mid count in loop: 1
Second loop from 6 to 22
Mid count in loop: 2
Space found at mid count: 2
mid_count for string: 7
mid_count_two loop vals: start 7 stop 22
mid_count_two: 1
mid_count_two loop vals: start 7 stop 22
mid_count_two: 2
mid_count_two loop vals: start 7 stop 22
mid_count_two: 3
mid_count_two loop vals: start 7 stop 22
mid_count_two: 4
mid_count_two loop vals: start 7 stop 22
mid_count_two: 5
mid_count_two loop vals: start 7 stop 22
mid_count_two: 6
mid_count_two loop vals: start 7 stop 22
mid_count_two: 7
mid_count_two loop vals: start 7 stop 22
mid_count_two: 8
mid_count_two loop vals: start 7 stop 22
mid_count_two: 9
mid_count_two loop vals: start 7 stop 22
mid_count_two: 10
space found at mid_count_two: 10
The first middle name is at the 5th index and the second middle name is at the 7th index
Mid count two: 18
The first name is: Needs 
The first middle name is: a
The second middle-name is:  four-word 
The last name is: name

I love you Tai and Dad, Mark William Watters
Thank you Tai Truscott and Mark Watters, big bro and dad

"""
def return_name_mid(name):
    if type(name) != str:
        print("Please input a string")
    else:
        amount_of_spaces_for_next_alg_impl = 0
        for spaces_found in name:
            if spaces_found == " ":
                amount_of_spaces_for_next_alg_impl += 1
        print("There are {} spaces in this string".format(amount_of_spaces_for_next_alg_impl))
        print("So there is presumably a first name, a last name, and {} middle names".format(amount_of_spaces_for_next_alg_impl - 1))
        first_count = 0
        mid_count, mid_count_two = 0, 0
        last_count = 0
        first_name = ""
        middle_name_one = ""
        middle_name_two = ""
        last_name = ""
        for char in name:
            first_count += 1
            if char == " ":
                break
        first_count -= 1
        print("First name: {} First count: {}".format(first_name, first_count))
        for count in range(first_count + 1):
            first_name += name[count]
        print("The first space is at the {}th index".format(first_count))
        print("The first name is: {}".format(first_name))
        for x in range(first_count + 1, len(name), 1):
            print("Second loop from {} to {}".format(first_count + 1, len(name)))
            mid_count += 1
            print("Mid count in loop: {}".format(mid_count))
            if name[x] == " ":
                print("Space found at mid count: {}".format(mid_count))
                break
        mid_count = mid_count + first_count
        print("mid_count for string: {}".format(mid_count))
        for y in range(mid_count + 1, len(name), 1):
            print("mid_count_two loop vals: start {} stop {}".format(mid_count, len(name)))
            mid_count_two += 1
            print("mid_count_two: {}".format(mid_count_two))
            if name[y] == " ":
                print("space found at mid_count_two: {}".format(mid_count_two))
                break
        mid_count_two += 1 + mid_count
        print("The first middle name is at the {}th index and the second middle name is at the {}th index".format(first_count, mid_count))
        for x in range(first_count + 1, mid_count, 1):
            middle_name_one += name[x]
        for x in range(mid_count, mid_count_two, 1):
            middle_name_two += name[x]
        for x in range(mid_count_two, len(name), 1):
            last_name += name[x]
        print("Mid count two: {}".format(mid_count_two))
        print("The first name is: {}".format(first_name))
        print("The first middle name is: {}".format(middle_name_one))
        print("The second middle-name is: {}".format(middle_name_two))
        print("The last name is: {}".format(last_name))
        
                
def main():
    Charles = "Charles Thomas Wallace Truscott"
    Tai = "Tai William Wedekind Truscott"
    Mark = "Needs a four-word name"
    return_name_mid(Charles)
    return_name_mid(Tai)
    return_name_mid(Mark)

if __name__ == "__main__": main()