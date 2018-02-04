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
alien={'color':'green','point':5}
print("the alien's color is" +alien['color'])
fav_numbers={'eric':17,'ever':4}
for name in fav_numbers.keys():
    print(name+'loves a number')
for number in fav_numbers.values():
    print(str(number)+'is a favorite')
for number in fav_numbers.keys():
    print(str(number)+'is a favorite')
