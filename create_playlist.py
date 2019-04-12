# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:51:49 2019

@author: Madhura
Implementation of playlist creation.
Average of the features is maintained separately for each user.(considered an array for now)
"""
import heapq

#avg[genre][feature]
#need to populate songs in the same proportion as listened by the user.
#count[genre] count of the number of songs heard from each genre.

def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return sqrt(
				(p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
				)
    
def create_playlists(avg,count,n,user_genres,total_songs):
    max_songs = 100 #max number of songs in a playlist
    #playlsit is built only if the total number of songs heard reaches a certain number
    #yet to be decided
    some_threshold = 10 #yet to be decided
    playlists = []
    for i in user_genres:
        number_of_songs=(count[i]/total_songs)*max_songs;
        #populate the songs
        #select the songs nearest to the avg of the given genre
        df = pd.read_csv("cluster"+i+".csv")
        name = df.filename
        f1 = df.tonnetz
		f2 = df.mfccs
		f3= df.chroma
		f4 = df.mel
		f5 = df.contrast
        distance_map = {}
        for (f1,f2,f3,f4,f5):
            dist = distance(f1,f2,f3,f4,f5,avg[i][0],avg[i][1],avg[i][2],avg[i][3],avg[i][4])
            if dist not in distance_map:
                distance_map[dist] = [name]
            else:
                song_list = distance_map[dist]
                song_list.add(name)
                distance_map[dist] = song_list
        heapq.heapify(distance_map)
        playlist = []
        for j in number_of_songs:
            songs = heapq.heappop(distance_map)
            for song in songs:
                playlist.add(song)
        playlists.add(playlist)
    return playlists
        
        
            
            
            
            
        
        
        
        
    
    

