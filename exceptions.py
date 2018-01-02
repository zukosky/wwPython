#No exception handling
#for nIndex in range(0,6):
    #print(nIndex-5)
#    div = 5 / (nIndex-5)

import sys
for nIndex in range(0,6):
    print(nIndex-3)
    try:
        #Will throw and exception on nIndex=3
        div = 5 / (nIndex-3)
    except:
        #Exception caught.  Loop will continue.
        e = sys.exc_info()[0]
        print("Error: %s" % e)
