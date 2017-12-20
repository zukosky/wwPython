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
