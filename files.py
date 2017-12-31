# Reading a bar-delimited file
fName = "oui-clean.txt"
fileHandle = open(fName, 'r')
ouiRef = {}
oui =[]
manu = []
for line in fileHandle:
    fields = line.split('|')  # Only reads one line at a time
    oui.append(fields[0])
    manu.append(fields[1].rstrip())  #.rstrip() removes the trailing \n

fileHandle.close()

print(len(oui))
print(len(manu))
print(oui[0:3])
print(manu[0:3])
ouiRef = dict(zip(oui,manu))
#print(ouiRef.keys())
#print(ouiRef.values())
thisOui = ouiRef.get('14:A7:8B'.replace(':','-'),"")
print(thisOui)
#print(ouiRef.keys())