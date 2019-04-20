# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:51:49 2019

@author: Madhura
Implementation of playlist creation.
Average of the features is maintained separately for each user.(considered an array for now)
"""
import heapq
import pandas as pd
import math
#avg[genre][feature]
#need to populate songs in the same proportion as listened by the user.
#count[genre] count of the number of songs heard from each genre.

def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return math.sqrt(
				(p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
				)
    
def create_playlists(avg,count,user_genres,total_songs):
    max_songs = 100 #max number of songs in a playlist
    #playlsit is built only if the total number of songs heard reaches a certain number
    #yet to be decided
    some_threshold = 10 #yet to be decided
    playlists = []
    for i in user_genres:
        number_of_songs=(count[i]/total_songs)*max_songs;
        #populate the songs
        #select the songs nearest to the avg of the given genre
        df = pd.read_csv("cluster"+str(i)+".csv")
        name = df.filename
        f1 = df.tonnetz
        f2 = df.mfcc
        f3= df.chroma
        f4 = df.mel
        f5 = df.contrast
        distance_map = {}
        dist_array = []
        for (songname,v1,v2,v3,v4,v5) in zip(name,f1,f2,f3,f4,f5):
            dist = distance(v1,v2,v3,v4,v5,avg[i][0],avg[i][1],avg[i][2],avg[i][3],avg[i][4])
            if dist not in distance_map:
                dist_array.append(dist)
                song_list = []
                song_list.append(songname)
                distance_map[dist] = song_list
            else:
                song_list = distance_map[dist]
                song_list.append(songname)
                distance_map[dist] = song_list
        heapq.heapify(dist_array)
        playlist = []
        while number_of_songs > 0 and len(dist_array)>0:
            closest = heapq.heappop(dist_array)
            songs = distance_map[closest]
            for song in songs:
                playlist.append(song)
            number_of_songs -= len(songs)
        playlists.append(playlist)
    return playlists
        

df = pd.read_csv("user_history.csv")
print(df)
clusterid = df.clusterid
f1 = df.avgf1
f2 = df.avgf2
f3= df.avgf3
f4 = df.avgf4
f5 = df.avgf5
cnt = df.bitch
print(cnt)
avg = []
songs_count = []
total_count = 0
user_genres = []
for (clusterid,v1,v2,v3,v4,v5,count) in zip(clusterid,f1,f2,f3,f4,f5,cnt):
    avg_f = []
    avg_f.append(v1)
    avg_f.append(v2)
    avg_f.append(v3)
    avg_f.append(v4)
    avg_f.append(v5)
    avg.append(avg_f)
    songs_count.append(count)
    total_count += count
    user_genres.append(clusterid)
playlists = create_playlists(avg,songs_count,user_genres,total_count)
for i in playlists:
    print(i)
    print("___________________________________________________________________")
    for i in range(0,5):
        print("\n")
            
        
        
        
        
    
    

