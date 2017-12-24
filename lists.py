##########################################
# Creating a list.  Note the brackets
bicycles = ['Trek','Giant','Huffy','Schwinn','Bianchi']
print(bicycles)
print("Last element of a list [-1]",bicycles[-1])

# Adding new items to a list.  First to the end
bicycles.append('Specialized')
print("Last element of a list [-1]",bicycles[-1])
# Adding new items to a list. Now to the front
bicycles.insert(0,'Cannondale')
print(bicycles)

### Deleting elements in a list. First by index
bicycles2 = bicycles
print("Oops!  I didn't copy the list. I created a variable that points at the same list.", (bicycles is bicycles2))

### Make a separate copy of a list
bicycles2 = list(bicycles)
del bicycles2[0]
print(bicycles2)
#### Now by value
bicycles2.remove('Huffy')
print(bicycles2)

### Poping an element from a list.  Remove the last item but do something with it
bicycles2 = list(bicycles)
print("Remaining bicycles: ", bicycles2)
lastBike = bicycles2.pop()
print("Remaining bicycles: ", bicycles2)
print("Popped bike: ",lastBike)

##### Ordering
bicycles.sort()
print("Reorder lists with .sort(): ", bicycles)

### Length of a list
print("Number of bicycles: ",len(bicycles))


########################################################################################
#####################  LOOPING  ############################
########################################################################################
for bike in bicycles:
    print(bike)


#### List comprehension.  Building a list in one line
squares = [value**2 for value in range(1,15)]
print(squares)
