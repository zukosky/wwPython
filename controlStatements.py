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

#Using xrange instead of range.  Generates the numbers as needed instead of all at once
for nIndex in xrange(0,12):
	print(nIndex)
