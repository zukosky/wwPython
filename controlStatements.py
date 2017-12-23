#############################################################################################
################################   IF THEN ELSE   ################################################
#############################################################################################
val1 = 5
val2 = 7
oper = "Multiplication"
if oper == "Multiplication":
    outVal = val1 * val2
elif oper == "Division":
    outVal = val1 / val2
elif oper == "Subtraction":
    outVal = val1 - val2
else:
    outVal = val1 + val2

print("Operation: " + oper + ", Value: " + str(outVal))

# FOR  LOOP
# By numberic reange
for nIndex in range(0,15):
	print(nIndex)

# Breaking off in a loop
for nIndex in range(0,15):
	print(nIndex)
	if nIndex==7:
		break

#Using xrange instead of range in python2. It was renamed range.  Generates the numbers as needed instead of all at once
for nIndex in range(0,12):
	print(nIndex)

#Strings can also be iterable
strList = ['red','green','blue','yellow']
for thisColor in strList:
	print(thisColor)

#Iterating over lists of lists
strList = [['fucia','indigo','pink'],['blue','navy','saffiron']]
for  thisColor in  strList:
	for subColor in thisColor:
		print(subColor)


### WHILE LOOP

strList = ['red','green','blue','yellow']
print("Testing first while loop")
nIndex=0
thisColor = strList[nIndex]
while thisColor != 'yellow':
	print(thisColor)
	nIndex = nIndex + 1
	thisColor =  strList[nIndex]

#### CASE STATEMENT
# Doesn't exist!
