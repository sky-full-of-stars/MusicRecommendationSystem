#store <clusterid, num-of-songs> in hashmap
#using this hmap update centroid.csv

import csv
import pandas as pd
df = pd.read_csv("centroid.csv")
df=df.copy()

print(df)
pd.options.mode.chained_assignment = None 
hashmap={}

for i in range(0,7):
	csvfilename="cluster"+str(i)+".csv"
	input_file = open(csvfilename,"r+")
	reader_file = csv.reader(input_file)
	length = len(list(reader_file))
	hashmap[i]=length

for i in range(0,7):
    print(i)
    print("---")
    print(hashmap[i])

for i in range(1,7):
	#update i+1th row in csv file with hashmap[i]
	#for the column numOfSongs
	#df.set_value(i+1, "numOfSongs", hashmap[i]
    #print(df.iloc[0][6])
    df.iloc[i, df.columns.get_loc('numOfSongs')] = hashmap[i]
	
    
    
print(df)