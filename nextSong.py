"""
Author:akshay
written in sublime
didnt even complile
contains complete implementation of recomendation of next song part
"""


import queue 
songHistory= queue.Queue(maxsize=10)


def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return sqrt(
				(p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
				)


countOfNewSongs = 0 
newSong="new song name here"
def nextSongRecommendationModule(newSong):
	#s=Set()
	hashmap={}
	#fetch data from column names of 6 csv files
	import pandas as pd
	for i in range(1,7):
		csv_file_name="cluster"+i+".csv"
		df = pd.read_csv(csv_file_name)
		songs=df.filename;
		#will fail for cluster11.csv BEWARE
		clusterId=csv_file_name[7]
		for songName in songs:
			#s.add( ("songName",clusterId) )
			hashmap["songName"]="clusterId"
		
		#if s.contains(newSong):
		y, sr = librosa.load(newSong)
		[a,b,c,d,e]=features(y,sr)
		if newSong in hashmap:
			clusterId= hashmap[newSong]
			df = pd.read_csv("cluster"+clusterId+".csv")
			name=df.filename
			f1 = df.tonnetz
			f2 =df.mfccs
			f3=df.chroma
			f4 =df.mel
			f5 =df.contrast
			minimum=1000000000;
            temp= minimum
            nearestSong=newSong
			for (songname,v1,v2,v3,v4,v5) in zip(name,f1,f2,f3,f4,f5):
				if(newSong == songName):
                    pass
				dist=distance(a,b,c,d,e,v1,v2,v3,v4,v5)
				if(dist<min):
                    temp=min
                    secondNearest=nearestSong
					min = dist
					nearestSong=songname

			print("nearest song is"+neartestSong)
            
            if(neartestSong in songHistory):
                nextSongRecommendationModule(secondNearest)
            else:
                if(songHistory.full()):
                    songHistory.pop()
                songHistory.append(newSong)     
		else:
			countOfNewSongs=countOfNewSongs+1
			df = pd.read_csv("centroid.csv")
			id=df.cluster_number
			f1 = df.tonnetz
			f2 =df.mfccs
			f3=df.chroma
			f4 =df.mel
			f5 =df.contrast
			minimum=10000000000;
			for (clusterId,c1,c2,c3,c4,c5) in zip(id,f1,f2,f3,f4,f5):
				dist=distance(c1,c2,c3,c4,c5,v1,v2,v3,v4,v5)
				if(dist<min):
					min=dist
					clusterSongBelongsTo=clusterId

			#add song to expected cluster...update csv

			newRow = [newSong,a,b,c,d,e]
			csvname= "cluster"+ clusterSongBelongsTo+".csv"
			with open(csvname,'a') as fd:
				fd.write(newRow)
        

			#modify centroid?
			df = pd.read_csv("centroid.csv")
			numOfSongs = df.numOfSongs
			id=df.cluster_number
			f1 = df.tonnetz
			f2 =df.mfccs
			f3=df.chroma
			f4 =df.mel
			f5 =df.contrast
			for (id,v1,v2,v3,v4,v5,count) in zip(id,f1,f2,f3,f4,f5,numOfSongs):
				if(id==clusterSongBelongsTo):
					v1=(v1*count+a)/(count+1)
					v2=(v2*count+b)/(count+1)
					v3=(v3*count+c)/(count+1)
					v4=(v4*count+d)/(count+1)
					v5=(v5*count+e)/(count+1)
					df[1]=v1 df[2]=v2 df[3]=v3 df[4]=v4 df[5]=v5 df[6]=count+1
                    
                    
            songHistory.append(newSong)
			print("song belongs to", clusterSongBelongsTo)
			write(data.csv,newSong,a,b,c,d,e)
			#write("cluster"+clusterSongBelongsTo+".csv",newSong,a,b,c,d,e)