"""
Author:akshay
written in sublime
didnt even complile
contains complete implementation of recomendation of next song part
"""

def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return sqrt(
				(p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
				)

def nextSongRecommendationModule():
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
		newSong="new song name here"
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
			for (songname,v1,v2,v3,v4,v5) in zip(name,f1,f2,f3,f4,f5):
				dist=distance(a,b,c,d,e,v1,v2,v3,v4,v5)
				if(dist<min):
					min = dist
					nearestSong=songname

			print(neartestSong)
		else:
			df = pd.read_csv(centroid.csv")
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

			print("song belongs to", clusterSongBelongsTo)
			write(data.csv,newSong,a,b,c,d,e)
			write("cluster"+clusterSongBelongsTo+".csv"+,newSong,a,b,c,d,e)