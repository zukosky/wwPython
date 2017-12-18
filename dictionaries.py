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

