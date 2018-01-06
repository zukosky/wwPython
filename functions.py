import datetime
import time
######## Basic format for creating a function, no arguments
def getTime():
    print(datetime.datetime.now())
    print(datetime.datetime.now().time())
#################  FUNCTION CALL ##########################
getTime()
###########################################################
######## Basic format for creating a function, one argument
def getUppercaseString(strVal):
    print(strVal.upper())
#################  FUNCTION CALL ##########################
getUppercaseString("Here is a mixed-case string converted to upper")
###########################################################
######## Returning a value ########################################
def getNumberSquared(numVal):
    valSquared = numVal * numVal
    return valSquared
#################  FUNCTION CALL ##########################
print(getNumberSquared(5))
###########################################################
######## Returning a value WITHOUT an explicite return statement.  Problem: None is returned########################################
def getLowercaseString(strVal):
    valLC = strVal.lower()
#################  FUNCTION CALL ##########################
print(getLowercaseString("Here is a mixed-case string incorrectly converted to lower"))
print("That returned None because I didn't have an explicit return statement value ")
###########################################################
######## Returning a list ########################################
def getFiveNumberSequence(valStart):
    #This is an example of list comprehension
    seq = [value for value in range(valStart, valStart+5)]
    return seq
#################  FUNCTION CALL ##########################
print(getFiveNumberSequence(10))
###########################################################
