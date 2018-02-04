import pandas as pd
import numpy as np

#Create two lists
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#Join them together
BabyDataSet = list(zip(names,births))
print(BabyDataSet)

print(births)