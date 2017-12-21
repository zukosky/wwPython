#Creating a static dictionary of different types of information for one object
signals = {'model':'MD11',
           'year':'2010',
           'signalStrength':'15'}
#Creating a static dictionary of the same type of information for multiple objects
houseColors = {'1640':'grey',
               '1642':'white',
               '1650':'red',
               '1652':'blue',
               }
#Print one value for one key
print(signals['model'])
#Print all of the keys themselves
print(signals.keys())
#Print all of the values themselves
print(signals.values())
#Starting with an empty dictionary
signalsFromScratch = {}
signalsFromScratch['model'] = '777'
signalsFromScratch['year'] = '2015'
signalsFromScratch['signalStrength'] = '28'
print(signalsFromScratch.keys())
#Modifying and deleting values
signalsFromScratch['model'] = '788'
print(signalsFromScratch['model'])
del(signalsFromScratch['signalStrength'])
print(signalsFromScratch.keys())
print(signalsFromScratch.values())

#Looping through all of the keys and values in a dictionary
for key,value in signals.items():
    print(key + ": " + "\t" + value)
for key,value in houseColors.items():
    print(key + ": " + "\t" + value)

#The default method is to loop over keys.  Note the absence of .keys
for thisKey in houseColors:
    print(thisKey)

#There isn't a default sorting order, so you have to introduce a sorting function:

for thisValue in sorted(houseColors.values()):
    print(thisValue)

#Print the number of  key value pairs
print("Number of  elements: " +  str(len(signals)))

# Copying a dictionary
signalsCopy = signals.copy()

#Emptying a dictionary
signalsCopy.clear


#############################################################################################
################################   NESTING   ################################################
#############################################################################################
# Example of lists of dictionaries. Used when each dictionary contains many kinds of information
# about the same object.  E.g. everything about one user.  List of dictionary becomes a list of users.
print("Creating a list of dictionaries...")
signal1 = {'model':'MD11',
           'year':'2010',
           'signalStrength':'15'}
signal2 = {'model':'777',
           'year':'2016',
           'signalStrength':'18'}
signal3 = {'model':'747',
           'year':'1990',
           'signalStrength':'12'}

signalsList = [signal1, signal2, signal3]
print("Values within the list of dictionaries:")
for signal in signalsList:
    print(signal.values())

#example of dictionary with lists
signal4 = {'model':'777',
           'year':'2016',
           'signalStrength':'18',
           'stops':['0RD','PRV','PDX','LGA']
}
for values in signal4.values():
    print(values)

#Example of dictionary within a dictionary

planes = { '777': {
    'engines':2,
    'passengers':'350'
},
 'MD11': {
    'engines':3,
    'passengers':'300'
}
}

for key in planes.keys():
    print(key)
    print(planes[key])