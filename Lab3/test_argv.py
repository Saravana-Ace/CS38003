# import sys
# for arg in sys.argv:
#     print (arg)
#
# print(sys.argv)


def printArgs(first, *arg):
    print ("first argument =", first)
    for ar in arg:
        print (ar)

printArgs(10,1,2,3,4,5)
