#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
age=int(input("enter the age:"))
if age >=18:
    print("you can vote")
elif age<18:
    print("ticket price=10")
else:
    print("ticket price=15")
