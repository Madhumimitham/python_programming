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
square=[]
for x in range(1,11):
    square.append(x**2)
    print (square)
    square=[x**2 for x in range (1,11)]
    print "square=",square
