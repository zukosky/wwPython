
#No exception handling
#for nIndex in range(0,6):
    #print(nIndex-5)
#    div = 5 / (nIndex-5)

import sys
import time
import random
for nIndex in range(0,6):
    print(nIndex-3)
    try:
        #Will throw and exception on nIndex=3
        div = 5 / (nIndex-3)
    except:
        #Exception caught.  Loop will continue.
        e = sys.exc_info()[0]
        print("Error: %s" % e)
#while True:
#	print("Printing forever")
#Note, in order to continue out of an exception, the while needs to be outside of the try block
while True:
	try:
		print("printing forever")
		time.sleep(1)
		ranNum = random.randint(1,11)
		print ("Random Number: %s" % ranNum)
		div = 5 / (5-ranNum)
#		continue  this is not necessary
	except KeyboardInterrupt:
		print("Keyboard interrupt exception caught")
		e = sys.exc_info()[0]
		print("Error: %s" % e)
		sys.exit()
	except ZeroDivisionError:
		print("Zero Division error")
		e = sys.exc_info()[0]
		print("Error: %s" % e)
#		sys.exit() WIthout sys.exit() will run forever.
	except:
		print("general exception caught")
		e = sys.exc_info()[0]
		print("Error: %s" % e)
		sys.exit()
